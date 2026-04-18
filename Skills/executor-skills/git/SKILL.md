---
name: git
description: Git 版本控制全流程指南。涵盖日常操作、分支策略、协作规范、冲突解决、撤销恢复等完整工作流。当用户进行 git 操作、提交代码、管理分支、处理冲突、版本发布时使用此技能。
type: tool
execution_mode: executor
metadata:
  category: version-control
  platform: [windows, macos, linux]
  tags: [git, vcs, branch, commit, merge, rebase]
---

# Git 全流程指南

## 概述

整合 Git 操作命令、工作流规范和最佳实践，覆盖从日常提交到灾难恢复的完整场景。按照「基础操作 → 协作流程 → 应急处理」三层结构组织。

## 何时使用

- 提交代码、编写 commit message
- 创建/切换/合并/删除分支
- 处理合并冲突
- 撤销修改、回退提交
- 版本发布与标签管理
- 子模块管理
- 误操作数据恢复

## 工作流全景图

| 工作流 | 说明 | 频率 | 文件 |
|--------|------|------|------|
| **基础提交** | 从修改到推送的基础流程 | ⭐⭐⭐⭐⭐ | [workflows/basic-commit.md](workflows/basic-commit.md) |
| **分支协作** | 特性分支团队协作 | ⭐⭐⭐⭐⭐ | [workflows/branch-collaboration.md](workflows/branch-collaboration.md) |
| **代码审查** | 现代团队代码审查流程 | ⭐⭐⭐⭐⭐ | [workflows/code-review.md](workflows/code-review.md) |
| **冲突解决** | 处理合并/变基时的代码冲突 | ⭐⭐⭐⭐ | [workflows/merge-conflict.md](workflows/merge-conflict.md) |
| **撤销操作** | 不同阶段的代码撤销和回退 | ⭐⭐⭐⭐ | [workflows/undo-operations.md](workflows/undo-operations.md) |
| **版本发布** | 版本发布和热修复 | ⭐⭐⭐⭐ | [workflows/release-tagging.md](workflows/release-tagging.md) |
| **变基协作** | 使用 rebase 保持历史整洁 | ⭐⭐⭐ | [workflows/rebase-workflow.md](workflows/rebase-workflow.md) |
| **子模块** | 子模块管理 | ⭐⭐ | [workflows/submodule.md](workflows/submodule.md) |
| **灾难恢复** | 误操作数据恢复 | ⭐ | [workflows/disaster-recovery.md](workflows/disaster-recovery.md) |

---

## 一、基础操作

### 仓库初始化

```bash
git init                                    # 初始化新仓库
git clone <url>                             # 克隆远程仓库
git config --global user.name "Your Name"   # 配置用户名
git config --global user.email "you@example.com"  # 配置邮箱
```

### 日常三步曲

```bash
git status              # 1. 查看状态
git add <file>          # 2. 暂存文件（git add . 全部暂存）
git commit -m "msg"     # 3. 提交
```

### 提交信息规范

遵循 Conventional Commits 格式：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**类型：**

| 类型 | 说明 |
|------|------|
| `feat` | 新功能 |
| `fix` | Bug 修复 |
| `docs` | 文档变更 |
| `style` | 格式调整（不影响逻辑） |
| `refactor` | 重构（非新功能、非修复） |
| `perf` | 性能优化 |
| `test` | 测试相关 |
| `chore` | 构建/工具/依赖 |
| `ci` | CI/CD 变更 |

**示例：**
```
feat(auth): add JWT token refresh mechanism

Implement automatic token refresh before expiration.
Tokens are refreshed 5 minutes before expiry.

Closes #123
```

**规则：**
1. 使用祈使语气（"Add feature" 而非 "Added feature"）
2. 首行不超过 50 字符
3. 首字母大写，末尾不加句号
4. Body 每行不超过 72 字符
5. Body 解释 what 和 why，而非 how

### 查看与检查

```bash
git log --oneline --graph     # 可视化提交历史
git diff                      # 未暂存的修改
git diff --staged             # 已暂存的修改
git show <commit>             # 查看提交详情
git blame <file>              # 逐行查看修改者
```

---

## 二、分支管理

### 分支操作

```bash
git branch                    # 列出本地分支
git branch -r                 # 列出远程分支
git branch -a                 # 列出所有分支
git checkout -b <name>        # 创建并切换分支
git switch <name>             # 切换分支（Git 2.23+）
git branch -m <new-name>      # 重命名当前分支
git branch -d <name>          # 删除已合并分支
git branch -D <name>          # 强制删除分支
```

### 分支命名规范

| 前缀 | 用途 | 示例 |
|------|------|------|
| `feature/` | 新功能 | `feature/user-auth` |
| `fix/` | Bug 修复 | `fix/login-error` |
| `hotfix/` | 紧急修复 | `hotfix/security-patch` |
| `release/` | 发布准备 | `release/1.2.0` |
| `docs/` | 文档更新 | `docs/api-guide` |

### 分支策略选择

| 策略 | 复杂度 | 适用场景 |
|------|--------|----------|
| **GitHub Flow** | 低 | 小团队、持续部署 |
| **Git Flow** | 高 | 定期发布、多版本维护 |
| **Trunk-Based** | 极低 | 高 CI/CD 成熟度、快速迭代 |

#### GitHub Flow（推荐简化流程）

```bash
git checkout main
git pull
git checkout -b feature/your-feature
# 开发...
git push -u origin feature/your-feature
# 创建 PR → Review → 合并
git checkout main && git pull
git branch -d feature/your-feature
```

