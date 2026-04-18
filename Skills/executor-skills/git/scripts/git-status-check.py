#!/usr/bin/env python3
"""
Git Repository Status Checker
Provides a comprehensive overview of Git repository state
"""

import subprocess
import sys
from pathlib import Path
from typing import Dict, List


def run_git_command(args: List[str], repo_path: str = ".") -> str:
    """Run a git command and return the output."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if e.returncode == 128:
            return ""
        return f"Error: {e.stderr.strip()}"


def get_git_status(repo_path: str = ".") -> Dict:
    """Get comprehensive git status information."""
    status = {
        "is_git_repo": False,
        "current_branch": "",
        "untracked_files": [],
        "modified_files": [],
        "staged_files": [],
        "ahead_commits": 0,
        "behind_commits": 0,
        "remote_status": "",
        "has_conflicts": False
    }

    branch_info = run_git_command(["rev-parse", "--abbrev-ref", "HEAD"], repo_path)
    if not branch_info or "fatal" in branch_info:
        return status

    status["is_git_repo"] = True
    status["current_branch"] = branch_info

    status_output = run_git_command(["status", "--porcelain"], repo_path)
    for line in status_output.split("\n"):
        if not line:
            continue

        status_char = line[0]
        filename = line[3:]

        if status_char == "??" or status_char == "?":
            status["untracked_files"].append(filename)
        elif status_char == "M":
            status["modified_files"].append(filename)
        elif status_char in ["A", "M "]:
            status["staged_files"].append(filename)

    status["has_conflicts"] = "U" in status_output or any(
        line.startswith("AA") or line.startswith("UU")
        for line in status_output.split("\n")
    )

    try:
        rev_count = run_git_command(
            ["rev-list", "--count", "--left-right", f"HEAD...@{{u}}"], repo_path
        )
        if rev_count and "\t" in rev_count:
            behind, ahead = rev_count.split("\t")
            status["behind_commits"] = int(behind)
            status["ahead_commits"] = int(ahead)
    except Exception:
        pass

    return status


def print_status(status: Dict):
    """Print formatted git status."""
    if not status["is_git_repo"]:
        print("Not a Git repository")
        return

    print(f"\nGit Repository Status")
    print(f"{'='*50}")

    print(f"\nBranch: {status['current_branch']}")

    remote_info = []
    if status["ahead_commits"] > 0:
        remote_info.append(f"{status['ahead_commits']} ahead")
    if status["behind_commits"] > 0:
        remote_info.append(f"{status['behind_commits']} behind")
    print(f"   Remote: {' '.join(remote_info) if remote_info else 'Up to date'}")

    if status["has_conflicts"]:
        print(f"\nCONFLICTS DETECTED - Resolve before committing")

    if status["staged_files"]:
        print(f"\nStaged files ({len(status['staged_files'])}):")
        for f in status["staged_files"][:10]:
            print(f"   + {f}")
        if len(status["staged_files"]) > 10:
            print(f"   ... and {len(status['staged_files']) - 10} more")

    if status["modified_files"]:
        print(f"\nModified files ({len(status['modified_files'])}):")
        for f in status["modified_files"][:10]:
            print(f"   ~ {f}")
        if len(status["modified_files"]) > 10:
            print(f"   ... and {len(status['modified_files']) - 10} more")

    if status["untracked_files"]:
        print(f"\nUntracked files ({len(status['untracked_files'])}):")
        for f in status["untracked_files"][:10]:
            print(f"   ? {f}")
        if len(status["untracked_files"]) > 10:
            print(f"   ... and {len(status['untracked_files']) - 10} more")

    if not any([status["staged_files"], status["modified_files"], status["untracked_files"]]):
        print(f"\nWorking directory clean")

    print(f"\n{'='*50}\n")


def main():
    """Main entry point."""
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    status = get_git_status(repo_path)
    print_status(status)

    if status["has_conflicts"] or status["modified_files"]:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
