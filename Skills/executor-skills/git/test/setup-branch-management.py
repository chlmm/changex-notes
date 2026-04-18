#!/usr/bin/env python3
"""
T03: 合并后清理分支

场景: feature/login 已合并到 main，但本地和远程都还有这个分支
目标: 清理本地和远程的 feature/login 分支
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-branch-management"


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
        f.write("def app():\n    pass\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: initialize app'", cwd=repo_path)

    # 创建 feature/login 分支并开发
    run("git checkout -b feature/login", cwd=repo_path)
    with open(os.path.join(repo_path, "login.py"), "w") as f:
        f.write("def login(username, password):\n    # authenticate user\n    return True\n")
    run("git add login.py", cwd=repo_path)
    run("git commit -m 'feat(auth): add login functionality'", cwd=repo_path)

    # 合并回 main
    run("git checkout main", cwd=repo_path)
    run("git merge feature/login", cwd=repo_path)

    # 模拟远程仓库（用本地 bare repo 代替）
    remote_path = repo_path + "-remote.git"
    if os.path.exists(remote_path):
        shutil.rmtree(remote_path)
    run(f"git clone --bare {repo_path} {remote_path}")
    run(f"git remote add origin {remote_path}", cwd=repo_path)
    run("git push origin main", cwd=repo_path)
    run("git push origin feature/login", cwd=repo_path)

    # 设置上游跟踪
    run("git branch --set-upstream-to=origin/main main", cwd=repo_path)
    run("git branch --set-upstream-to=origin/feature/login feature/login", cwd=repo_path)

    # 回到 feature/login，模拟"合并后未清理"的状态
    run("git checkout feature/login", cwd=repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T03 目标: feature/login 已合并到 main，请清理本地和远程的 feature/login 分支")
    print("  删除本地: git branch -d feature/login")
    print("  删除远程: git push origin --delete feature/login")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
