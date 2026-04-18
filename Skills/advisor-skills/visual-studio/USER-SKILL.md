---
name: visual-studio
description: Visual Studio IDE C++ 开发指南。按工作流组织，覆盖项目搭建、编辑导航、构建编译、调试、CMake、重构、性能分析等场景。
type: ide
execution_mode: advisor
metadata:
  category: ide
  platform: [windows]
  language: [c++, cmake]
  tags: [Visual Studio, C++, IDE, 调试, 构建]
---

# Visual Studio — C++ 开发指南

## 概述

这个 Skill 帮你在 Visual Studio IDE 中高效进行 C++ 开发。不是菜单手册，而是按工作流组织的策略指南——遇到场景知道**做什么、为什么、什么顺序**。快捷键统一在 [shortcuts.md](shortcuts.md) 查询。

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
| 项目搭建 | 新建项目、模板选择、属性配置 | [workflows/project-setup.md](workflows/project-setup.md) |
| 代码编辑与导航 | 跳转定义、h/cpp切换、查找引用、多文件浏览 | [workflows/editing-navigation.md](workflows/editing-navigation.md) |
| 构建与编译 | Build配置、编译选项、链接错误排查 | [workflows/build-compile.md](workflows/build-compile.md) |
| 调试 | 断点类型、多线程、数据查看、远程调试 | [workflows/debugging.md](workflows/debugging.md) |

### 进阶工作流

| 场景 | 关键时刻 | 文件 |
|------|---------|------|
| CMake 工作流 | CMake项目配置、Presets、vcpkg集成 | [workflows/cmake-workflow.md](workflows/cmake-workflow.md) |
| 重构 | 安全重命名、提取函数、Include管理 | [workflows/refactoring.md](workflows/refactoring.md) |
| 性能分析与诊断 | CPU Profiler、内存分析、代码分析 | [workflows/profiling-diagnostics.md](workflows/profiling-diagnostics.md) |

### 辅助工作流

| 场景 | 关键时刻 | 文件 |
|------|---------|------|
| Git 集成 | 提交、分支、冲突解决 | [workflows/git-integration.md](workflows/git-integration.md) |
| 自定义与扩展 | 键位、主题、插件 | [workflows/customization.md](workflows/customization.md) |

## 快捷键速查

所有快捷键按意图分类，见 [shortcuts.md](shortcuts.md)。

## 版本说明

本指南基于 **Visual Studio 2022** (v17.x) 编写，大部分内容也适用于 VS 2019。C++ 相关功能需要安装"使用 C++ 的桌面开发"工作负载。

## 资源

- **快捷键速查**: [shortcuts.md](shortcuts.md)
- **工作流目录**: [workflows/](workflows/)
