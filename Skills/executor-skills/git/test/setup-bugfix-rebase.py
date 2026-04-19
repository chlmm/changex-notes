#!/usr/bin/env python3
"""
Bug 修复 rebase 流程

真实场景: 生产环境发现 bug，从 master 拉出修复分支，修复期间 master 有新提交，
需要用 rebase 将修复基于最新代码验证，确保修复在最新代码上仍然有效。

流程:
  1. git checkout -b bugFix        # 发现 bug，从 master 拉出修复分支
  2. git commit                    # 提交修复代码
  3. git checkout master           # 回到主分支
  4. git commit                    # 修复期间 master 有新合入
  5. git checkout bugFix           # 回到修复分支
  6. git rebase master             # 基于最新代码验证修复

为什么用 rebase 而不是 merge:
  - bug 修复必须是线性的：先有 bug，再有修复，历史应清晰反映这一因果关系
  - merge 会产生分叉，模糊了"修复"这个动作的独立性
  - rebase 后合并到 master 是 fast-forward，不产生多余的 merge commit
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-bugfix-rebase"


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
    run("git checkout -b bugFix", cwd=repo_path)

    # 步骤 2: 在 bugFix 上提交修复（修复空密码校验）
    with open(os.path.join(repo_path, "auth.py"), "w") as f:
        f.write("def login(username, password):\n    if not password:\n        raise ValueError('password required')\n    return True\n")
    run("git add auth.py", cwd=repo_path)
    run("git commit -m 'fix(auth): validate empty password on login'", cwd=repo_path)

    # 步骤 3: 回到 master
    run("git checkout master", cwd=repo_path)

    # 步骤 4: master 上有其他提交（同事合入的新功能）
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("from auth import login\n\ndef main():\n    login('admin', '')\n\ndef logout():\n    print('logged out')\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: add logout function'", cwd=repo_path)

    # 步骤 5: 切回 bugFix
    run("git checkout bugFix", cwd=repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("场景: 你修复了 auth.py 的空密码 bug 并提交到 bugFix 分支，")
    print("      但 master 上已有同事的新提交，需要 rebase 确保修复基于最新代码。")
    print()
    print("当前状态:")
    print("  bugFix: 修复了空密码校验（基于旧 master）")
    print("  master: 新增了 logout 功能")
    print()
    print("操作:")
    print("  git rebase master              # 将 bugFix 变基到 master 最新提交")
    print("  git checkout master            # 切回 master")
    print("  git merge bugFix               # fast-forward 合并修复")
    print()
    print("验证:")
    print("  git log --oneline --graph      # 线性历史：init -> logout -> fix")
    print("  cat auth.py                    # 修复仍然有效")
    print("  cat app.py                     # logout 功能也在")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
