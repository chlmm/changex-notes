#!/usr/bin/env python3
"""
T11: Stash 切换分支

场景: 在 main 上改了一半代码，突然需要切到 hotfix/urgent 修紧急 bug
目标: 用 stash 保存当前工作，切到 hotfix 修 bug，修完后切回 main 恢复工作
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-stash-workflow"


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
        f.write("def app():\n    print('running')\n")
    with open(os.path.join(repo_path, "auth.py"), "w") as f:
        f.write("def authenticate(token):\n    return token == 'valid'\n")
    run("git add .", cwd=repo_path)
    run("git commit -m 'feat: initialize app'", cwd=repo_path)

    # 创建 hotfix/urgent 分支（从当前 main 创建，但还未做修复）
    run("git checkout -b hotfix/urgent", cwd=repo_path)
    run("git checkout main", cwd=repo_path)

    # 在 main 上做了一半的开发（未暂存）
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("def app():\n    print('running')\n\ndef new_feature():\n    # TODO: still working on this\n    pass\n")
    # 注意：不 add，保持在工作区

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T11 目标: 保存当前工作 → 切到 hotfix 修 bug → 切回 main 恢复工作")
    print("  1. git stash save 'WIP: new feature'")
    print("  2. git checkout hotfix/urgent")
    print("  3. # 修复 auth.py 中的 bug")
    print("  4. git add auth.py && git commit -m 'fix(auth): fix authentication bypass'")
    print("  5. git checkout main")
    print("  6. git stash pop")
    print()
    print("验证:")
    print("  - hotfix/urgent 上有 bug 修复 commit")
    print("  - main 上恢复了 new_feature() 的未完成代码")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
