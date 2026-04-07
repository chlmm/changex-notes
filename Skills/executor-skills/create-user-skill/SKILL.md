---
name: create-user-skill
description: 创建 user-skill 的指南和模板。当需要为用户操作类工具（无法通过 AI 直接操作）创建使用指南时使用此 skill。
type: meta
execution_mode: executor
metadata:
  category: meta-skill
  author: user
  version: "1.0.0"
---

# 创建 User-Skill 指南

## 概述

User-skill 是面向用户的操作指南，用于那些**只能由用户手动操作**的工具（如 GUI 软件、浏览器扩展、需要人工判断的操作等）。

与 AI skill（`skills/`）的区别：

| 对比项 | AI Skill | User-Skill |
|--------|----------|------------|
| 执行者 | AI 直接执行 | 用户按指南操作 |
| 文件位置 | `skills/` | `user-skills/` |
| 文件名 | `SKILL.md` | `USER-SKILL.md` |
| 适用场景 | 命令行、API、可自动化操作 | GUI 工具、浏览器扩展、需人工判断 |
| 未来 MCP 迁移 | 直接可用 | 需重写为 AI skill |

## 何时创建 User-Skill

创建 user-skill 当工具满足以下条件：

- **GUI 应用**：Obsidian、VSCode、Figma、Photoshop 等
- **浏览器扩展**：需要用户点击、配置
- **需要人工判断**：设计决策、内容审核等
- **暂无可用的 MCP 工具**：未来可能有，但目前没有

## 文件结构

```
user-skills/
├── <category>/
│   └── <skill-name>/
│       ├── USER-SKILL.md      # 主文档（必需）
│       ├── examples/          # 使用示例（可选）
│       │   ├── example-1.md
│       │   └── example-2.md
│       └── workflows/         # 流程图（可选）
│           ├── workflow-1.md
│           └── workflow-2.md
```

## 创建步骤

### Step 1: 确定分类

根据工具类型选择分类：

| 分类 | 说明 | 示例 |
|------|------|------|
| `obsidian/` | Obsidian 插件 | dataview-queries |
| `vscode/` | VSCode 扩展 | compare-folders |
| `software/` | 桌面软件 | lazygit, zerotier |
| `browser/` | 浏览器扩展/工具 | omni |
| `ai-tools/` | AI 相关工具 | claude-task-master |
| `network-tools/` | 网络工具 | easytier, zerotier |
| `productivity/` | 效率工具 | keyviz, faved |
| `development-tools/` | 开发工具 | diff2html, project-graph |
| `entertainment/` | 娱乐工具 | watcharr |
| `text-analysis/` | 文本分析 | novel-analyst |

### Step 2: 创建文件夹

```bash
mkdir -p "user-skills/<category>/<skill-name>"
```

### Step 3: 创建 USER-SKILL.md

使用以下模板：

```yaml
---
name: <skill-name>
description: <一句话描述工具用途和使用场景>
execution_mode: user
metadata:
  category: <分类>
  platform: [windows, macos, linux, web, chrome, etc.]
  homepage: <官网链接>
  github: <GitHub 链接>
  tags: [标签1, 标签2]
---

# <工具名称> 使用指南

## 概述

<工具简介，2-3 句话说明是什么、能做什么>

## 功能特性

- <核心功能 1>
- <核心功能 2>
- <核心功能 3>

## 安装

### 方式一：<安装方式>

**操作步骤**:
1. <步骤 1>
2. <步骤 2>
3. <步骤 3>

### 方式二：<安装方式>

**操作步骤**:
[TBD - 待补充]

## 基础使用

### <功能名称>

**操作步骤**:
1. <步骤 1>
2. <步骤 2>
3. <步骤 3>

**预期效果**: <描述操作后的结果>

## 进阶用法（可选）

### <高级功能>

**操作步骤**:
[TBD - 待补充]

## 配置选项（可选）

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| <选项名> | <说明> | <默认值> |

## 常见问题（可选）

**Q: <问题>**
A: <答案>

## 使用场景（可选）

- <场景 1>
- <场景 2>

## 资源

- **官网**: <链接>
- **GitHub**: <链接>
- **原文件位置**: `<原文件路径>`

---

## 示例 User-Skill

### 示例 1: 简单软件（keyviz）

```yaml
---
name: keyviz
description: Keyviz - 按键可视化工具。在屏幕上实时显示按键操作，适合录屏演示和教学场景。
execution_mode: user
metadata:
  category: productivity
  platform: [windows, macos, linux]
  github: https://github.com/mulaRahul/keyviz
  tags: [按键可视化, 录屏工具, 演示]
---

# Keyviz 使用指南

## 概述

Keyviz 是一个实时按键可视化工具...（简洁明了）
```

### 示例 2: 带 examples 的软件（diff2html）

```yaml
---
name: diff2html
description: diff2html - Git diff 可视化工具...
execution_mode: user
metadata:
  category: development-tools
---

# diff2html 使用指南

## 概述
...

## 基础使用

### 快速开始

具体示例请参考：[examples/basic-usage.md](examples/basic-usage.md)

## 常用命令
...
```

然后在 `examples/basic-usage.md` 中详细展示命令流程。

### 示例 3: 带 workflows 的软件（lazygit）

```yaml
---
name: lazygit
description: Lazygit - 终端 Git 图形界面工具...
execution_mode: user
---

# Lazygit 使用指南

## 工作流程图

| 流程图 | 说明 | 文件 |
|--------|------|------|
| 核心架构图 | 整体架构层次 | [workflows/core-architecture.md](workflows/core-architecture.md) |
| 基本工作流程 | 启动到退出流程 | [workflows/basic-workflow.md](workflows/basic-workflow.md) |
```

---

## 内容组织建议

### 何时创建 examples/

- 有具体的命令示例（如 diff2html）
- 有多个使用场景（如 Dataview 的各种查询）
- 需要展示具体配置

### 何时创建 workflows/

- 有复杂的操作流程（如 lazygit 的分支管理）
- 有架构图或流程图（mermaid）
- 需要可视化展示操作步骤

### 保持简洁

- **基础信息** → USER-SKILL.md
- **具体示例** → examples/
- **流程图表** → workflows/

---

## 迁移为 AI Skill（未来）

当工具有 MCP 支持时，迁移步骤：

1. 复制 `user-skills/<skill>/` 到 `skills/<skill>/`
2. 重命名 `USER-SKILL.md` → `SKILL.md`
3. 修改 `execution_mode: user` → `execution_mode: ai`
4. 将用户操作步骤改为 AI 可直接执行的命令/工具调用
5. 删除不必要的 examples/（如果 AI 可直接执行）

---

## 注意事项

1. **保持占位符标记** - 不确定的内容用 `[TBD - 待补充]` 标记
2. **保留原文件引用** - 在资源部分注明原文件位置
3. **添加 GitHub/官网链接** - 方便用户获取最新信息
4. **使用表格展示快捷键/配置** - 更易读
5. **为未来 MCP 预留** - 考虑哪些步骤未来可能自动化
