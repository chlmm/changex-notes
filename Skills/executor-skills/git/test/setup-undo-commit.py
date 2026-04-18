#!/usr/bin/env python3
"""
T07: 撤销未推送的提交

场景: 本地提交了 2 个 commit 还没 push，第二个 commit 有问题
目标: 撤销第二个 commit，保留第一个
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-undo-commit"


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
    with open(os.path.join(repo_path, "calculator.py"), "w") as f:
        f.write("def add(a, b):\n    return a + b\n")
    run("git add calculator.py", cwd=repo_path)
    run("git commit -m 'feat: add calculator with add function'", cwd=repo_path)

    # 第一个 commit（正确的）
    with open(os.path.join(repo_path, "calculator.py"), "w") as f:
        f.write("def add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n")
    run("git add calculator.py", cwd=repo_path)
    run("git commit -m 'feat: add subtract function'", cwd=repo_path)

    # 第二个 commit（有问题的 - 错误的实现）
    with open(os.path.join(repo_path, "calculator.py"), "w") as f:
        f.write("def add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n\ndef multiply(a, b):\n    return a + b  # BUG: should be a * b\n")
    run("git add calculator.py", cwd=repo_path)
    run("git commit -m 'feat: add multiply function (BROKEN)'", cwd=repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T07 目标: 撤销第二个 commit（multiply），保留第一个（subtract）")
    print("  git reset --soft HEAD~1   # 撤销提交但保留修改在暂存区")
    print("  或 git reset HEAD~1       # 撤销提交，修改回到工作区")
    print("  或 git reset --hard HEAD~1  # 彻底丢弃（谨慎）")
    print()
    print("验证: git log 只有一个 commit（subtract），没有 multiply 的 commit")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
