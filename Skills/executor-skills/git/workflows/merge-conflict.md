---
type: workflow-diagram
category: git
title: 冲突解决流程
description: 处理 git pull 或合并时的代码冲突
---

# 冲突解决流程

```mermaid
flowchart TB
    A[git pull] --> B{冲突？}
    B -->|无冲突| C[自动合并]
    B -->|有冲突| D[标记冲突文件]
    D --> E[手动编辑解决]
    E --> F[git add <resolved-file>]
    F --> G[git commit]
    G --> H[完成合并]
```

## 命令速查

| 步骤 | 命令 | 说明 |
|------|------|------|
| 查看冲突 | `git status` | 显示冲突文件列表 |
| 标记已解决 | `git add <file>` | 将解决后的文件标记为已解决 |
| 完成合并 | `git commit` | 提交合并结果 |
| 中止合并 | `git merge --abort` | 放弃当前合并 |

## 冲突标记格式

```
<<<<<<< HEAD
当前分支的代码
=======
合并分支的代码
>>>>>>> branch-name
```

## 解决技巧

- 不确定时与对方开发者沟通
- 复杂冲突使用 `git mergetool`
- 解决后务必测试
- 偏好 rebase 获取更整洁历史（仅限个人分支）

## 使用场景

- 多人修改同一文件
- 长时间未同步分支
- 合并或变基时

## 使用频率：⭐⭐⭐⭐
