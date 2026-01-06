---
type: snippet
category: Dataview
language: dataview
tags: [dataview, table, metadata]
title: 获取当前笔记元数据
description: 显示当前笔记的元数据表格。
created: 2023-10-27
status: active
---
```dataview
table this
where file = this.file
```
