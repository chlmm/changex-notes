#!/usr/bin/env python3
"""
T01 & T02: 基础提交流程测试环境

T01 - 遗漏文件的提交:
  场景: 刚提交了一个 commit，但忘记 add 新创建的 utils.py
  目标: 把 utils.py 补进上一个提交（用 git commit --amend）

T02 - 提交信息写错了:
  场景: commit message 写成了 "fix bug"
  目标: 改成规范的 fix(api): handle null response in user service
"""

import os
import subprocess
import tempfile
import shutil

REPO_NAME = "git-test-basic-commit"


def run(cmd, cwd=None):
    subprocess.run(cmd, shell=True, cwd=cwd, check=True,
                   capture_output=True, text=True)


def setup():
    repo_path = os.path.join(tempfile.gettempdir(), REPO_NAME)

    # 清理旧环境
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    os.makedirs(repo_path)
    run("git init", cwd=repo_path)
    run("git config user.email 'test@example.com'", cwd=repo_path)
    run("git config user.name 'Test User'", cwd=repo_path)

    # 创建初始文件并提交
    with open(os.path.join(repo_path, "main.py"), "w") as f:
        f.write("def main():\n    print('hello')\n\nif __name__ == '__main__':\n    main()\n")
    run("git add main.py", cwd=repo_path)
    run("git commit -m 'feat: initialize project'", cwd=repo_path)

    # 修改 main.py 并提交（commit message 故意写错为 "fix bug"）
    with open(os.path.join(repo_path, "main.py"), "w") as f:
        f.write("def main():\n    print('hello')\n\ndef greet(name):\n    return f'Hello, {name}!'\n\nif __name__ == '__main__':\n    main()\n")
    run("git add main.py", cwd=repo_path)
    run("git commit -m 'fix bug'", cwd=repo_path)

    # 创建 utils.py 但忘记 add（用于 T01）
    with open(os.path.join(repo_path, "utils.py"), "w") as f:
        f.write("def helper():\n    return 'utility function'\n\ndef format_response(data):\n    return {'status': 'ok', 'data': data}\n")

    print(f"✅ 测试环境已创建: {repo_path}")
    print()
    print("T01 目标: 把 utils.py 补进上一个 commit（git add utils.py && git commit --amend）")
    print("T02 目标: 把 'fix bug' 改成 'fix(api): handle null response in user service'（git commit --amend -m '...'）")
    print()
    print(f"进入测试: cd {repo_path}")


if __name__ == "__main__":
    setup()
