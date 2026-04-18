---
name: qtcreator
description: Qt Creator IDE C++/Qt 开发指南。按工作流组织，覆盖项目搭建、Kit配置、编辑导航、构建编译、调试、Qt Designer、信号槽、QML等场景。
type: ide
execution_mode: advisor
metadata:
  category: ide
  platform: [windows, macos, linux]
  language: [c++, qml, qt]
  tags: [Qt Creator, C++, Qt, QML, 跨平台]
---

# Qt Creator — C++/Qt 开发指南

## 概述

这个 Skill 帮你在 Qt Creator 中高效进行 C++/Qt 开发。不是菜单手册，而是按工作流组织的策略指南——遇到场景知道**做什么、为什么、什么顺序**。快捷键统一在 [shortcuts.md](shortcuts.md) 查询。

## 设计原则

| 层 | 职责 | 文件 |
|----|------|------|
| **策略层** | 做什么、为什么、什么顺序 | `workflows/*.md` |
| **执行层** | 按什么键触发 | [shortcuts.md](shortcuts.md) |
| **索引层** | 有哪些场景、去哪找 | 本文件 |

工作流文件只写操作名（如"跳转定义"），不写快捷键。需要查键时 grep `shortcuts.md` + 操作名即可。

## 工作流索引

### 核心工作流

| 场景 | 关键时刻 | 文件 |
|------|---------|------|
| 项目搭建 | 新建项目、qmake/CMake选择、Kit配置 | [workflows/project-setup.md](workflows/project-setup.md) |
| 代码编辑与导航 | 跳转定义、h/cpp切换、查找引用、分屏 | [workflows/editing-navigation.md](workflows/editing-navigation.md) |
| 构建与编译 | qmake/CMake构建、编译错误排查 | [workflows/build-compile.md](workflows/build-compile.md) |
| 调试 | GDB调试、QObject查看、QML调试、信号槽断点 | [workflows/debugging.md](workflows/debugging.md) |

### Qt 特有工作流

| 场景 | 关键时刻 | 文件 |
|------|---------|------|
| Qt Designer / UI 设计 | 拖控件、布局、信号槽连接 | [workflows/qt-designer.md](workflows/qt-designer.md) |
| Qt 特有工作流 | 信号槽、资源系统、翻译、QML | [workflows/qt-specific-workflow.md](workflows/qt-specific-workflow.md) |
| Kit 与跨平台 | Kit配置、多平台编译、交叉编译 | [workflows/kit-cross-platform.md](workflows/kit-cross-platform.md) |

### 进阶工作流

| 场景 | 关键时刻 | 文件 |
|------|---------|------|
| CMake 工作流 | CMake项目配置、Presets | [workflows/cmake-workflow.md](workflows/cmake-workflow.md) |
| 重构 | 重命名、提取函数、信号槽重构 | [workflows/refactoring.md](workflows/refactoring.md) |
| Git 集成 | 提交、分支、diff | [workflows/git-integration.md](workflows/git-integration.md) |

## 快捷键速查

所有快捷键按意图分类，见 [shortcuts.md](shortcuts.md)。跨平台快捷键差异已在表中标注。

## 版本说明

本指南基于 **Qt Creator 12+** 编写，大部分内容也适用于 Qt Creator 10/11。

## 资源

- **快捷键速查**: [shortcuts.md](shortcuts.md)
- **工作流目录**: [workflows/](workflows/)
