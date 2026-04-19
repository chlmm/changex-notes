#!/usr/bin/env python3
"""
Bug 修复基本流程：分支隔离 + 合并

真实场景: 生产环境发现 bug，拉出修复分支，修完直接合并回来。
这个场景下没有人和你并行开发，master 在你修复期间没有变动，
合并时自动 fast-forward，历史始终线性。

流程:
  1. git branch bugFix           # 发现 bug，从 master 拉出修复分支
  2. git checkout bugFix         # 切到修复分支
  3. git commit                  # 提交修复代码
  4. git checkout master         # 回到主分支
  5. git merge bugFix            # 合并修复（fast-forward）

对比 T09 (Bug 修复 rebase 流程):
  本场景: master 没动过 → 直接 merge 就是 fast-forward
  T09:    master 有新提交 → 先 rebase 再 merge，保持线性历史

这是最常见的 bug 修复方式，也是所有分支工作的基础模式：
  用分支隔离改动，做完后合回来。
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-bugfix-merge"


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

    # master 上的初始代码（包含一个 bug：用户登录没有校验空密码）
    with open(os.path.join(repo_path, "auth.py"), "w") as f:
        f.write("def login(username, password):\n    # BUG: 没有校验空密码\n    return True\n")
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("from auth import login\n\ndef main():\n    login('admin', '')\n")
    run("git add .", cwd=repo_path)
    run("git commit -m 'feat: add auth module'", cwd=repo_path)

    # 步骤 1: 发现 bug，从 master 拉出修复分支
    run("git branch bugFix", cwd=repo_path)

    # 步骤 2: 切到修复分支
    run("git checkout bugFix", cwd=repo_path)

    # 步骤 3: 在 bugFix 上提交修复（修复空密码校验）
    with open(os.path.join(repo_path, "auth.py"), "w") as f:
        f.write("def login(username, password):\n    if not password:\n        raise ValueError('password required')\n    return True\n")
    run("git add auth.py", cwd=repo_path)
    run("git commit -m 'fix(auth): validate empty password on login'", cwd=repo_path)

    # 步骤 4: 回到 master（注意：master 没有新提交，还是停在初始位置）
    run("git checkout master", cwd=repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("场景: 你修复了 auth.py 的空密码 bug 并提交到 bugFix 分支，")
    print("      修复期间没有其他人提交代码到 master。")
    print()
    print("当前状态:")
    print("  bugFix: 修复了空密码校验")
    print("  master: 停在初始提交（没有新提交）")
    print()
    print("操作:")
    print("  git merge bugFix               # 直接合并（fast-forward）")
    print("  git branch -d bugFix           # 合并后清理分支")
    print()
    print("验证:")
    print("  git log --oneline --graph      # 线性历史：init -> fix")
    print("  git branch -d bugFix           # 可以安全删除 bugFix")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
