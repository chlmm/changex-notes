---
name: git-helper
description: This skill should be used when working with Git version control operations, including repository management, committing changes, branch operations, merging, conflict resolution, and Git workflows. Use for tasks like initializing repositories, managing branches, resolving merge conflicts, setting up remotes, or handling complex Git scenarios.
---

# Git Helper Skill

This skill provides specialized knowledge and workflows for Git version control operations, helping users manage repositories, branches, commits, and resolve conflicts efficiently.

## Purpose

Enable efficient Git operations through proven workflows, best practices, and automated assistance for common Git tasks including repository initialization, branch management, conflict resolution, and remote operations.

## When to Use This Skill

Use this skill when users request any Git-related operations:
- Initializing or configuring Git repositories
- Committing changes or managing commit history
- Creating, switching, merging, or deleting branches
- Handling merge conflicts
- Setting up or managing remote repositories
- Reverting changes or rolling back commits
- Checking repository status and history
- Working with Git workflows (Git Flow, GitHub Flow, etc.)

## Core Git Operations

### Repository Setup

**Initialize a new repository:**
```bash
git init
```

**Clone an existing repository:**
```bash
git clone <repository-url>
```

**Configure user information:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**View current configuration:**
```bash
git config --list
```

### Basic Workflow

**Check repository status:**
```bash
git status
```

**Stage changes for commit:**
- Stage specific files: `git add <file>`
- Stage all changes: `git add .`
- Stage with interactive mode: `git add -i`

**Commit staged changes:**
```bash
git commit -m "Descriptive commit message"
```

**Amend the last commit (use with caution):**
```bash
git commit --amend
```

**View commit history:**
```bash
git log
git log --oneline
git log --graph --all --oneline
```

### Branch Management

**List branches:**
```bash
git branch              # Local branches
git branch -r           # Remote branches
git branch -a           # All branches
```

**Create a new branch:**
```bash
git branch <branch-name>
git checkout -b <branch-name>  # Create and switch
```

**Switch branches:**
```bash
git checkout <branch-name>
git switch <branch-name>        # Git 2.23+
```

**Rename current branch:**
```bash
git branch -m <new-name>
```

**Delete a branch:**
```bash
git branch -d <branch-name>     # Only if merged
git branch -D <branch-name>     # Force delete
```

### Merging and Rebase

**Merge a branch into current branch:**
```bash
git merge <branch-name>
```

**Rebase current branch onto another:**
```bash
git rebase <branch-name>
```

**Abort merge/rebase in progress:**
```bash
git merge --abort
git rebase --abort
```

### Remote Operations

**View remote repositories:**
```bash
git remote -v
```

**Add a remote repository:**
```bash
git remote add <name> <url>
```

**Fetch from remote:**
```bash
git fetch <remote-name>
```

**Pull changes (fetch + merge):**
```bash
git pull <remote-name> <branch-name>
```

**Push changes to remote:**
```bash
git push <remote-name> <branch-name>
```

**Push new branch and set upstream:**
```bash
git push -u <remote-name> <branch-name>
```

### Undoing Changes

**Unstage changes:**
```bash
git reset HEAD <file>
```

**Discard local changes in working directory:**
```bash
git checkout -- <file>
git restore <file>  # Git 2.23+
```

**Reset to previous commit:**
```bash
git reset --soft HEAD~1   # Keep changes staged
git reset --mixed HEAD~1  # Keep changes unstaged (default)
git reset --hard HEAD~1   # Discard all changes
```

**Revert a commit (create new commit to undo):**
```bash
git revert <commit-hash>
```

## Conflict Resolution

When conflicts occur during merge or rebase:

1. **Identify conflicting files:**
   ```bash
   git status
   ```

2. **Edit files to resolve conflicts** - Look for conflict markers:
   ```
   <<<<<<< HEAD
   Your changes
   =======
   Incoming changes
   >>>>>>> branch-name
   ```

3. **Stage resolved files:**
   ```bash
   git add <resolved-file>
   ```

4. **Complete the merge/rebase:**
   ```bash
   git commit      # For merge
   git rebase --continue  # For rebase
   ```

5. **Use merge tools for visual resolution:**
   ```bash
   git mergetool
   ```

## Common Git Workflows

### Feature Branch Workflow

1. Create feature branch from main:
   ```bash
   git checkout main
   git pull
   git checkout -b feature/your-feature
   ```

2. Make commits to feature branch

3. Push feature branch:
   ```bash
   git push -u origin feature/your-feature
   ```

4. Create pull request and merge after review

5. Delete feature branch after merge:
   ```bash
   git checkout main
   git branch -d feature/your-feature
   ```

### Hotfix Workflow

1. Create hotfix branch from production:
   ```bash
   git checkout production
   git checkout -b hotfix/urgent-fix
   ```

2. Make and commit the fix

3. Merge hotfix to production and main:
   ```bash
   git checkout production
   git merge hotfix/urgent-fix
   git checkout main
   git merge hotfix/urgent-fix
   ```

## Best Practices

**Commit Messages:**
- Use present tense ("Add feature" not "Added feature")
- Be concise but descriptive
- Limit first line to 50 characters
- Add detailed description in body if needed
- Reference issue numbers when applicable

**Branch Naming:**
- Use descriptive names: `feature/user-authentication`, `fix/login-bug`, `hotfix/security-patch`
- Use consistent naming conventions across the team

**Commit Often:**
- Small, focused commits are easier to review and revert
- Commit logical units of work
- Avoid including unrelated changes in one commit

**Use .gitignore:**
- Exclude build artifacts, dependencies, IDE files, temporary files
- Add project-specific patterns

## Useful Commands Reference

**Compare changes:**
```bash
git diff                  # Unstaged changes
git diff --staged         # Staged changes
git diff <branch1> <branch2>  # Compare branches
```

**Search commit history:**
```bash
git log --grep "search-term"
git log --author "author-name"
git log --since="2024-01-01"
```

**Show file history:**
```bash
git log --follow <file>
git blame <file>
```

**Stash changes temporarily:**
```bash
git stash                # Stash current changes
git stash list           # List stashes
git stash pop            # Apply and remove stash
git stash apply          # Apply stash without removing
```

**Clean untracked files:**
```bash
git clean -f             # Remove untracked files
git clean -fd            # Remove untracked files and directories
```

## Troubleshooting

**HEAD detached:**
```bash
git checkout <branch-name>
```

**Large file blocking push:**
```bash
git rm --cached <large-file>
git commit -m "Remove large file"
```

**Accidentally committed sensitive data:**
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch <sensitive-file>" \
  --prune-empty --tag-name-filter cat -- --all
```

**Lost commits after reset:**
```bash
git reflog               # Find lost commit hash
git reset <commit-hash>  # Restore from reflog
```

When assisting with Git operations, always:
1. Explain what each command does before executing
2. Warn about destructive operations (reset --hard, rebase, etc.)
3. Suggest safer alternatives when possible
4. Encourage backing up important work before major operations
