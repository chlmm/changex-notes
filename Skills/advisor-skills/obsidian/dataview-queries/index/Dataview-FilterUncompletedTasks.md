---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, tasks, filter]
title: 筛选包含特定文本的未完成任务
description: 在指定文件夹中查找包含特定文本（如“数列”）的未完成任务。
created: 2023-10-27
status: active
---
```dataviewjs
dv.taskList(
	dv.pages('"ww"')
	.file.tasks
	.where(t => !t.completed)
	.where(t => t.text.includes("数列"))
)
```
