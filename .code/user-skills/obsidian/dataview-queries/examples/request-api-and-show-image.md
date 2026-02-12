---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, api, request, image]
title: 请求API并显示图片
description: 通过API请求远程数据（如xkcd漫画）并在笔记中显示图片。
---

# 请求API并显示图片

## 用途

通过 API 请求远程数据并在笔记中显示图片。

## 适用场景

- 显示每日漫画（xkcd 等）
- 显示远程图片资源
- 动态获取网络内容

## 操作步骤

1. 修改代码中的 API URL
2. （可选）修改请求头 `headers`
3. 插入代码块查看结果

## 代码

```dataviewjs
const headers = { "Authorization": "Bearer whatever" }
let data = await requestUrl({url: "https://xkcd.com/info.0.json", headers})
let image = data.json.img
dv.paragraph(`![](${image})`)
```

## 自定义说明

- `url` - API 端点地址
- `headers` - 请求头（如需要身份验证）
- `data.json.img` - 根据 API 响应结构调整图片 URL 路径

## 示例：xkcd 漫画

上述代码会从 xkcd API 获取最新漫画信息并显示图片。
