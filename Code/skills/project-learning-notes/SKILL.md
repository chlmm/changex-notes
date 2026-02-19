---
name: project-learning-notes
description: 用于创建GitHub项目学习笔记的Skill。接收GitHub项目链接，自动提取用户名和项目名，在资源学习/项目/目录下按 用户名@@@项目名 创建独立文件夹，包含Obsidian格式的Markdown笔记文件。
---

# 项目学习笔记创建器

## 功能概述

接收GitHub项目链接，自动提取用户名（owner）和项目名（repo），为每个项目创建独立的学习笔记文件夹。采用 `用户名@@@项目名` 的命名格式解决项目重名问题，包含结构化的学习笔记Markdown文件。

## 使用时机

当用户需要：
- 学习开源项目源码时
- 记录代码阅读笔记时
- 分析项目架构设计时
- 整理项目实践经验时

## 支持的链接格式

| 平台 | 链接示例 | 提取格式 |
|------|----------|----------|
| GitHub | `https://github.com/username/repo-name` | 用户名@@@项目名 |
| GitHub | `https://github.com/username/repo-name/tree/main/...` | 用户名@@@项目名 |

## 工作流程

### 1. 接收用户输入

用户需提供：
- **项目链接**（必需）- GitHub项目链接
- **项目描述**（可选）- 项目简介或学习目标

**示例输入：**
```
链接: https://github.com/Qt-Widgets/fairwindplusplus-navigation-software-dial-map
描述: 一个用于航海导航软件开发的地图界面组件项目
```

### 2. 解析链接提取信息

**GitHub链接处理：**
```
输入: https://github.com/username/repo-name
提取: username@@@repo-name

输入: https://github.com/username/repo-name/tree/main/src
提取: username@@@repo-name (忽略后续路径)
```

### 3. 规范化文件夹名称

**处理规则：**
- 保留GitHub用户名原样
- 使用 `@@@` 作为分隔符（解决用户名/项目名中的/冲突）
- 保留项目名原样

**示例：**
```
链接: https://github.com/Qt-Widgets/fairwindplusplus-navigation-software-dial-map
文件夹: Qt-Widgets@@@fairwindplusplus-navigation-software-dial-map
```

### 4. 创建项目学习目录

**目录结构：**
```
资源学习/项目/
└── {用户名@@@项目名}/               # 项目专属目录
    ├── index.md                     # 项目主笔记
    ├── code-review.md               # 代码阅读笔记
    ├── architecture.md              # 架构分析笔记
    └── README.md                    # 项目原README备份
```

**示例：**
```
资源学习/项目/
├── Qt-Widgets@@@fairwindplusplus-navigation-software-dial-map/
│   ├── index.md
│   ├── code-review.md
│   ├── architecture.md
│   └── README.md
├── torvalds@@@linux/
│   └── ...
└── ...
```

### 5. 创建Markdown笔记文件

#### 主笔记文件 (index.md)

**文件位置：** `资源学习/项目/{用户名@@@项目名}/index.md`

**文件内容模板：**
```markdown
---
title: {项目名}
owner: {用户名}
url: {原始链接}
tags: [项目学习, 待分类]
status: 未开始
created: {YYYY-MM-DD}
---

# {项目名}

> 作者/组织: [{用户名}](https://github.com/{用户名})
> 项目链接: [{原始链接}]({原始链接})
> 
> 描述: {项目描述}

## 项目概述

<!-- 项目简介、功能特点、技术栈、为什么学习这个项目 -->

### 核心功能

1. **功能1**
   <!-- 详细描述 -->

2. **功能2**
   <!-- 详细描述 -->

3. **功能3**
   <!-- 详细描述 -->

### 技术栈

<!-- 项目使用的主要技术、框架、语言 -->
- 语言：
- 框架：
- 工具：

### 适用场景

<!-- 这个项目适合解决什么问题 -->

---

## 学习笔记

<!-- 用户个人学习区域（AI 请勿修改以下内容） -->

### 关键知识点

<!-- 学习项目过程中掌握的关键技术、设计模式等 -->

### 学习进度

- [ ] 阅读README和文档
- [ ] 搭建本地环境
- [ ] 运行示例代码
- [ ] 阅读核心源码
- [ ] 动手实践/复现
- [ ] 总结输出

### 个人思考

<!-- 学习感悟、技术思考、应用场景联想 -->

### 待办事项

- [ ] 了解项目背景
- [ ] 分析代码结构
- [ ] 记录学习笔记
- [ ] 实践练习

### 相关资源

<!-- 相关文章、视频、类似项目等 -->
```

#### 代码阅读笔记 (code-review.md)

**文件位置：** `资源学习/项目/{用户名@@@项目名}/code-review.md`

