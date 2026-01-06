---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, tasks, filter]
title: 筛选日记中特定人员未完成任务
description: 在日记文件夹中查找包含特定人员名称（如“周维”）的未完成任务。
created: 2023-10-27
status: active
---
```dataviewjs
dv.taskList(
	dv.pages('"01-日记文件夹"')
	.file.tasks
	.where(t => t.text.includes("周维"))
	.where(t => !t.completed)
		
)
```
