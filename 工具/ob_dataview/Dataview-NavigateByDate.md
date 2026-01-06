---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, daily-notes, navigation]
title: 日期导航代码片段
description: 在日记笔记中显示前一天和后一天的日期导航。
created: 2023-10-27
status: active
---
```dataviewjs
/*
    previous/next note by date for Daily Notes
    Also works for other files having a `date:` YAML entry.
    MCH 2021-06-14
*/
var none = '(none)';
var p = dv.pages('"' + dv.current().file.folder + '"').where(p => p.file.day).map(p => [p.file.name, p.file.day.toISODate()]).sort(p => p[1]);
var t = dv.current().file.day ? dv.current().file.day.toISODate() : DateTime.now().toISODate();
// Obsidian uses moment.js; Luxon’s format strings differ!
var format = app['internalPlugins']['plugins']['daily-notes']['instance']['options']['format'] || 'YYYY-MM-DD';
var current = '(' + moment(t).format(format) + ')';
var nav = [];
var today = p.find(p => p[1] == t);
var next = p.find(p => p[1] > t);
var prev = undefined;
p.forEach(function (p, i) {
    if (p[1] < t) {
        prev = p;
    }
});
nav.push(prev ? '[[' + prev[0] + ']]' : none);
//nav.push(today ? today[0] : none);
nav.push(today ? today[0] : current);
nav.push(next ? '[[' + next[0] + ']]' : none);

//dv.list(nav);
//dv.paragraph(nav.join(" · "));
dv.paragraph(nav[0] + ' ← ' + nav[1] + ' → ' + nav[2]);
```

## 代码分析
以下是您提供的代码逐行分析的功能：

1. 第 1 行：定义了 `none` 变量，用于表示“无”。
2. 第 2 行：调用了 `dv.pages` 函数，获取存储库中的所有文件。
3. 第 3 行：使用 `where` 方法过滤掉没有 `day` 属性的文件，并将每个文件转换为包含文件名和日期的数组。
4. 第 4 行：使用 `sort` 方法按照日期升序排序文件。
5. 第 5 行：定义了 `t` 变量，用于存储当前日期。如果当前文件具有 `day` 属性，则使用该属性的日期；否则，使用当前日期。
6. 第 6 行：获取 Obsidian 的日期格式设置。Obsidian 使用 moment.js 库来处理日期格式，而 Luxon 库的格式字符串略有不同。
7. 第 7 行：定义了 `current` 变量，用于存储当前日期的字符串表示。该字符串由当前日期根据格式设置生成。
8. 第 8 行：定义了 `nav` 数组，用于存储导航链接。
9. 第 9 行：使用 `find` 方法查找与当前日期相同的文件，并将其添加到导航数组中。
10. 第 10 行：使用 `find` 方法查找下一个日期大于当前日期的文件，并将其添加到导航数组中。
11. 第 11-15 行：遍历文件数组，查找上一个日期小于当前日期的文件，并将其添加到导航数组中。
12. 第 16 行：将上一个链接或 `(none)` 添加到导航数组中。
13. 第 18 行：将当前链接或当前日期字符串添加到导航数组中。
14. 第 20 行：将下一个链接或 `(none)` 添加到导航数组中。
15. 第 23 行：使用 `dv.paragraph` 函数生成包含导航链接的段落。

这段代码的功能是查询存储库中的文件，并生成一个包含上一个链接、当前链接和下一个链接的段落。

如果您对 DataViewJS 或 Obsidian 有任何进一步的问题或需要进一步帮助，请随时提问！