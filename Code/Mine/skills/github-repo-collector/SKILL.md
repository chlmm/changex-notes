---
name: github-repo-collector
description: 从 GitHub URL 获取仓库信息，生成 YAML 格式的项目收藏记录。当用户说"收藏 GitHub 项目"、"获取 GitHub 项目信息"、"添加 GitHub 仓库"时使用。
---

# GitHub Repo Collector

使用 GraphQL API 批量获取 GitHub 仓库信息，生成符合 Notes 系统格式的 YAML 收藏记录。

## 使用方式

```bash
# 单项目
{baseDirectory}/scripts/gh-repo-collect.sh <github_url>

# 多项目批量
{baseDirectory}/scripts/gh-repo-collect.sh <url1> <url2> <url3> ...

# 示例
{baseDirectory}/scripts/gh-repo-collect.sh https://github.com/adhikasp/mcp-reddit
{baseDirectory}/scripts/gh-repo-collect.sh https://github.com/xxx/a https://github.com/yyy/b
```

## 输出格式

```yaml
---
url: https://github.com/adhikasp/mcp-reddit
name: adhikasp/mcp-reddit
title: mcp-reddit
description: A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.
stars: 368
language: Python
topics: [llm, mcp, model-context-protocol, reddit]
tags: []
comment: 
---
```

## 字段说明

| 字段 | 来源 | 说明 |
|------|------|------|
| `url` | GitHub API | 仓库链接 |
| `name` | GitHub API | owner/repo 格式 |
| `title` | GitHub API | 项目名称 |
| `description` | GitHub API | 项目描述 (About) |
| `stars` | GitHub API | Star 数 |
| `language` | GitHub API | 主要语言 |
| `topics` | GitHub API | GitHub Topics |
| `tags` | AI 整理时填写 | 个人分类标签 |
| `comment` | AI 整理时填写 | 个人备注 |

## 技术方案

使用 **GraphQL API** 而非 REST API：

| 对比项 | REST API | GraphQL |
|--------|----------|---------|
| API 调用 | N 次（每项目一次） | 1 次（批量） |
| 速率限制 | 易触发限制 | 节省配额 |
| 并发处理 | 需文件锁 | 单次原子操作 |

## 工作流程（收件箱模式）

### 1. 快速收藏
用户提供 GitHub URL → AI 执行脚本 → 自动追加到 `Index.md` 收件箱

### 2. 定期整理
用户说"整理 GitHub 收件箱" → AI 分析项目 → 自动分类、添加标签、备注 → 移动到分类文件

## 存储位置

```
changex-notes/Index/GitHub/
├── Index.md        # 收件箱（待整理项目）
├── AI工具.md       # AI 相关工具
├── MCP工具.md      # MCP 工具
├── 开源项目.md     # 开源项目收藏
└── ...
```

## 使用示例

### 快速收藏单个项目

用户说：收藏这个项目 https://github.com/mendableai/firecrawl

AI 执行：
```bash
{baseDirectory}/scripts/gh-repo-collect.sh https://github.com/mendableai/firecrawl
```

### 批量收藏多个项目

用户说：帮我收藏这几个项目：
- https://github.com/xxx/a
- https://github.com/yyy/b
- https://github.com/zzz/c

AI 执行：
```bash
{baseDirectory}/scripts/gh-repo-collect.sh \
  https://github.com/xxx/a \
  https://github.com/yyy/b \
  https://github.com/zzz/c
```

### 整理收件箱

用户说：整理 GitHub 收件箱

AI 会：
1. 读取 `Index.md` 中待整理的项目
2. 分析每个项目的 `description`、`topics`、`language`
3. 决定分类文件、添加标签、补充备注
4. 将项目移动到对应分类文件
5. 清空 `Index.md` 收件箱

## 标签规范

整理时使用的标签应保持一致：

| 类别 | 常用标签 |
|------|----------|
| AI 工具 | AI工具, LLM, AI应用 |
| MCP 工具 | MCP工具, MCP |
| 开发工具 | 开发工具, 工具 |
| 前端 | 前端, 前端框架 |
| 后端 | 后端, 后端框架 |
| 爬虫 | 爬虫, 数据采集 |
| 学习资源 | 学习资源, 教程 |

## 依赖

- `gh` (GitHub CLI) - 需要已登录认证
- `jq` - JSON 处理
