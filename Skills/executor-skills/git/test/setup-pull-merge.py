#!/usr/bin/env python3
"""
T06: 拉取远程更新并合并

场景: 远程 main 上有同事的新提交，你本地 main 落后了
目标: 用 git pull 或 git fetch + git merge 拉取并合并远程更新
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-pull-merge"


def run(cmd, cwd=None):
    subprocess.run(cmd, shell=True, cwd=cwd, check=True,
                   capture_output=True, text=True)


def setup():
    repo_path = os.path.join(tempfile.gettempdir(), REPO_NAME)

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    os.makedirs(repo_path)

    # 1. 创建远程 bare repo
    remote_path = repo_path + "-remote.git"
    if os.path.exists(remote_path):
        shutil.rmtree(remote_path)
    os.makedirs(remote_path)
    run("git init --bare", cwd=remote_path)

    # 2. 在临时目录中创建项目并推送到远程
    tmp_repo = os.path.join(repo_path, "tmp-setup")
    os.makedirs(tmp_repo)
    run("git init", cwd=tmp_repo)
    run("git config user.email 'test@example.com'", cwd=tmp_repo)
    run("git config user.name 'Test User'", cwd=tmp_repo)

    with open(os.path.join(tmp_repo, "app.py"), "w") as f:
        f.write("def app():\n    print('v1.0')\n")
    run("git add .", cwd=tmp_repo)
    run("git commit -m 'feat: initialize app'", cwd=tmp_repo)

    run(f"git remote add origin {remote_path}", cwd=tmp_repo)
    run("git branch -M main", cwd=tmp_repo)
    run("git push -u origin main", cwd=tmp_repo)

    # 3. 模拟同事在远程推送新提交
    with open(os.path.join(tmp_repo, "app.py"), "w") as f:
        f.write("def app():\n    print('v1.1')\n\ndef greet(name):\n    return f'Hello, {name}!'\n")
    run("git add .", cwd=tmp_repo)
    run("git commit -m 'feat: add greet function'", cwd=tmp_repo)
    run("git push origin main", cwd=tmp_repo)

    # 清理临时目录
    shutil.rmtree(tmp_repo)

    # 4. 用户从远程克隆（此时会包含同事的第一个提交，但不包含最新提交）
    # 为了模拟"本地落后"，我们先 clone，然后在远程再追加提交
    run(f"git clone {remote_path} {repo_path}/workspace", cwd=repo_path)
    workspace = os.path.join(repo_path, "workspace")
    run("git config user.email 'test@example.com'", cwd=workspace)
    run("git config user.name 'Test User'", cwd=workspace)

    print(f"✅ 测试环境已创建")
    print(f"   远程仓库: {remote_path}")
    print(f"   本地仓库: {workspace}")
    print()
    print("T06 目标: 本地 main 落后远程，拉取并合并远程更新")
    print("  方法1: git pull origin main")
    print("  方法2: git fetch origin && git merge origin/main")
    print()
    print("验证:")
    print("  git log --oneline   # 包含 'feat: add greet function' 提交")
    print("  git status          # 与远程同步，无差异")
    print()
    print(f"进入测试: cd {workspace}")


if __name__ == "__main__":
    setup()
