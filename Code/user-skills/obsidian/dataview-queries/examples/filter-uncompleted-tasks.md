---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, tasks, filter]
title: 筛选包含特定文本的未完成任务
description: 在指定文件夹中查找包含特定文本（如"数列"）的未完成任务。
---

# 筛选包含特定文本的未完成任务

## 用途

在指定文件夹中查找包含特定关键词的未完成任务。

## 适用场景

- 按项目筛选任务
- 按标签筛选任务
- 按关键词查找相关任务

## 操作步骤

1. 修改代码中的文件夹路径 `"ww"`
2. 修改筛选关键词 `"数列"`
3. 插入到笔记中查看结果

## 代码

```dataviewjs
dv.taskList(
	dv.pages('"ww"')
	.file.tasks
	.where(t => !t.completed)
	.where(t => t.text.includes("数列"))
)
```

## 自定义说明

- `"ww"` - 修改为你要查询的文件夹路径
- `"数列"` - 修改为你要筛选的关键词
