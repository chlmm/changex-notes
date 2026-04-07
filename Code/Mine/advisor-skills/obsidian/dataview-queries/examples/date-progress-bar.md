---
type: snippet
category: Dataview
language: dataviewjs
tags:
  - dataview
  - dataviewjs
  - progress
  - moment
  - date
title: 日期进度条计算
description: 计算两个日期之间的进度并显示剩余天数百分比。
---

# 日期进度条计算

## 用途

计算两个日期之间的进度并显示剩余天数百分比，以可视化进度条形式展示。

## 适用场景

- 项目周期跟踪
- 学习进度监控
- 倒计时提醒

## 操作步骤

1. 新建笔记或在现有笔记中插入代码块
2. 将代码块类型设置为 `dataviewjs`
3. 修改代码中的起始日期 (`a`) 和结束日期 (`b`)
4. 查看渲染结果

## 代码

```dataviewjs
var a = moment("2024-05-01");
var b = moment("2024-05-25");

var n = moment()
var t = moment().startOf('day');

let q =  b.diff(a, 'days');
let p =  b.diff(t, 'days');
let r =  t.diff(a, 'days');

let h = n.diff(a, 'hours');
let i = b.diff(a, 'hours');

let html = `<progress style="height:10px;width:80%" value="`+h+`" max="`+i+`"></progress>`

if (r>0 && r<q) {
	html += `\n#### `+p+` days left of `+q+` days\n`
	html += (h/i*100).toFixed(2)+`% complete`
} else if (r==0) {
	html += `\nstars today`
} else if (r==q) {
	html += `\nends today`
} else if (r>q) {
	html += `\nended `+-p+` days ago`
}else {
	html += `\n#### `+-r+` days to go`
}

dv.paragraph(html)
```

## 效果说明

- 显示进度条
- 显示剩余天数
- 显示完成百分比
- 支持多种状态：进行中、今天开始、今天结束、已结束、未开始
