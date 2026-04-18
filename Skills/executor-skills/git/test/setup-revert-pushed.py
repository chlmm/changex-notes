#!/usr/bin/env python3
"""
T12: 用 revert 回退已推送的提交

场景: 昨天推送的一个 commit 有 bug，但已经有人基于它开发了，不能用 reset
目标: 用 git revert 安全回退，创建一个反向提交
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-revert-pushed"


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
        f.write("def add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n")
    run("git add calculator.py", cwd=repo_path)
    run("git commit -m 'feat: add calculator basics'", cwd=repo_path)

    # 正常的功能提交
    with open(os.path.join(repo_path, "calculator.py"), "w") as f:
        f.write("def add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n\ndef multiply(a, b):\n    return a * b\n")
    run("git add calculator.py", cwd=repo_path)
    run("git commit -m 'feat: add multiply function'", cwd=repo_path)

    # 有 bug 的提交（需要 revert 这个）
    with open(os.path.join(repo_path, "calculator.py"), "w") as f:
        f.write("def add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n\ndef multiply(a, b):\n    return a * b\n\ndef divide(a, b):\n    return a / b  # BUG: no zero check!\n")
    run("git add calculator.py", cwd=repo_path)
    run("git commit -m 'feat: add divide function'", cwd=repo_path)

    # 模拟已推送（创建远程 bare repo）
    remote_path = repo_path + "-remote.git"
    if os.path.exists(remote_path):
        shutil.rmtree(remote_path)
    run(f"git clone --bare {repo_path} {remote_path}")
    run(f"git remote add origin {remote_path}", cwd=repo_path)
    run("git push -u origin main", cwd=repo_path)

    # 模拟同事基于有 bug 的提交做了新开发
    colleague_repo = repo_path + "-colleague"
    if os.path.exists(colleague_repo):
        shutil.rmtree(colleague_repo)
    run(f"git clone {remote_path} {colleague_repo}")
    run("git config user.email 'colleague@example.com'", cwd=colleague_repo)
    run("git config user.name 'Colleague'", cwd=colleague_repo)

    with open(os.path.join(colleague_repo, "utils.py"), "w") as f:
        f.write("def format_result(val):\n    return f'Result: {val}'\n")
    run("git add utils.py", cwd=colleague_repo)
    run("git commit -m 'feat: add result formatter'", cwd=colleague_repo)
    run("git push origin main", cwd=colleague_repo)

    # 清理同事目录
    shutil.rmtree(colleague_repo)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T12 目标: 用 revert 安全回退有 bug 的 divide 函数提交")
    print("  1. git log --oneline  # 找到 'feat: add divide function' 的 hash")
    print("  2. git revert <commit-hash>  # 不要用 -n，让 git 自动创建 revert commit")
    print("  3. git push origin main")
    print()
    print("⚠️  注意: 不能用 git reset！因为同事已经基于它开发了")
    print("   用 revert 会创建一个新的反向 commit，不破坏历史")
    print()
    print("验证:")
    print("  git log --oneline       # 有 'Revert feat: add divide function' 的提交")
    print("  cat calculator.py       # divide 函数被移除了")
    print("  原始 commit 仍在历史中  # 安全回退，不重写历史")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
