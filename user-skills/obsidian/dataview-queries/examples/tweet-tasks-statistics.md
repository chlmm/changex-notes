---
type: snippet
category: Dataview
language: dataview
tags: [dataview, table, tasks, filter, metrics]
title: 推文任务统计表
description: 统计指定文件夹中包含 #tweet 标签的任务完成情况及文件修改信息。
---

# 推文任务统计表

## 用途

统计指定文件夹中包含 `#tweet` 标签的任务完成情况及文件修改信息。

## 适用场景

- 社交媒体内容发布跟踪
- 定期任务统计
- 工作效率分析

## 操作步骤

1. 修改代码中的文件夹路径 `"4.permanent/permanent-2022"`
2. 根据需要修改标签筛选条件 `#tweet`
3. 插入代码块查看统计结果

## 代码

```dataview
TABLE WITHOUT ID
  choice(length(filter(file.tasks, (t) => regexmatch(".*#tweet.*", t.text) and !t.completed)) > 0, "✅", "❌") as "Need to Post",
  length(filter(file.tasks, (t) => regexmatch(".*#tweet.*", t.text))) as "Ghost Tasks",
  length(filter(file.tasks.completed, (t) => t)) as "Done Tasks",
  length(file.tasks) as "Total Tasks",
  striptime(date(today)) - striptime(file.ctime) as "Duration",
  dateformat(date(file.mtime), "yyyy-MM-dd") as "Last Modified",
  file.link as "Source"
FROM "4.permanent/permanent-2022"
SORT date desc
LIMIT 7
```

## 字段说明

| 字段 | 说明 |
|------|------|
| Need to Post | 是否需要发布（✅/❌） |
| Ghost Tasks | 包含 #tweet 标签的任务数 |
| Done Tasks | 已完成任务数 |
| Total Tasks | 总任务数 |
| Duration | 文件创建至今的天数 |
| Last Modified | 最后修改日期 |
| Source | 文件链接 |

## 自定义说明

- `"4.permanent/permanent-2022"` - 修改为你要统计的文件夹
- `#tweet` - 修改为你要跟踪的标签
