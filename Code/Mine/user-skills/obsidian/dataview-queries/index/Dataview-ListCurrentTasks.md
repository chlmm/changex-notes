---
type: snippet
category: Dataview
language: dataview
tags: [dataview, table, list, tasks, metadata]
title: 获取当前笔记列表和任务
description: 显示当前笔记包含的列表和任务数据。
created: 2023-10-27
status: active
---
```dataview
table this.file.lists, this.file.tasks
where file = this.file
limit 1
```
