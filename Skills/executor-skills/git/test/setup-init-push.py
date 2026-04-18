#!/usr/bin/env python3
"""
T04: 从零初始化并推送项目

场景: 本地有一个项目目录，还没有用 Git 管理
目标: 初始化仓库、关联远程、完成首次推送
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-init-push"


def run(cmd, cwd=None):
    subprocess.run(cmd, shell=True, cwd=cwd, check=True,
                   capture_output=True, text=True)


def setup():
    repo_path = os.path.join(tempfile.gettempdir(), REPO_NAME)

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    os.makedirs(repo_path)

    # 创建项目文件（不初始化 git，让用户来做）
    with open(os.path.join(repo_path, "README.md"), "w") as f:
        f.write("# My Project\n\nA awesome project.\n")
    with open(os.path.join(repo_path, "main.py"), "w") as f:
        f.write("def main():\n    print('Hello, World!')\n\nif __name__ == '__main__':\n    main()\n")
    with open(os.path.join(repo_path, "requirements.txt"), "w") as f:
        f.write("# dependencies\n")

    # 预创建一个空的远程 bare repo
    remote_path = repo_path + "-remote.git"
    if os.path.exists(remote_path):
        shutil.rmtree(remote_path)
    os.makedirs(remote_path)
    run("git init --bare", cwd=remote_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print(f"   远程仓库: {remote_path}")
    print()
    print("T04 目标: 初始化仓库、关联远程、首次推送")
    print("  1. git init")
    print("  2. git add .")
    print("  3. git commit -m 'feat: initialize project'")
    print(f"  4. git remote add origin {remote_path}")
    print("  5. git branch -M main")
    print("  6. git push -u origin main")
    print()
    print("验证:")
    print("  git remote -v              # 显示远程地址")
    print("  git log --oneline          # 有初始提交")
    print(f"  git ls-remote {remote_path}  # 远程仓库有 main 分支")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
