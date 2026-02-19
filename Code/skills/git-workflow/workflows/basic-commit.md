---
type: workflow-diagram
category: git
title: 基础提交流程
description: 从修改文件到推送到远程的完整基础流程
---

# 基础提交流程

```mermaid
flowchart TD
    A[修改文件] --> B{git status}
    B -->|未跟踪/修改| C[git add <file>]
    C --> D[暂存区更新]
    D --> E[git commit -m 'msg']
    E --> F[生成新提交]
    F --> G{推送远程？}
    G -->|是| H[git push origin branch]
    G -->|否| I[保留在本地]
    H --> J[远程仓库更新]
```

## 命令速查

| 步骤 | 命令 | 说明 |
|------|------|------|
| 查看状态 | `git status` | 检查哪些文件被修改 |
| 暂存文件 | `git add <file>` | 将文件加入暂存区 |
| 提交更改 | `git commit -m 'message'` | 创建新提交 |
| 推送到远程 | `git push origin <branch>` | 将提交推送到远程仓库 |

## 使用场景

- 日常开发提交
- 个人项目维护
- 单分支简单协作

## 使用频率：⭐⭐⭐⭐⭐
