---
type: snippet
category: Dataview
language: dataview
tags: [dataview, table, tasks, filter, metrics]
title: 推文任务统计表
description: 统计指定文件夹中包含 #tweet 标签的任务完成情况及文件修改信息。
created: 2023-10-27
status: active
---
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
