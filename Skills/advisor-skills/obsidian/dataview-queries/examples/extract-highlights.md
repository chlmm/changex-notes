---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, highlight, extraction, regex]
title: 获取本文件高亮内容
description: 提取当前笔记中所有高亮文本（==text==）并以列表形式展示。
---

# 获取本文件高亮内容

## 用途

提取当前笔记中所有高亮文本（`==text==`）并以列表形式展示。

## 适用场景

- 自动收集笔记重点
- 复习时快速浏览关键内容
- 生成摘要

## 操作步骤

1. 将代码块插入到需要提取高亮的笔记中
2. 确保笔记中有 `==高亮内容==` 格式的文本
3. 查看自动生成的列表

## 代码

```dataviewjs
//定义一个函数，接受一个markdown字符串作为参数
function extractHighlight(markdown) {
  //定义一个空数组，用来存放高亮部分
  let highlights = [];
  //定义一个正则表达式，匹配被==包裹的部分
  let regex = /==(.+?)==/g;
  //定义一个变量，用来存放正则表达式的匹配结果
  let match;
  //使用循环，遍历所有的匹配结果
  while (match = regex.exec(markdown)) {
    //把匹配结果中的第一个捕获组（也就是高亮部分）添加到数组中
    highlights.push(match[1]);
  }
  //返回数组
  return highlights.filter(p=>p!=  '(.+?)');
}

dv.list(extractHighlight(await app.vault.readRaw(dv.current().file.path)))
```

## 效果说明

提取所有 `==高亮内容==` 格式的文本，以无序列表形式展示。
