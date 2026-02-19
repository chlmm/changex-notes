---
type: workflow-diagram
category: lazygit
title: Lazygit 核心架构图
description: Lazygit 的整体架构层次和组件关系
---

# Lazygit 核心架构图

```mermaid
graph TD
    A[UI Layer] -->|用户交互| B[Application Logic Layer]
    B -->|执行命令| C[Command Execution Layer]
    C -->|调用| D[Git CLI]
    B -->|读取/写入| E[Configuration Layer]
    A -->|加载配置| E
    
    subgraph UI Layer
        A1[TUI Rendering<br/>• 基于gocui/charm.sh<br/>• 面板布局管理]
        A2[Keyboard Handler<br/>• 快捷键映射<br/>• 事件分发]
    end
    
    subgraph Application Logic Layer
        B1[State Manager<br/>• 仓库状态缓存<br/>• 实时更新]
        B2[Panel Controllers<br/>• 分支/提交/文件控制器<br/>• 视图协调]
    end
    
    subgraph Command Execution Layer
        C1[Git Wrapper<br/>• 封装原生命令<br/>• 错误处理]
        C2[Async Executor<br/>• 后台任务队列<br/>• 进度反馈]
    end
    
    subgraph Configuration Layer
        E1[Config Loader<br/>• YAML解析<br/>• 默认值回退]
        E2[I18n Manager<br/>• 多语言支持<br/>• 动态切换]
    end
    
    classDef layer fill:#e6f7ff,stroke:#1890ff,stroke-width:2px;
    class A,B,C,E layer;
    classDef component fill:#f6ffed,stroke:#52c41a;
    class A1,A2,B1,B2,C1,C2,E1,E2 component;
```

## 架构层次说明

| 层次 | 职责 |
|------|------|
| **UI Layer** | TUI 渲染、键盘事件处理 |
| **Application Logic Layer** | 状态管理、面板控制器 |
| **Command Execution Layer** | Git 命令封装、异步执行 |
| **Configuration Layer** | 配置加载、国际化 |
