#!/usr/bin/env python3
"""
T05: 三方合并冲突

场景: main 和 feature/config 都修改了 config.yaml 的同一区域
目标: 手动解决合并冲突，保留双方必要修改
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-merge-conflict"


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

    # 初始提交 - 包含 config.yaml
    with open(os.path.join(repo_path, "config.yaml"), "w") as f:
        f.write("app:\n  name: MyApp\n  port: 8080\n  debug: false\n\ndatabase:\n  host: localhost\n  port: 5432\n")
    run("git add config.yaml", cwd=repo_path)
    run("git commit -m 'feat: add initial config'", cwd=repo_path)

    # 创建 feature/config 分支
    run("git checkout -b feature/config", cwd=repo_path)

    # feature/config 修改 config.yaml
    with open(os.path.join(repo_path, "config.yaml"), "w") as f:
        f.write("app:\n  name: MyApp\n  port: 8080\n  debug: true\n  log_level: DEBUG\n\ndatabase:\n  host: localhost\n  port: 5432\n  pool_size: 10\n")
    run("git add config.yaml", cwd=repo_path)
    run("git commit -m 'feat(config): add debug mode and connection pool'", cwd=repo_path)

    # 回到 main，修改 config.yaml 同一区域（制造冲突）
    run("git checkout main", cwd=repo_path)
    with open(os.path.join(repo_path, "config.yaml"), "w") as f:
        f.write("app:\n  name: MyApp\n  port: 9090\n  debug: false\n  workers: 4\n\ndatabase:\n  host: localhost\n  port: 5432\n  timeout: 30\n")
    run("git add config.yaml", cwd=repo_path)
    run("git commit -m 'feat(config): change port and add workers'", cwd=repo_path)

    # 切回 feature/config，准备合并
    run("git checkout feature/config", cwd=repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T05 目标: 将 main 合并到 feature/config，手动解决 config.yaml 的冲突")
    print("  git merge main")
    print("  # 手动编辑 config.yaml，保留双方必要修改")
    print("  git add config.yaml")
    print("  git commit")
    print()
    print("验证: config.yaml 包含双方的修改（port/9090, debug/true, workers, pool_size, log_level, timeout），无冲突标记")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
