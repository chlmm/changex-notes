#!/usr/bin/env python3
"""
T08 & T09: 恢复丢失的提交/分支

T08 - 恢复已删除的分支:
  场景: 不小心用 git branch -D 删除了未合并的 feature/experimental 分支
  目标: 用 reflog 找回并恢复该分支

T09 - 找回丢失的提交:
  场景: 执行了 git reset --hard HEAD~3，丢失了 3 个 commit
  目标: 用 reflog 恢复所有丢失的 commit
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-lost-commit"


def run(cmd, cwd=None):
    subprocess.run(cmd, shell=True, cwd=cwd, check=True,
                   capture_output=True, text=True)


def setup_t08(repo_path):
    """T08: 删除未合并分支"""
    run("git checkout main", cwd=repo_path)

    # 创建 feature/experimental 分支
    run("git checkout -b feature/experimental", cwd=repo_path)
    with open(os.path.join(repo_path, "experiment.py"), "w") as f:
        f.write("def new_algorithm():\n    # Experimental approach\n    return 'experimental result'\n")
    run("git add experiment.py", cwd=repo_path)
    run("git commit -m 'feat: add experimental algorithm'", cwd=repo_path)

    with open(os.path.join(repo_path, "experiment.py"), "w") as f:
        f.write("def new_algorithm():\n    # Experimental approach v2\n    return 'improved result'\n\ndef benchmark():\n    return 'benchmark data'\n")
    run("git add experiment.py", cwd=repo_path)
    run("git commit -m 'feat: improve experimental algorithm and add benchmark'", cwd=repo_path)

    # 切回 main 并删除分支（未合并！）
    run("git checkout main", cwd=repo_path)
    run("git branch -D feature/experimental", cwd=repo_path)


def setup_t09(repo_path):
    """T09: hard reset 丢失提交"""
    # 在 main 上添加 3 个 commit
    for i in range(1, 4):
        with open(os.path.join(repo_path, f"module{i}.py"), "w") as f:
            f.write(f"# Module {i}\ndef func_{i}():\n    return 'result_{i}'\n")
        run("git add .", cwd=repo_path)
        run(f"git commit -m 'feat: add module {i}'", cwd=repo_path)

    # 执行 hard reset 丢掉这 3 个 commit
    run("git reset --hard HEAD~3", cwd=repo_path)


def setup():
    repo_path = os.path.join(tempfile.gettempdir(), REPO_NAME)

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    os.makedirs(repo_path)
    run("git init", cwd=repo_path)
    run("git config user.email 'test@example.com'", cwd=repo_path)
    run("git config user.name 'Test User'", cwd=repo_path)

    # 初始提交
    with open(os.path.join(repo_path, "main.py"), "w") as f:
        f.write("def main():\n    print('hello')\n")
    run("git add main.py", cwd=repo_path)
    run("git commit -m 'feat: initialize project'", cwd=repo_path)

    # 同时设置 T08 和 T09 的场景
    setup_t08(repo_path)
    setup_t09(repo_path)

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T08 目标: feature/experimental 分支被误删，用 reflog 找回")
    print("  git reflog                        # 找到分支最后的 commit hash")
    print("  git checkout -b feature/experimental <commit-hash>")
    print()
    print("T09 目标: 3 个 module commit 被 reset --hard 丢失，用 reflog 恢复")
    print("  git reflog                        # 找到 reset 之前的 HEAD")
    print("  git reset --hard <commit-hash>    # 恢复到那个状态")
    print()
    print("验证 T08: feature/experimental 分支恢复，有 2 个 commit")
    print("验证 T09: git log 显示 3 个 module commit 都回来了")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
