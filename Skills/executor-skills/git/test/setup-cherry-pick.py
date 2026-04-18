#!/usr/bin/env python3
"""
T06: Cherry-pick 特定提交

场景: feature/new-api 上有一个修复 bug 的 commit，需要只把这个修复应用到 main
目标: 用 cherry-pick 把 bug 修复 commit 单独应用到 main，不带其他功能代码
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-cherry-pick"


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
        f.write("def get_user(user_id):\n    return {'id': user_id, 'name': 'User'}\n\ndef create_user(name):\n    return {'id': 1, 'name': name}\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'feat(api): add user endpoints'", cwd=repo_path)

    # 创建 feature/new-api 分支
    run("git checkout -b feature/new-api", cwd=repo_path)

    # 功能提交 1
    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("def get_user(user_id):\n    return {'id': user_id, 'name': 'User'}\\n\ndef create_user(name):\n    return {'id': 1, 'name': name}\n\ndef update_user(user_id, data):\n    return {'id': user_id, **data}\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'feat(api): add update endpoint'", cwd=repo_path)

    # Bug 修复提交（这是需要 cherry-pick 的）
    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("def get_user(user_id):\n    if not user_id:\n        raise ValueError('user_id is required')\n    return {'id': user_id, 'name': 'User'}\n\ndef create_user(name):\n    return {'id': 1, 'name': name}\n\ndef update_user(user_id, data):\n    return {'id': user_id, **data}\n")
    run("git add api.py", cwd=repo_path)
    bug_fix_msg = "fix(api): validate user_id parameter in get_user"
    run(f"git commit -m '{bug_fix_msg}'", cwd=repo_path)

    # 功能提交 2
    with open(os.path.join(repo_path, "api.py"), "w") as f:
        f.write("def get_user(user_id):\n    if not user_id:\n        raise ValueError('user_id is required')\n    return {'id': user_id, 'name': 'User'}\n\ndef create_user(name):\n    return {'id': 1, 'name': name}\n\ndef update_user(user_id, data):\n    return {'id': user_id, **data}\n\ndef delete_user(user_id):\n    return {'deleted': True, 'id': user_id}\n")
    run("git add api.py", cwd=repo_path)
    run("git commit -m 'feat(api): add delete endpoint'", cwd=repo_path)

    # 回到 main
    run("git checkout main", cwd=repo_path)

    # 打印 bug fix 的 commit hash
    result = subprocess.run(
        f"git log --grep 'validate user_id' --format=%H -1",
        shell=True, cwd=repo_path, capture_output=True, text=True
    )
    # 注意：此时在 main 上，feature/new-api 的提交不在 log 中
    # 用户需要先查看 feature/new-api 的 log

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T06 目标: 只把 bug 修复 commit cherry-pick 到 main，不带功能代码")
    print("  1. git log feature/new-api --oneline  # 找到 bug fix commit 的 hash")
    print("  2. git cherry-pick <commit-hash>")
    print()
    print("验证: main 上只有 cherry-pick 来的 bug 修复（get_user 中有参数校验），没有 update/delete 端点")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
