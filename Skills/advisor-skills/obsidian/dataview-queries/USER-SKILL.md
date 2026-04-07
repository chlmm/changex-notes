---
name: obsidian-dataview-queries
description: Obsidian Dataview 插件查询合集。用于任务管理、笔记导航、数据统计等场景。
type: obsidian-plugin
execution_mode: advisor
metadata:
  category: obsidian
  plugin: dataview
---

# Obsidian Dataview 查询合集

## 概述

Dataview 是 Obsidian 的核心数据查询插件，通过类 SQL 语法检索笔记元数据，支持 `dataview` 和 `dataviewjs` 两种查询方式。

## 前置条件

- 安装并启用 Dataview 插件
- 了解基础 YAML frontmatter 语法

## 快速开始

### 基础查询语法

**Dataview (类 SQL)**
```dataview
TABLE 字段1, 字段2
FROM "文件夹" or #标签
WHERE 条件
SORT 字段 DESC
LIMIT 10
```

**DataviewJS (JavaScript)**
```dataviewjs
dv.table(
  ["列1", "列2"],
  dv.pages("#标签")
    .map(p => [p.file.name, p.file.ctime])
)
```

## 查询示例分类

### 日期与时间

| 示例 | 用途 | 文件 |
|------|------|------|
| 日期进度条 | 计算日期进度并显示进度条 | [examples/date-progress-bar.md](examples/date-progress-bar.md) |
| 日期导航 | 日记前后天导航 | [examples/date-navigation.md](examples/date-navigation.md) |

### 任务管理

| 示例 | 用途 | 文件 |
|------|------|------|
| 筛选未完成任务 | 按关键词筛选未完成任务 | [examples/filter-uncompleted-tasks.md](examples/filter-uncompleted-tasks.md) |
| 按人员筛选任务 | 筛选特定人员的未完成任务 | [examples/filter-person-tasks.md](examples/filter-person-tasks.md) |
| 推文任务统计 | 统计带 #tweet 标签的任务 | [examples/tweet-tasks-statistics.md](examples/tweet-tasks-statistics.md) |

### 内容提取

| 示例 | 用途 | 文件 |
|------|------|------|
| 提取标题内容 | 收集特定标题下的内容 | [examples/extract-heading-content.md](examples/extract-heading-content.md) |
| 提取高亮内容 | 提取 ==高亮== 文本 | [examples/extract-highlights.md](examples/extract-highlights.md) |

### 元数据与调试

| 示例 | 用途 | 文件 |
|------|------|------|
| 显示当前元数据 | 查看当前笔记完整元数据 | [examples/show-current-note-metadata.md](examples/show-current-note-metadata.md) |
| 列出任务和列表 | 查看当前笔记的任务数据 | [examples/list-current-tasks.md](examples/list-current-tasks.md) |

### API 与外部数据

| 示例 | 用途 | 文件 |
|------|------|------|
| API 请求显示图片 | 从 API 获取并显示图片 | [examples/request-api-and-show-image.md](examples/request-api-and-show-image.md) |

## 使用建议

1. **从简单开始** - 先使用基础的 `dataview` 语法，再尝试 `dataviewjs`
2. **复制修改** - 复制示例文件中的代码，根据需求修改参数
3. **调试技巧** - 使用元数据查询示例了解可用字段

## 资源

- **Dataview 官方文档**: https://blacksmithgu.github.io/obsidian-dataview/
- **示例文件夹**: [./examples/](examples/)