**文件内容模板：**
```markdown
# 代码阅读笔记

## 目录结构分析

<!-- 项目整体目录结构说明 -->
```
项目根目录/
├── src/           # 源代码
├── tests/         # 测试文件
├── docs/          # 文档
└── ...
```

## 核心文件分析

### 文件1: `{文件名}`

**作用：** 
<!-- 该文件的主要功能 -->

**关键代码：**
```{语言}
<!-- 粘贴关键代码段 -->
```

**学习要点：**
<!-- 从这段代码中学到了什么 -->

### 文件2: `{文件名}`

...

## 设计模式与技巧

<!-- 项目中使用的设计模式、编程技巧 -->

| 模式/技巧 | 应用场景 | 具体实现 |
|-----------|----------|----------|
|           |          |          |

## 值得借鉴的代码

<!-- 特别好的代码片段，可以复用或学习 -->
```

#### 架构分析笔记 (architecture.md)

**文件位置：** `资源学习/项目/{用户名@@@项目名}/architecture.md`

**文件内容模板：**
```markdown
# 架构分析

## 整体架构图

<!-- 绘制或粘贴项目的架构图 -->
```
[架构图]
```

## 模块划分

### 模块A

**职责：** 
**依赖：** 
**关键类/函数：** 

### 模块B

...

## 数据流分析

<!-- 数据如何在项目中流动 -->

## 扩展性设计

<!-- 项目是如何设计以支持扩展的 -->

## 性能优化点

<!-- 项目中体现的性能优化思路 -->
```

#### README备份 (README.md)

**文件位置：** `资源学习/项目/{用户名@@@项目名}/README.md`

**用途说明：**
- 复制项目原始README内容
- 方便离线查阅
- 可在本地做批注和笔记

### 6. 执行步骤

1. **解析链接**：从GitHub链接中提取用户名和项目名
2. **生成文件夹名**：组合为 `用户名@@@项目名` 格式
3. **创建目录**：创建 `资源学习/项目/{用户名@@@项目名}/` 目录
4. **检查文件**：确认该目录下是否已存在同名文件
5. **创建主笔记**：创建 `index.md` 文件，填充模板
6. **创建代码笔记**：创建 `code-review.md` 文件
7. **创建架构笔记**：创建 `architecture.md` 文件
8. **创建README占位**：创建空的 `README.md` 文件（用户后续可粘贴原README）
9. **确认完成**：向用户报告创建结果

## 示例

**用户输入：**
```
链接: https://github.com/Qt-Widgets/fairwindplusplus-navigation-software-dial-map
描述: 航海导航软件的地图界面组件
```

**执行结果：**
- 创建目录: `资源学习/项目/Qt-Widgets@@@fairwindplusplus-navigation-software-dial-map/`
- 创建主笔记: `资源学习/项目/Qt-Widgets@@@fairwindplusplus-navigation-software-dial-map/index.md`
- 创建代码笔记: `资源学习/项目/Qt-Widgets@@@fairwindplusplus-navigation-software-dial-map/code-review.md`
- 创建架构笔记: `资源学习/项目/Qt-Widgets@@@fairwindplusplus-navigation-software-dial-map/architecture.md`
- 创建README占位: `资源学习/项目/Qt-Widgets@@@fairwindplusplus-navigation-software-dial-map/README.md`
- YAML frontmatter包含项目名、用户名、链接、标签等元数据
- index.md包含项目概述、技术栈、学习进度、个人笔记区域等

## 注意事项

1. **命名规范**：必须使用 `@@@` 分隔用户名和项目名，避免与文件夹路径分隔符 `/` 冲突
2. **目录存在性**：如果目录已存在，提醒用户避免覆盖
3. **链接处理**：支持标准GitHub链接，自动忽略 `/tree/`、`/blob/` 等后续路径
4. **自动添加日期**：自动填充当前日期到 `created` 字段
5. **默认标签**：包含 `项目学习` 和 `待分类`，用户可在Obsidian中后续修改
6. **状态管理**：支持 `未开始`、`学习中`、`已完成` 三种状态
7. **README文件**：创建空文件作为占位，用户需手动将项目README内容复制进来
8. **四文件结构**：
   - `index.md`：主学习笔记，包含项目概述和个人笔记
   - `code-review.md`：代码阅读笔记，分析核心代码和实现细节
   - `architecture.md`：架构分析笔记，理解项目设计思想
   - `README.md`：项目原始README备份
9. **未来扩展**：
   - 可添加 `examples/` 目录存放示例代码
   - 可添加 `notes/` 目录存放额外笔记
   - 可添加 `clone/` 目录存放克隆的项目代码
