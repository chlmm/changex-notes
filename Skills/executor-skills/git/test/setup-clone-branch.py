#!/usr/bin/env python3
"""
T05: 克隆项目并创建分支

场景: 需要从远程克隆一个项目，然后在本地创建 feature 分支并推送到远程
目标: 熟悉 git clone、创建分支、推送分支的完整流程
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-clone-branch"
WORK_NAME = "my-project"  # 用户克隆后的目录名


def run(cmd, cwd=None):
    subprocess.run(cmd, shell=True, cwd=cwd, check=True,
                   capture_output=True, text=True)


def setup():
    base_dir = os.path.join(tempfile.gettempdir(), REPO_NAME)

    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

    os.makedirs(base_dir)

    # 1. 创建远程仓库（bare repo with commits）
    remote_path = os.path.join(base_dir, "origin.git")
    os.makedirs(remote_path)
    run("git init --bare", cwd=remote_path)

    # 2. 在临时目录中创建初始内容并推送到 bare repo
    tmp_repo = os.path.join(base_dir, "tmp-source")
    os.makedirs(tmp_repo)
    run("git init", cwd=tmp_repo)
    run("git config user.email 'test@example.com'", cwd=tmp_repo)
    run("git config user.name 'Test User'", cwd=tmp_repo)

    with open(os.path.join(tmp_repo, "app.py"), "w") as f:
        f.write("class App:\n    def run(self):\n        print('app running')\n")
    with open(os.path.join(tmp_repo, "models.py"), "w") as f:
        f.write("class User:\n    def __init__(self, name):\n        self.name = name\n")
    run("git add .", cwd=tmp_repo)
    run("git commit -m 'feat: initial project'", cwd=tmp_repo)

    run(f"git remote add origin {remote_path}", cwd=tmp_repo)
    run("git branch -M main", cwd=tmp_repo)
    run("git push -u origin main", cwd=tmp_repo)

    # 清理临时目录
    shutil.rmtree(tmp_repo)

    # 用户的工作目录（空，需要 clone）
    work_dir = os.path.join(base_dir, WORK_NAME)

    print(f"✅ 测试环境已创建")
    print(f"   远程仓库: {remote_path}")
    print(f"   工作目录: {base_dir}（请在此目录下执行 clone）")
    print()
    print("T05 目标: 克隆项目、创建 feature 分支、推送到远程")
    print(f"  1. cd {base_dir}")
    print(f"  2. git clone {remote_path} {WORK_NAME}")
    print(f"  3. cd {WORK_NAME}")
    print("  4. git checkout -b feature/user-profile")
    print("  # 做一些修改...")
    print("  5. git add . && git commit -m 'feat: add user profile'")
    print("  6. git push -u origin feature/user-profile")
    print()
    print("验证:")
    print("  git branch -a  # 看到本地和远程的 feature/user-profile")
    print(f"  git ls-remote {remote_path}  # 远程有 feature/user-profile 分支")
    print()
    print(f"进入目录: cd {base_dir}")


if __name__ == "__main__":
    setup()
