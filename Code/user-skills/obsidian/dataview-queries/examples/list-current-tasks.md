---
type: snippet
category: Dataview
language: dataview
tags: [dataview, table, list, tasks, metadata]
title: 获取当前笔记列表和任务
description: 显示当前笔记包含的列表和任务数据。
---

# 获取当前笔记列表和任务

## 用途

显示当前笔记包含的所有列表项和任务数据。

## 适用场景

- 查看当前笔记的结构
- 调试任务数据
- 了解笔记内容组成

## 操作步骤

1. 将代码插入到任意笔记中
2. 查看当前笔记的列表和任务信息

## 代码

```dataview
table this.file.lists, this.file.tasks
where file = this.file
limit 1
```

## 效果说明

显示当前笔记中所有列表项和任务的详细数据。
