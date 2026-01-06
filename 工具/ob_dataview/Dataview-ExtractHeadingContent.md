---
type: snippet
category: Dataview
language: dataviewjs
tags: [dataview, dataviewjs, table, heading, extraction]
title: 提取指定标题下的内容
description: 查找包含特定标签的笔记中某个特定标题下的内容并生成表格。
created: 2023-10-27
status: active
---
```dataviewjs

// 表格标题内容
const headers = ["位置", "内容"];

// 需要索引的栏目
const targetHeading = "定义[^1]";

// 用于定位的标签或者文件夹地址
const pages = dv.pages("#review");
const pagesArray = pages.array();

const targetPagesArray = [];
const contentArray = [];

for(let i = 0; i < pagesArray.length;i++) {
    const currentFile = pagesArray[i].file;
    const sectionCache = app.metadataCache.getFileCache(currentFile);
    
    const headingCache = sectionCache.headings?.filter(h => {
        return h.heading === targetHeading
    })
    
    if(headingCache?.length > 0) {
        const headingRange = {
            start: headingCache[0].position.start.offset,
            end: headingCache[0].position.end.offset,
        };
        const heading = headingCache[0].heading;
        const content = await dv.io.load(currentFile.path);
        
        if(!content) continue;
        const headingInRange = content.slice(headingRange.start, headingRange.end);
        const contentInNextRange = content.slice(headingRange.end);
        
        const level = headingInRange.match(/#{1,6}/)[0].length;
        const nextHeadingRegex = new RegExp(`(^|\\n)#{1,${level}}\\s`);
        
        const position = contentInNextRange.match(nextHeadingRegex);

        let contentRange;
        let positionEnd;

        if(position) {
            positionEnd = headingRange.end + position?.index;
            contentRange = content.slice(headingRange.end, positionEnd);
        }else {
            contentRange = content.slice(headingRange.end);
        }
        
        const link = dv.sectionLink(currentFile.name, targetHeading)
        contentArray.push({
            file: link,
            content: contentRange,
        })
    }
}

dv.table(headers, contentArray.map(
    p => 
        [
            p.file,
            p.content,
        ]
    
))
```


```dataviewjs
// 表格标题内容
const headers = ["位置", "内容"];

// 需要索引的栏目
const targetHeading = "定义[^1]";

// 用于定位的标签或者文件夹地址
const pages = dv.pages("#review");
const pagesArray = pages.array();

const targetPagesArray = [];
const contentArray = [];

for(let i = 0; i < pagesArray.length;i++) {
    const currentFile = pagesArray[i].file;
    const sectionCache = app.metadataCache.getFileCache(currentFile);
    
    const headingCache = sectionCache.headings?.filter(h => {
        return h.heading === targetHeading
    })
    
    if(headingCache?.length > 0) {
        const headingRange = {
            start: headingCache[0].position.start.offset,
            end: headingCache[0].position.end.offset,
        };
        const heading = headingCache[0].heading;
        const content = await dv.io.load(currentFile.path);
        
        if(!content) continue;
        const headingInRange = content.slice(headingRange.start, headingRange.end);
        const contentInNextRange = content.slice(headingRange.end);
        
        const level = headingInRange.match(/#{1,6}/)[0].length;
        const nextHeadingRegex = new RegExp(`(^|\\n)#{1,${level}}\\s`);
        
        const position = contentInNextRange.match(nextHeadingRegex);

        let contentRange;
        let positionEnd;

        if(position) {
            positionEnd = headingRange.end + position?.index;
            contentRange = content.slice(headingRange.end, positionEnd);
        }else {
            contentRange = content.slice(headingRange.end);
        }
        
        const link = dv.sectionLink(currentFile.name, targetHeading)
        contentArray.push({
            file: link,
            content: contentRange,
        })
    }
}

dv.table(headers, contentArray.map(
    p => 
        [
            p.file,
            p.content,
        ]
    
))
```

