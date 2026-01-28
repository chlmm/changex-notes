---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, tasks, filter]
title: 筛选日记中特定人员未完成任务
description: 在日记文件夹中查找包含特定人员名称（如"周维"）的未完成任务。
---

# 筛选日记中特定人员未完成任务

## 用途

在日记文件夹中查找包含特定人员名称的未完成任务。

## 适用场景

- 按人员分配查看任务
- 团队协作任务跟踪
- 个人任务筛选

## 操作步骤

1. 修改代码中的文件夹路径 `"01-日记文件夹"`
2. 修改人员名称 `"周维"`
3. 插入代码块查看结果

## 代码

```dataviewjs
dv.taskList(
	dv.pages('"01-日记文件夹"')
	.file.tasks
	.where(t => t.text.includes("周维"))
	.where(t => !t.completed)
		
)
```

## 自定义说明

- `"01-日记文件夹"` - 修改为你要查询的文件夹路径
- `"周维"` - 修改为你要筛选的人员名称

## 扩展用法

可以同时筛选多个人员：
```dataviewjs
.where(t => t.text.includes("周维") || t.text.includes("张三"))
```
