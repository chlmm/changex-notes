# Git 实操测试题库

## 说明

每个测试场景配有独立的环境搭建脚本，运行后会生成一个模拟真实项目的 Git 仓库，你需要在其中解决指定问题。

### 使用方式

```bash
# 运行环境搭建脚本（会在 /tmp 下生成测试仓库）
python3 {baseDirectory}/test/<script>.py

# 进入测试仓库
cd /tmp/<test-repo-name>

# 解决问题后验证
git log --oneline --graph --all
```

### 验证标准

- [ ] 仓库状态干净（无未提交修改）
- [ ] 提交历史符合预期
- [ ] 分支结构正确
- [ ] 无冲突残留

---

## 一、基础操作

### T01: 遗漏文件的提交

**难度**: ⭐  
**场景**: 你刚刚提交了一个 commit，但发现忘记 add 一个新创建的文件 `utils.py`，需要把它补进上一个提交中。  
**环境脚本**: [setup-basic-commit.py](setup-basic-commit.py)  
**验证**: 上一个 commit 包含 `utils.py` 的内容，且只有一个 commit（不是两个）。

### T02: 提交信息写错了

**难度**: ⭐  
**场景**: 你提交了一个 commit，但 commit message 写成了 "fix bug"，需要改成规范的 `fix(api): handle null response in user service`。  
**环境脚本**: [setup-basic-commit.py](setup-basic-commit.py)（同 T01）  
**验证**: 最新 commit 的 message 为 `fix(api): handle null response in user service`。

### T03: 日常三步曲提交

**难度**: ⭐  
**场景**: 你修改了 `app.py` 和新建了 `helper.py`，需要完整走一遍 add → commit → push 流程推送到远程。  
**环境脚本**: [setup-daily-commit.py](setup-daily-commit.py)  
**验证**: 远程 main 分支包含最新提交，`git status` 干净，`git log` 显示规范 commit message。

---

## 二、远程仓库操作

### T04: 从零初始化并推送项目

**难度**: ⭐⭐  
**场景**: 你在本地有一个项目目录，还没有用 Git 管理。需要初始化仓库、关联远程、完成首次推送。  
**环境脚本**: [setup-init-push.py](setup-init-push.py)  
**验证**: 远程仓库有 main 分支和初始提交，`git remote -v` 显示正确的远程地址。

### T05: 克隆项目并创建分支

**难度**: ⭐  
**场景**: 你需要从远程克隆一个项目，然后在本地创建 feature 分支并推送到远程。  
**环境脚本**: [setup-clone-branch.py](setup-clone-branch.py)  
**验证**: 本地有克隆的项目，远程存在 `feature/user-profile` 分支。

### T06: 拉取远程更新并合并

**难度**: ⭐⭐  
**场景**: 远程 main 上有同事的新提交，你本地 main 落后了，需要拉取并合并到本地。  
**环境脚本**: [setup-pull-merge.py](setup-pull-merge.py)  
**验证**: 本地 main 与远程同步，`git log` 包含同事的提交。

---

## 三、Bug 修复

### T07: Bug 修复基本流程

**难度**: ⭐  
**场景**: 生产环境发现 bug，从 `master` 拉出 `bugFix` 分支修复。修复期间没有人并行开发，修完直接合并回来，自动 fast-forward。  
**环境脚本**: [setup-bugfix-merge.py](setup-bugfix-merge.py)  
**验证**: `bugFix` 的修复 commit 出现在 `master` 上，历史线性，合并后可安全删除 `bugFix` 分支。

### T08: Bug 修复 rebase 流程

**难度**: ⭐⭐  
**场景**: 生产环境发现 bug，从 `master` 拉出 `bugFix` 分支修复。修复期间 `master` 有新提交，需要用 rebase 将修复基于最新代码验证，确保修复仍然有效。  
**环境脚本**: [setup-bugfix-rebase.py](setup-bugfix-rebase.py)  
**验证**: `bugFix` 线性排列在 `master` 最新提交之后，修复代码在最新代码上仍然有效，合并到 `master` 为 fast-forward。

### T09: 分支变基冲突

**难度**: ⭐⭐⭐  
**场景**: 你在 `feature/dashboard` 上开发了 3 个 commit，同时 `main` 上也有新提交，需要用 rebase 同步并解决冲突。  
**环境脚本**: [setup-rebase-conflict.py](setup-rebase-conflict.py)  
**验证**: `feature/dashboard` 的 3 个 commit 线性排列在 `main` 最新提交之后，历史整洁无 merge commit。

---

## 四、合并与冲突

### T10: 三方合并冲突

**难度**: ⭐⭐⭐  
**场景**: `main` 和 `feature/config` 都修改了 `config.yaml` 的同一区域，合并时产生冲突，需要手动解决。  
**环境脚本**: [setup-merge-conflict.py](setup-merge-conflict.py)  
**验证**: 合并完成，`config.yaml` 包含双方的必要修改，无冲突标记残留。

### T11: Cherry-pick 特定提交

**难度**: ⭐⭐  
**场景**: `feature/new-api` 上有一个修复 bug 的 commit，你需要只把这个修复应用到 `main`，不要其他功能代码。  
**环境脚本**: [setup-cherry-pick.py](setup-cherry-pick.py)  
**验证**: `main` 上只有一个新增的 cherry-pick commit，内容仅包含 bug 修复。

### T12: 合并后清理分支

**难度**: ⭐⭐  
**场景**: `feature/login` 已合并到 `main`，但本地和远程都还有这个分支，需要清理。  
**环境脚本**: [setup-branch-management.py](setup-branch-management.py)  
**验证**: `feature/login` 分支在本地和远程均已删除。

