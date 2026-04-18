#!/usr/bin/env python3
"""
T04: 分支变基冲突

场景: feature/dashboard 上有 3 个 commit，同时 main 上也有新提交
目标: 用 rebase 同步 main 的更新并解决冲突，保持线性历史
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-rebase-conflict"


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

    # 初始提交 - 包含 config.py
    with open(os.path.join(repo_path, "config.py"), "w") as f:
        f.write("APP_NAME = 'MyApp'\nVERSION = '1.0'\nDEBUG = False\n")
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("from config import APP_NAME\n\ndef main():\n    print(f'{APP_NAME} running')\n")
    run("git add .", cwd=repo_path)
    run("git commit -m 'feat: initialize project'", cwd=repo_path)

    # 创建 feature/dashboard 分支
    run("git checkout -b feature/dashboard", cwd=repo_path)

    # feature/dashboard 的 3 个 commit（修改 config.py 和新增文件）
    with open(os.path.join(repo_path, "config.py"), "w") as f:
        f.write("APP_NAME = 'MyApp'\nVERSION = '1.0'\nDEBUG = False\nDASHBOARD_ENABLED = True\n")
    run("git add config.py", cwd=repo_path)
    run("git commit -m 'feat(dashboard): enable dashboard in config'", cwd=repo_path)

    with open(os.path.join(repo_path, "dashboard.py"), "w") as f:
        f.write("def show_dashboard():\n    return 'Dashboard View'\n")
    run("git add dashboard.py", cwd=repo_path)
    run("git commit -m 'feat(dashboard): add dashboard page'", cwd=repo_path)

    with open(os.path.join(repo_path, "dashboard.py"), "w") as f:
        f.write("from config import DASHBOARD_ENABLED\n\ndef show_dashboard():\n    if not DASHBOARD_ENABLED:\n        return 'Disabled'\n    return 'Dashboard View'\n")
    run("git add dashboard.py", cwd=repo_path)
    run("git commit -m 'feat(dashboard): add enabled check'", cwd=repo_path)

    # 回到 main，添加新提交（修改 config.py 同一区域，制造冲突）
    run("git checkout main", cwd=repo_path)
    with open(os.path.join(repo_path, "config.py"), "w") as f:
        f.write("APP_NAME = 'MyApp'\nVERSION = '1.1'\nDEBUG = False\nLOG_LEVEL = 'INFO'\n")
    run("git add config.py", cwd=repo_path)
    run("git commit -m 'feat: bump version and add log level'", cwd=repo_path)

    # 切回 feature/dashboard，准备 rebase
    run("git checkout feature/dashboard", cwd=repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T04 目标: 将 feature/dashboard rebase 到 main 最新提交上，解决冲突")
    print("  git fetch origin  # (本环境无远程，直接 rebase)")
    print("  git rebase main")
    print("  # 解决冲突后: git add <file> && git rebase --continue")
    print()
    print("验证: feature/dashboard 的 3 个 commit 线性排列在 main 最新提交之后，无 merge commit")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
