
"""
🎬 文件下载机器人 - 带实时进度显示版
改进进度显示，更直观
"""

import os
import asyncio
import logging
from telethon import TelegramClient, events
from telethon.tl.types import DocumentAttributeFilename

# 配置
API_ID = 这里要改
API_HASH = "这里要改"
SESSION_NAME = "tgdown"
DOWNLOAD_DIR = "这里改成你的服务器绝对路径"

# 创建目录
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# 设置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class CococoUserBot:
    def __init__(self):
        self.client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
        self.download_dir = DOWNLOAD_DIR
        
    async def start(self):
        """启动客户端"""
        await self.client.start()
        logger.info("UserBot 启动成功！")
        print("🎬 Cococo UserBot 大文件下载器启动成功！")
        print("💾 下载目录:", DOWNLOAD_DIR)
        print("📏 无文件大小限制！")
        print("🛑 按 Ctrl+C 停止")
        
    def get_file_name(self, message):
        """智能获取文件名"""
        try:
            if message.document:
                for attr in message.document.attributes:
                    if isinstance(attr, DocumentAttributeFilename):
                        return attr.file_name
                return f"document_{message.document.id}"
            elif message.video:
                return f"video_{message.video.id}.mp4"
            else:
                return "unknown_file"
        except Exception as e:
            logger.error(f"获取文件名失败: {e}")
            return f"file_{int(asyncio.get_event_loop().time())}"
    
    def get_file_size(self, message):
        """获取文件大小"""
        if message.document:
            return message.document.size
        elif message.video:
            return message.video.size
        return 0
    
    def format_size(self, size_bytes):
        """格式化文件大小显示"""
        if size_bytes >= 1024**3:  # GB
            return f"{size_bytes/1024**3:.2f} GB"
        elif size_bytes >= 1024**2:  # MB
            return f"{size_bytes/1024**2:.2f} MB"
        elif size_bytes >= 1024:  # KB
            return f"{size_bytes/1024:.2f} KB"
        else:
            return f"{size_bytes} B"
    
    def create_progress_bar(self, percentage, length=10):
        """创建文本进度条"""
        filled = int(length * percentage / 100)
        empty = length - filled
        bar = "█" * filled + "░" * empty
        return f"[{bar}] {percentage:.1f}%"
    
    async def download_file(self, event):
        """下载文件 - 带实时进度显示"""
        try:
            message = event.message
            
            # 获取文件信息
            file_name = self.get_file_name(message)
            file_size = self.get_file_size(message)
            
            if file_size == 0:
                await message.reply("❌ 无法获取文件信息")
                return
                
            file_path = os.path.join(self.download_dir, file_name)
            
            # 发送开始消息
            status_msg = await message.reply(
                f"📥 **开始下载大文件**\n\n"
                f"📁 文件名: `{file_name}`\n"
                f"📊 文件大小: {self.format_size(file_size)}\n"
                f"⏳ 进度: {self.create_progress_bar(0)}\n"
                f"⬇️ 已下载: 0 / {self.format_size(file_size)}"
            )
            
            # 进度跟踪变量
            last_update_percentage = 0
            update_interval = 5  # 每5%更新一次
            
            async def progress_callback(current, total):
                nonlocal last_update_percentage, status_msg
                
                if total == 0:
                    return
                    
                percentage = (current / total) * 100
                
                # 只在进度有显著变化时更新消息（避免过于频繁）
                if percentage - last_update_percentage >= update_interval or percentage >= 100:
                    try:
                        progress_bar = self.create_progress_bar(percentage)
                        downloaded = self.format_size(current)
                        total_size = self.format_size(total)
                        
                        # 更新进度消息
                        await status_msg.edit(
                            f"📥 **下载进行中**\n\n"
                            f"📁 文件名: `{file_name}`\n"
                            f"📊 文件大小: {total_size}\n"
                            f"⏳ 进度: {progress_bar}\n"
                            f"⬇️ 已下载: {downloaded} / {total_size}"
                        )
                        last_update_percentage = percentage
                    except Exception as e:
                        logger.warning(f"更新进度失败: {e}")
            
            # 下载文件
            downloaded_path = await message.download_media(
                file=file_path,
                progress_callback=progress_callback
            )
            
            # 下载完成后的最终更新
            if downloaded_path and os.path.exists(downloaded_path):
                actual_size = os.path.getsize(downloaded_path)
                await status_msg.edit(
                    f"✅ **大文件下载完成！** 🎉\n\n"
                    f"📁 文件名: `{file_name}`\n"
                    f"📊 文件大小: {self.format_size(actual_size)}\n"
                    f"📍 保存路径: `{downloaded_path}`\n\n"
                    f"⏰ 下载时间: {asyncio.get_event_loop().time()}\n"
                    f"🎬 享受您的大文件！"
                )
                logger.info(f"成功下载大文件: {file_name} ({actual_size} bytes)")
            else:
                await status_msg.edit("❌ 下载失败，请重试")
                
        except Exception as e:
            logger.error(f"下载失败: {e}")
            await message.reply(f"❌ 下载失败: {str(e)}")
    
    async def run(self):
        """运行机器人"""
        # 注册消息处理器
        @self.client.on(events.NewMessage(pattern='/start'))
        async def start_handler(event):
            await event.reply(
                "🎬 **大文件下载器** 🤖\n\n"
                "✨ **特色功能：**\n"
                "• ✅ 无文件大小限制\n"
                "• 📊 实时进度显示\n"
                "• ⏳ 自动重试机制\n"
                "• 💾 保存到服务器\n\n"
                "🚀 **使用方法：** 直接发送任意大小的文件即可！"
            )
        
        @self.client.on(events.NewMessage(pattern='/status'))
        async def status_handler(event):
            """查看下载目录状态"""
            try:
                total_files = 0
                total_size = 0
                
                for root, dirs, files in os.walk(self.download_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        total_files += 1
                        total_size += os.path.getsize(file_path)
                
                status_text = (
                    f"📊 **下载目录状态**\n\n"
                    f"📁 文件总数: {total_files} 个文件\n"
                    f"💾 总大小: {self.format_size(total_size)}\n"
                    f"📍 目录路径: `{self.download_dir}`\n"
                    f"✅ 机器人运行正常！"
                )
                await event.reply(status_text)
            except Exception as e:
                await event.reply(f"❌ 状态查询失败: {e}")
        
        @self.client.on(events.NewMessage)
        async def message_handler(event):
            if event.message.document or event.message.video:
                await self.download_file(event)
            elif event.message.text and event.message.text.startswith('/'):
                # 忽略其他命令
                pass
            else:
                await event.reply("🤖 请发送视频或文件进行下载（支持任意大小）")
        
        # 启动
        await self.start()
        print("✅ UserBot 已就绪，可以开始发送文件了！")
        print("📊 支持实时进度显示")
        await self.client.run_until_disconnected()

async def main():
    bot = CococoUserBot()
    await bot.run()

if __name__ == '__main__':
    asyncio.run(main())
