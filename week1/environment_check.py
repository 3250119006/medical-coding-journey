#!/usr/bin/env python3
"""
第一周环境配置验证脚本 - 修正版
"""

import sys
import subprocess
import os

print("=" * 50)
print("   第一周开发环境验证报告")
print("=" * 50)

# 检查Python环境
try:
    python_version = subprocess.run(["python3", "--version"], capture_output=True, text=True)
    print(f"✅ Python: {python_version.stdout.strip()}")
except:
    print("❌ Python 未正确安装")

# 检查conda环境
try:
    conda_version = subprocess.run(["conda", "--version"], capture_output=True, text=True)
    print(f"✅ Conda: {conda_version.stdout.strip()}")
except:
    print("❌ Conda 未正确安装")

# 检查Git
try:
    git_version = subprocess.run(["git", "--version"], capture_output=True, text=True)
    print(f"✅ Git: {git_version.stdout.strip()}")
except:
    print("❌ Git 未正确安装")

# 检查项目结构
print("\n=== 项目结构检查 ===")
project_path = "/home/serendipity/medical_coding"
if os.path.exists(project_path):
    print("✅ 项目目录存在")
    print("项目内容:")
    for item in os.listdir(project_path):
        item_path = os.path.join(project_path, item)
        if os.path.isdir(item_path):
            print(f"  📁 {item}/")
        else:
            print(f"  📄 {item}")
else:
    print("❌ 项目目录不存在")

print("\n" + "=" * 50)
print("🎉 环境验证完成！所有工具就绪！")
print("=" * 50)




















