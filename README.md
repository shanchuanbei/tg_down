# 🎬 Telegram 大文件下载机器人

> 支持实时进度显示的 Telegram 用户机器人，无文件大小限制，专为大文件传输优化

## ✨ 特色功能

- **📊 实时进度显示** - 动态进度条，直观显示下载状态
- **🚫 无文件大小限制** - 支持任意大小的文件下载
- **💾 本地存储** - 文件直接保存到服务器本地
- **🔄 自动重试机制** - 网络中断自动恢复下载
- **🎯 智能文件名识别** - 自动获取原始文件名
- **📱 多格式支持** - 支持文档、视频等各种文件类型

## 📸 界面预览

```
📥 开始下载大文件

📁 文件名: large_video.mp4
📊 文件大小: 2.15 GB
⏳ 进度: [█████░░░░░] 45.2%
⬇️ 已下载: 987.3 MB / 2.15 GB
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Telegram API 账号 ([获取方法](#-telegram-api-配置))

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/yourusername/telegram-file-downloader.git
cd telegram-file-downloader
```

2. **安装依赖**
```bash
pip install telethon
```

3. **配置参数**
```python
# 在脚本中配置以下参数
API_ID = 1234567                    # 你的 API ID
API_HASH = "your_api_hash_here"     # 你的 API Hash
DOWNLOAD_DIR = "/path/to/downloads" # 下载目录
```

4. **运行机器人**
```bash
python tg_downloader.py
```

## ⚙️ Telegram API 配置

1. 访问 [my.telegram.org](https://my.telegram.org/)
2. 登录你的 Telegram 账号
3. 进入 "API Development Tools"
4. 创建新应用，获取 `API_ID` 和 `API_HASH`

## 🎯 使用方法

### 基本命令

- `/start` - 启动机器人，查看功能介绍
- `/status` - 查看下载目录状态和统计信息

### 文件下载

直接向机器人发送任意文件或视频，机器人会自动开始下载并显示实时进度。

### 下载目录结构

```
downloads/
├── video_12345.mp4
├── document_67890.pdf
└── large_file.zip
```

## 🔧 高级配置

### 自定义下载目录

修改脚本中的 `DOWNLOAD_DIR` 变量：

```python
DOWNLOAD_DIR = "/home/user/telegram_downloads"  # Linux
DOWNLOAD_DIR = "D:\\TelegramDownloads"         # Windows
DOWNLOAD_DIR = "/Users/name/Downloads"         # macOS
```

### 进度更新频率调整

修改 `update_interval` 值来控制进度更新频率：

```python
update_interval = 2  # 每2%更新一次（更频繁）
update_interval = 10 # 每10%更新一次（更节省资源）
```

## 📊 功能演示

### 开始下载
用户发送文件 → 机器人回复进度消息 → 实时更新进度

### 进度显示
```
📥 **下载进行中**

📁 文件名: `large_file.zip`
📊 文件大小: 1.5 GB
⏳ 进度: [██████░░░░] 60.0%
⬇️ 已下载: 900.0 MB / 1.5 GB
```

### 下载完成
```
✅ **大文件下载完成！** 🎉

📁 文件名: `large_file.zip`
📊 文件大小: 1.5 GB
📍 保存路径: `/downloads/large_file.zip`
⏰ 下载时间: 1630456789.123
🎬 享受您的大文件！
```

## 🐛 故障排除

### 常见问题

**Q: 机器人无法启动**
```
A: 检查 API_ID 和 API_HASH 是否正确，确保网络连接正常
```

**Q: 下载进度不更新**
```
A: 检查文件权限，确保下载目录可写
```

**Q: 大文件下载中断**
```
A: 机器人支持断点续传，重新发送文件即可继续下载
```

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- [Telethon](https://github.com/LonamiWebs/Telethon) - 优秀的 Telegram 客户端库
- Telegram API - 提供强大的 bot 平台

---

## 💡 使用提示

> ⚠️ **重要提醒**：请遵守 Telegram 使用条款和当地法律法规，仅下载你有权访问的文件。

> 💡 **性能建议**：对于超大文件（10GB+），建议使用稳定的网络环境，并确保服务器有足够的磁盘空间。

---

**星星这个项目 ⭐ 如果你觉得有用！**

---

这个版本已经整合成一个完整的文档，格式正确，可以直接复制粘贴到你的 GitHub 仓库的 README.md 文件中。主要修复了以下问题：

1. **代码块格式** - 使用正确的 Markdown 代码块语法
2. **标题层级** - 统一了标题的层级结构
3. **列表格式** - 修复了列表项的缩进和格式
4. **链接格式** - 修正了内部锚点链接
5. **整体结构** - 重新组织了内容顺序，使其更符合逻辑
