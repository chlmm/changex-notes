#!/usr/bin/env python3
"""
T10: 交互式变基整理历史

场景: feature/api-v2 分支有 5 个 commit，其中有 "WIP" 和 "fix typo" 等不规范的
目标: 用 interactive rebase 整理成 2 个干净的 commit
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-interactive-rebase"


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
    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("# API v1\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'feat: initialize api'", cwd=repo_path)

    # 创建 feature/api-v2 分支
    run("git checkout -b feature/api-v2", cwd=repo_path)

    # 5 个不规范的 commit
    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("# API v2\n\ndef get_items():\n    return []\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'WIP: start api v2'", cwd=repo_path)

    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("# API v2\n\ndef get_items():\n    return []\n\ndef get_item(id):\n    return {}\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'fix typo'", cwd=repo_path)

    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("# API v2\n\ndef get_items():\n    return []\n\ndef get_item(id):\n    return {}\n\ndef create_item(data):\n    return data\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'WIP: add create'", cwd=repo_path)

    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("# API v2\n\ndef get_items():\n    return []\n\ndef get_item(id):\n    if not id:\n        raise ValueError('id required')\n    return {}\n\ndef create_item(data):\n    return data\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'fix: add validation'", cwd=repo_path)

    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("# API v2\n\ndef get_items():\n    return []\n\ndef get_item(id):\n    if not id:\n        raise ValueError('id required')\n    return {}\n\ndef create_item(data):\n    if not data:\n        raise ValueError('data required')\n    return data\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'fix typo in create_item'", cwd=repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T10 目标: 将 5 个不规范的 commit 整理成 2 个干净的 commit")
    print("  git rebase -i HEAD~5")
    print()
    print("  建议整理为:")
    print("    1. feat(api): add v2 read endpoints (get_items, get_item)")
    print("    2. feat(api): add v2 write endpoint (create_item)")
    print()
    print("  操作: 用 squash/fixup 合并相关 commit，reword 修改 message")
    print()
    print("验证: git log 只有 2 个规范 commit，无 'WIP' 或 'fix typo'")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
