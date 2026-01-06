---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, api, request, image]
title: 请求API并显示图片
description: 通过API请求远程数据（如xkcd漫画）并在笔记中显示图片。
created: 2023-10-27
status: active
---
```dataviewjs
const headers = { "Authorization": "Bearer whatever" }
let data = await requestUrl({url: "https://xkcd.com/info.0.json", headers})
let image = data.json.img
dv.paragraph(`![](${image})`)
```
