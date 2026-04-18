#!/usr/bin/env python3
"""
T13: 版本发布与热修复

场景: 需要在 main 上打 v2.0.0 标签发布，发布后发现严重 bug
目标: 打 v2.0.0 标签，然后从 v2.0.0 创建 hotfix 修复 bug，打 v2.0.1 标签，合并回 main
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-tag-release"


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

    # v1.0.0 历史
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("APP_VERSION = '1.0.0'\n\ndef run():\n    print(f'Running {APP_VERSION}')\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: initial release'", cwd=repo_path)
    run("git tag -a v1.0.0 -m 'Release v1.0.0'", cwd=repo_path)

    # v2.0.0 开发
    with open(os.path.join(repo_path, "app.py"), "w") as f:
        f.write("APP_VERSION = '2.0.0'\n\ndef run():\n    print(f'Running {APP_VERSION}')\n\ndef new_feature():\n    return 'new in v2'\n")
    run("git add app.py", cwd=repo_path)
    run("git commit -m 'feat: v2.0.0 with new feature'", cwd=repo_path)

    with open(os.path.join(repo_path, "config.py"), "w") as f:
        f.write("DEBUG = False\nPORT = 8080\nMAX_CONNECTIONS = 100  # BUG: should be limited\n")
    run("git add config.py", cwd=repo_path)
    run("git commit -m 'feat: add config with connection settings'", cwd=repo_path)

    # 此时还没有打 v2.0.0 标签，需要用户来打

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T13 目标: 完成版本发布和热修复流程")
    print("  1. git tag -a v2.0.0 -m 'Release v2.0.0'    # 打发布标签")
    print("  2. git checkout -b hotfix/v2.0.1 v2.0.0      # 从标签创建热修复分支")
    print("  3. # 修复 config.py 中的 bug（MAX_CONNECTIONS 限制为 10）")
    print("  4. git add config.py && git commit -m 'fix: limit max connections'")
    print("  5. git tag -a v2.0.1 -m 'Release v2.0.1'     # 打修复标签")
    print("  6. git checkout main")
    print("  7. git merge hotfix/v2.0.1                    # 合并回 main")
    print()
    print("验证:")
    print("  - git tag 显示 v1.0.0, v2.0.0, v2.0.1")
    print("  - main 分支包含 hotfix 的修复")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
