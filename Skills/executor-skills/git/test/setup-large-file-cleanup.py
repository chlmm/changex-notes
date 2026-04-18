#!/usr/bin/env python3
"""
T14: 清理误提交的大文件

场景: 不小心把一个 50MB 的日志文件 app.log 提交到了仓库，即使删除了文件仓库体积依然很大
目标: 彻底从 Git 历史中移除 app.log
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-large-file-cleanup"


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
        f.write("def main():\n    print('hello world')\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: initialize project'", cwd=repo_path)

    # 误提交大日志文件（模拟 50MB，实际创建 5MB 用于测试）
    log_content = "2024-01-01 INFO Starting application\n" * 100000
    with open(os.path.join(repo_path, "app.log"), "w") as f:
        f.write(log_content)
    run("git add app.log", cwd=repo_path)
    run("git commit -m 'chore: add log file (MISTAKE)'", cwd=repo_path)

    # 后续正常提交
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("def main():\n    print('hello world')\n\ndef greet(name):\n    return f'Hello, {name}'\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: add greet function'", cwd=repo_path)

    # 意识到错误，删除了文件但历史还在
    os.remove(os.path.join(repo_path, "app.log"))
    run("git add -A", cwd=repo_path)
    run("git commit -m 'chore: remove log file'", cwd=repo_path)

    # 添加 .gitignore 防止再犯
    with open(os.path.join(repo_path, ".gitignore"), "w") as f:
        f.write("*.log\n")
    run("git add .gitignore", cwd=repo_path)
    run("git commit -m 'chore: add gitignore for log files'", cwd=repo_path)

    # 验证大文件仍在历史中
    result = subprocess.run(
        "git log --all --oneline -- app.log",
        shell=True, cwd=repo_path, capture_output=True, text=True
    )

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T14 目标: 彻底从 Git 历史中移除 app.log")
    print("  方法1 (推荐): git filter-repo --path app.log --invert-paths")
    print("  方法2: git filter-branch --force --index-filter \\")
    print("           'git rm --cached --ignore-unmatch app.log' -- --all")
    print("  然后: git gc --prune=now --aggressive")
    print()
    print("验证: git log --all -- app.log 无输出")
    print()
    print(f"进入测试: cd {repo_path}")
    print()
    print("⚠️  提示: filter-repo 需要安装 (pip install git-filter-repo)")
    print("   filter-branch 是内置命令但较慢，两者选一即可")


if __name__ == "__main__":
    setup()
