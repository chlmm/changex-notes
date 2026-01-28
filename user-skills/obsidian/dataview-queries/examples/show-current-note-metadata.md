---
type: snippet
category: Dataview
language: dataview
tags: [dataview, table, metadata]
title: 获取当前笔记元数据
description: 显示当前笔记的元数据表格。
---

# 获取当前笔记元数据

## 用途

显示当前笔记的完整元数据表格，包括所有属性和值。

## 适用场景

- 调试 frontmatter
- 了解笔记数据结构
- 学习 Dataview 元数据字段

## 操作步骤

1. 将代码插入到任意笔记中
2. 查看当前笔记的完整元数据

## 代码

```dataview
table this
where file = this.file
```

## 效果说明

显示当前笔记的所有元数据字段和值，帮助理解 Dataview 可用的数据。
