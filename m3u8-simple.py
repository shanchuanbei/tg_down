#!/usr/bin/env python3
"""
极简M3U8下载器
"""

import os

# 获取输入
title = input("🎬 影片标题: ").strip()
url = input("🔗 M3U8链接: ").strip()

# 执行命令（去掉日志重定向）
cmd = f"""cd /opt/m3u8DL && ulimit -n 10000 && nohup ./N_m3u8DL-RE "{url}" \
--save-dir "/mnt/data/nas/待整理" \
--save-name "{title}" \
--thread-count 64 \
--use-system-proxy false \
> /dev/null 2>&1 &"""

os.system(cmd)
print(f"\n✅ 下载已启动: {title}")
print(f"💾 保存到: /mnt/data/nas/待整理/{title}.mp4")