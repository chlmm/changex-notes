---
name: lazygit
description: Lazygit - 终端 Git 图形界面工具。简化 Git 操作流程，提供可视化分支管理、提交历史浏览等功能。
execution_mode: user
metadata:
  category: git-tools
  platform: [windows, macos, linux]
---

# Lazygit 使用指南

## 概述

Lazygit 是一个终端下的 Git TUI (Text User Interface) 工具，让你无需记忆复杂命令即可完成大部分 Git 操作。

## 安装

### macOS
```bash
brew install lazygit
```

### Windows
```bash
winget install lazygit
```

### Linux
```bash
[TBD - 待补充]
```

## 基础操作

### 启动

**操作步骤**:
1. 打开终端
2. 进入 Git 仓库目录
3. 运行命令：

```bash
lazygit
```

### 常用快捷键

| 按键 | 功能 |
|------|------|
| `?` | 显示帮助 |
| `q` | 退出 |
| `j/k` | 上下移动 |
| `h/l` | 切换面板 |
| `space` | 暂存/取消暂存文件 |
| `c` | 提交 |
| `P` | 推送 |
| `p` | 拉取 |

## 工作流程图

以下 Mermaid 图展示了 Lazygit 的核心工作流程：

| 流程图 | 说明 | 文件 |
|--------|------|------|
| 核心架构图 | Lazygit 的整体架构层次 | [workflows/core-architecture.md](workflows/core-architecture.md) |
| 基本工作流程 | 启动到退出的完整流程 | [workflows/basic-workflow.md](workflows/basic-workflow.md) |
| 分支管理流程 | 分支的创建、切换、合并、删除 | [workflows/branch-management.md](workflows/branch-management.md) |
| 文件提交流程 | 文件暂存和提交流程 | [workflows/file-commit.md](workflows/file-commit.md) |
| 自定义命令流程 | 高级自定义命令配置 | [workflows/custom-commands.md](workflows/custom-commands.md) |

## 进阶用法

### 交互式变基

**操作步骤**:
[TBD]

### 解决冲突

**操作步骤**:
[TBD]

### 分支管理

**操作步骤**:
[TBD]

## 配置文件

**位置**: `~/.config/lazygit/config.yml`

[TBD - 常用配置项]

## 资源

- **原文件位置**: `工具/softs/index/lazygit.md`
