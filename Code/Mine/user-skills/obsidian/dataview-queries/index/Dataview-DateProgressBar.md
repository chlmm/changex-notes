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
created: 2023-10-27
status: active
---
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