#### Git Flow（完整发布流程）

```bash
# 功能开发
git checkout develop && git checkout -b feature/name
# 开发完成
git checkout develop && git merge feature/name

# 发布
git checkout -b release/1.2.0
# 测试完成后
git checkout main && git merge release/1.2.0
git tag -a v1.2.0 -m "Release 1.2.0"
git checkout develop && git merge release/1.2.0
```

---

## 三、合并与变基

### Merge vs Rebase

| 场景 | 推荐方式 | 原因 |
|------|----------|------|
| 合并 PR | merge | 保留完整历史 |
| 同步上游更新（个人分支） | rebase | 线性历史 |
| 同步上游更新（共享分支） | merge | 安全、不重写历史 |

```bash
# Merge
git merge <branch>

# Rebase
git fetch origin
git rebase origin/main
# 冲突后
git add <resolved-file>
git rebase --continue
# 放弃变基
git rebase --abort
```

> **注意：** 不要在共享分支上使用 rebase！已 rebase 的分支推送需要 `git push -f`，仅在个人特性分支使用。

---

## 四、冲突解决

```bash
git status                    # 1. 查看冲突文件
# 2. 手动编辑解决冲突
git add <resolved-file>       # 3. 标记已解决
git commit                    # 4. 完成合并
# 或放弃合并
git merge --abort
```

冲突标记格式：
```
<<<<<<< HEAD
当前分支的代码
=======
合并分支的代码
>>>>>>> branch-name
```

**解决技巧：**
- 不确定时与对方开发者沟通
- 复杂冲突使用 `git mergetool`
- 解决后务必测试

---

## 五、撤销与恢复

| 场景 | 命令 | 效果 |
|------|------|------|
| 未暂存的修改 | `git restore <file>` | 丢弃工作区修改 |
| 已暂存未提交 | `git reset HEAD <file>` | 撤出暂存区，保留修改 |
| 撤销最近提交（保留修改） | `git reset --soft HEAD~1` | 撤销提交，修改保留在暂存区 |
| 撤销最近提交（丢弃修改） | `git reset --hard HEAD~1` | 彻底删除提交和修改 |
| 已推送的提交 | `git revert <commit-id>` | 创建反向提交，保留历史 |

> **警告：** `--hard` 会永久删除修改！已 push 的提交尽量用 `revert`。

### Stash 临时保存

```bash
git stash save "WIP: feature description"   # 保存
git stash list                               # 列表
git stash pop                                # 应用并删除
git stash apply stash@{0}                    # 应用不删除
```

---

## 六、远程操作

```bash
git remote -v                              # 查看远程
git remote add <name> <url>                # 添加远程
git fetch <remote>                         # 获取（不合并）
git pull <remote> <branch>                 # 获取并合并
git push <remote> <branch>                 # 推送
git push -u <remote> <branch>              # 首次推送并关联
```

---

## 七、版本发布与标签

```bash
git tag -a v1.0.0 -m "Release 1.0.0"       # 创建标签
git push origin v1.0.0                      # 推送标签
git push origin --tags                      # 推送所有标签
git checkout v1.0.0                         # 检出标签
git checkout -b hotfix v1.0.0               # 基于标签创建分支
```

**语义化版本：** `v主版本.次版本.补丁`（如 v1.2.3）

---

## 八、子模块

```bash
git submodule add <repo-url>                # 添加子模块
git submodule init                          # 初始化
git submodule update                        # 更新
git clone --recurse-submodules <url>        # 递归克隆
git submodule update --remote               # 拉取子模块最新
```

---

## 九、灾难恢复

```bash
git reflog                                  # 查看所有操作历史
git reflog show main                        # 特定分支 reflog
git reset --hard HEAD@{2}                   # 恢复到指定时间点
git fsck --lost-found                       # 查找悬空对象
```

> **重要：** reflog 默认只保留 90 天。定期 push 是最有效的备份。

---

## 十、PR 最佳实践

### PR 描述模板

```markdown
## Summary
简要描述变更

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing Done
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Related Issues
Closes #123
```

### Review Checklist

1. 代码遵循项目规范
2. 测试覆盖新功能
3. 文档已更新
4. 无敏感数据
5. CI/CD 通过
6. 性能影响已评估

---

## 命令速查

### 日常命令

```bash
git status                    # 查看状态
git add <file>               # 暂存文件
git commit -m "message"      # 提交
git push origin <branch>     # 推送
git pull origin <branch>     # 拉取
git checkout -b <branch>     # 创建并切换分支
git merge <branch>           # 合并分支
```

### 清理命令

```bash
git branch -d <branch>       # 删除本地分支
git push origin :<branch>    # 删除远程分支
git clean -fd                # 删除未跟踪文件
git gc                       # 垃圾回收
```

### 搜索历史

```bash
git log --grep "search-term"           # 搜索提交信息
git log --author "author-name"         # 按作者搜索
git log --since="2024-01-01"           # 按日期搜索
git log --follow <file>                # 文件历史（含重命名）
```

---

## 参考文档

- **提交信息模板**: [references/commit-message-template.md](references/commit-message-template.md)
- **分支策略详解**: [references/branching-models.md](references/branching-models.md)
- **.gitignore 模板**: [references/gitignore-template.md](references/gitignore-template.md)

## 工具脚本

- **仓库状态检查**: `{baseDirectory}/scripts/git-status-check.py <repo-path>`

## 资源

- [Pro Git 中文版](https://git-scm.com/book/zh/v2)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Git Flow 原文](https://nvie.com/posts/a-successful-git-branching-model/)
