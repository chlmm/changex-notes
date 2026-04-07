---
name: diff2html
description: diff2html - Git diff 可视化工具。将 diff 文件转换为美观的 HTML 页面。
type: tool
execution_mode: advisor
metadata:
  category: development-tools
  platform: [windows, macos, linux]
  tags: [git, diff, 可视化, 代码对比]
---

# diff2html 使用指南

## 概述

diff2html 是一个将 Git diff 文件转换为美观 HTML 页面的工具，方便查看代码变更和进行代码审查。

## 功能特性

- 将 diff 文件转换为 HTML
- 美观的代码高亮显示
- 支持 side-by-side 对比
- 易于分享和存档

## 安装

### 通过 npm 安装

```bash
npm install -g diff2html
```

## 基础使用

### 快速开始

**操作步骤**:
1. 生成 diff 文件
2. 使用 diff2html 转换为 HTML

具体示例请参考：[examples/basic-usage.md](examples/basic-usage.md)

### 常用命令

| 命令 | 说明 |
|------|------|
| `diff2html -i file -- diff.file` | 从文件读取 diff |
| `diff2html -F output.html` | 指定输出文件名 |
| `diff2html --open` | 生成后自动打开浏览器 |

## 常用命令

| 命令 | 说明 |
|------|------|
| `diff2html -i file -- diff.file` | 从文件读取 diff |
| `diff2html -F output.html` | 指定输出文件名 |
| `diff2html --open` | 生成后自动打开浏览器 |

## 进阶用法

### 对比指定文件

**操作步骤**:
[TBD]

### 自定义样式

**操作步骤**:
[TBD]

## 资源

- **原文件位置**: `工具/softs/index/diff2html.md`
