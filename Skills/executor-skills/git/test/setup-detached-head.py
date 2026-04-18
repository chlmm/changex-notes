#!/usr/bin/env python3
"""
T12: Detached HEAD 状态

场景: git checkout v1.0 进入 detached HEAD，在这里做了修改并 commit 了
目标: 把 detached HEAD 下的 commit 保存到新分支
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-detached-head"


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
        f.write("def app():\n    print('v1.0')\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: initial version'", cwd=repo_path)

    # 打 v1.0 标签
    run("git tag -a v1.0 -m 'Release v1.0'", cwd=repo_path)

    # main 上继续开发
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("def app():\n    print('v2.0-dev')\n\ndef new_feature():\n    pass\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: start v2 development'", cwd=repo_path)

    # 进入 detached HEAD 状态（checkout 到 v1.0 标签）
    run("git checkout v1.0", cwd=repo_path)

    # 在 detached HEAD 下做修改并提交
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("def app():\n    print('v1.0-patched')\n\ndef patch_info():\n    return 'security patch applied'\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'fix: apply security patch to v1.0'", cwd=repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T12 目标: 把 detached HEAD 下的 commit 保存到新分支")
    print("  git checkout -b hotfix/security-patch")
    print()
    print("验证: 新分支 hotfix/security-patch 包含在 detached HEAD 下做的 commit")
    print("  git log --oneline  # 应该看到 security patch 的 commit")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