---

## 五、撤销与恢复

### T13: 撤销未推送的提交

**难度**: ⭐⭐  
**场景**: 你在本地提交了 2 个 commit 但还没 push，发现第二个 commit 有问题，需要撤销它但保留第一个。  
**环境脚本**: [setup-undo-commit.py](setup-undo-commit.py)  
**验证**: 只剩下第一个 commit，第二个 commit 的修改回到工作区或被丢弃。

### T14: 用 revert 回退已推送的提交

**难度**: ⭐⭐⭐  
**场景**: 你发现昨天推送的一个 commit 有 bug，但已经有人基于它开发了，不能用 reset，需要用 revert 安全回退。  
**环境脚本**: [setup-revert-pushed.py](setup-revert-pushed.py)  
**验证**: 产生一个新的 revert commit 撤销了 bug 引入的修改，原 commit 仍在历史中。

### T15: 恢复已删除的分支

**难度**: ⭐⭐⭐  
**场景**: 你不小心用 `git branch -D` 删除了一个还未合并的分支 `feature/experimental`，需要找回来。  
**环境脚本**: [setup-lost-commit.py](setup-lost-commit.py)  
**验证**: `feature/experimental` 分支恢复，commit 历史完整。

### T16: 找回丢失的提交

**难度**: ⭐⭐⭐⭐  
**场景**: 你执行了 `git reset --hard HEAD~3`，丢失了 3 个 commit，现在需要恢复它们。  
**环境脚本**: [setup-lost-commit.py](setup-lost-commit.py)（同 T15）  
**验证**: 3 个丢失的 commit 全部恢复。

---

## 六、进阶操作

### T17: 交互式变基整理历史

**难度**: ⭐⭐⭐⭐  
**场景**: 你的 `feature/api-v2` 分支有 5 个 commit，其中有些是 "WIP" 或 "fix typo"，需要用 interactive rebase 整理成 2 个干净的 commit。  
**环境脚本**: [setup-interactive-rebase.py](setup-interactive-rebase.py)  
**验证**: 分支只有 2 个 commit，message 规范，无 "WIP" 或 "fix typo"。

### T18: Stash 切换分支

**难度**: ⭐⭐  
**场景**: 你在 `main` 上改了一半代码，突然需要切换到 `hotfix/urgent` 修一个紧急 bug。改完 bug 后切回 `main` 继续开发。  
**环境脚本**: [setup-stash-workflow.py](setup-stash-workflow.py)  
**验证**: `hotfix/urgent` 上有 bug 修复 commit；`main` 上恢复了之前未完成的工作。

### T19: Detached HEAD 状态

**难度**: ⭐⭐⭐  
**场景**: 你 `git checkout v1.0` 进入了 detached HEAD 状态，在这里做了修改并 commit 了，需要保存这些修改到新分支。  
**环境脚本**: [setup-detached-head.py](setup-detached-head.py)  
**验证**: 新分支包含在 detached HEAD 状态下做的 commit。

---

## 七、版本与发布

### T20: 版本发布与热修复

**难度**: ⭐⭐⭐  
**场景**: 项目需要在当前 `main` 打 `v2.0.0` 标签并发布。发布后发现严重 bug，需要从 `v2.0.0` 创建 `hotfix/v2.0.1` 修复后打新标签。  
**环境脚本**: [setup-tag-release.py](setup-tag-release.py)  
**验证**: 存在 `v2.0.0` 和 `v2.0.1` 两个标签，`hotfix/v2.0.1` 的修复已合并回 `main`。

### T21: 清理误提交的大文件

**难度**: ⭐⭐⭐⭐  
**场景**: 你不小心把一个 50MB 的日志文件 `app.log` 提交到了仓库，即使删除了文件，仓库体积依然很大。需要彻底从历史中移除。  
**环境脚本**: [setup-large-file-cleanup.py](setup-large-file-cleanup.py)  
**验证**: `app.log` 在所有 commit 的历史中都不存在，`git log --all -- app.log` 无输出。

---

## 题目与笔记场景覆盖

| 笔记场景 | 覆盖题目 |
|----------|----------|
| 1. 提交代码到 git 平台 | T01, T02, T03 |
| 2. 合并前拉取远程分支 | T06 |
| 3. 新分支的创建和推送 | T05 |
| 4. 删除分支 | T12 |
| 5. 拉取项目 | T05 |
| 6. 上传代码到远程仓库 | T04 |
| 7. 修改文件后提交 | T03 |
| 8. 新建并切换分支 | T05, T07 |
| 9. 合并其他分支代码 | T06, T10 |
| 10. 拉取并合并远程分支 | T06 |
| 11. 将合并代码拉取到本地 | T06 |
| 12. 提交代码到 master 分支 | T06, T12 |
| 13. 删除无用分支 | T12 |
| 14. 回调到上个版本 | T13, T14 |
| 15. Bug 修复基本流程（无并行） | T07 |
| 16. Bug 修复 rebase 流程（有并行） | T08 |

---

## 难度统计

| 难度 | 题数 | 编号 |
|------|------|------|
| ⭐ | 4 | T01, T02, T03, T07 |
| ⭐⭐ | 7 | T04, T06, T08, T11, T12, T13, T18 |
| ⭐⭐⭐ | 7 | T05, T09, T10, T14, T15, T19, T20 |
| ⭐⭐⭐⭐ | 4 | T16, T17, T21 |
