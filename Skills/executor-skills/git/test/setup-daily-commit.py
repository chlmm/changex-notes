#!/usr/bin/env python3
"""
T03: 日常三步曲提交

场景: 修改了 app.py 和新建了 helper.py，需要走 add → commit → push 流程
目标: 完整体验日常提交流程，推送到远程
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-daily-commit"


def run(cmd, cwd=None):
    subprocess.run(cmd, shell=True, cwd=cwd, check=True,
                   capture_output=True, text=True)


def setup():
    repo_path = os.path.join(tempfile.gettempdir(), REPO_NAME)

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    os.makedirs(repo_path)
    run("git init", cwd=repo_path)
    run("git config user.email 'test@example.com'", cwd=repo_path)
    run("git config user.name 'Test User'", cwd=repo_path)

    # 初始提交
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("def app():\n    print('hello')\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: initialize app'", cwd=repo_path)

    # 模拟远程仓库（bare repo）
    remote_path = repo_path + "-remote.git"
    if os.path.exists(remote_path):
        shutil.rmtree(remote_path)
    run(f"git clone --bare {repo_path} {remote_path}")
    run(f"git remote add origin {remote_path}", cwd=repo_path)
    run("git branch -M main", cwd=repo_path)
    run("git push -u origin main", cwd=repo_path)

    # 修改 app.py（未暂存）
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("def app():\n    print('hello world')\n\ndef run():\n    app()\n")

    # 新建 helper.py（未跟踪）
    with open(os.path.join(repo_path, "helper.py"), "w") as f:
        f.write("def format_output(msg):\n    return f'>> {msg}'\n")

    print(f"✅ 测试环境已创建: {repo_path}")
    print(f"   远程仓库: {remote_path}")
    print()
    print("T03 目标: 将修改和新建的文件提交并推送到远程")
    print("  1. git add .")
    print("  2. git commit -m 'feat: add run function and helper module'")
    print("  3. git push origin main")
    print()
    print("验证:")
    print("  git status          # 干净，无未提交修改")
    print("  git log --oneline   # 包含新提交")
    print(f"  git ls-remote {remote_path}  # 远程也有新提交")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
