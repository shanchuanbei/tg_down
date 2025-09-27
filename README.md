# 🎬 Telegram 大文件下载机器人

> 支持实时进度显示的 Telegram 用户机器人，无文件大小限制，专为大文件传输优化
> 仅在dibian13系统上运行完美，理论上dibian12也可以的

## ✨ 特色功能

## 无需安装docker，无需下载二进制文件，直接由python脚本驱动，超稳定
  
- **📊 实时进度显示** - 动态进度条，直观显示下载状态
- **🚫 无文件大小限制** - 支持任意大小的文件下载
- **💾 本地存储** - 文件直接保存到服务器本地
- **🔄 自动重试机制** - 网络中断自动恢复下载
- **🎯 智能文件名识别** - 自动获取原始文件名
- **📱 多格式支持** - 支持文档、视频等各种文件类型

⬇️ 存储端支持
├── 本地磁盘（支持）
├── WebDAV（暂不支持）
├── Alist（暂不支持）

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

1. **下载脚本**
```bash
sudo mkdir -p /opt/tg_down && cd /opt/tg_down
wget https://raw.githubusercontent.com/shanchuanbei/tg_down/refs/heads/main/tg.py -O tg.py
```

2. **安装依赖**
```bash
apt update && apt install -y python3-pip
pip3 install --break-system-packages "python-telegram-bot==13.15"
pip3 install --break-system-packages telethon
pip3 install --break-system-packages aiofiles aiohttp
```

3. **配置参数**
```python
# 在脚本中配置以下参数
API_ID = 1234567                    # 你的 API ID
API_HASH = "your_api_hash_here"     # 你的 API Hash
DOWNLOAD_DIR = "/path/to/downloads" # 下载目录
```

4. **运行机器人**
第一次运行需要前台启动 会让你输入机器人API列如：8554455525:esdfhdsajkdqwijhfisajfsiuhufuew
```bash
python3 tg.py
```
5. **用systemd后台启动**
前台启动完成后用ctrl+C结束命令然后一键配置systemd
```bash
sudo cat > /etc/systemd/system/tgdown.service << EOF
[Unit]
Description=tgdown - 大文件下载器
After=network.target
Wants=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/tg_down
ExecStart=/usr/bin/python3 /opt/tg_down/tg.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
Environment=PYTHONUNBUFFERED=1

LimitNOFILE=65536
TimeoutStopSec=30

[Install]
WantedBy=multi-user.target
EOF
```
启动
```bash
sudo systemctl start tgdown
```
停止
```bash
sudo systemctl stop tgdown
```
重启
```bash
sudo systemctl restart tgdown
```
开机自启
```bash
sudo systemctl enable tgdown
```
检查服务状态
```bash
sudo systemctl status tgdown
```
查看运行日志
```bash
sudo journalctl -u tgdown -f
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

