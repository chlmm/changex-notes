---
type: workflow-diagram
category: lazygit
title: 高级自定义命令流程
description: Lazygit 自定义命令的配置和执行流程
---

# 高级自定义命令流程

```mermaid
flowchart LR
    A[主界面] --> B{触发自定义命令}
    B -->|配置键位| C[加载custom_commands配置]
    C --> D[解析命令模板]
    D --> E[注入上下文变量<br/>• branch_name<br/>• selected_file<br/>• commit_hash]
    E --> F[执行Shell命令]
    F -->|成功| G[显示绿色Toast通知]
    F -->|失败| H[显示红色错误详情]
    G & H --> I[可选：刷新相关面板]
    
    %% 配置示例（实际配置文件中）：
    %% customCommands:
    %%   - key: '<c-p>'
    %%     command: 'git push origin {{.CurrentBranch}}'
    %%     context: 'branches'
    
    classDef process fill:#e6f7ff,stroke:#1890ff;
    classDef decision fill:#fff7e6,stroke:#fa8c16;
    classDef success fill:#f6ffed,stroke:#52c41a;
    classDef error fill:#fff2f2,stroke:#ff4d4f;
    
    class C,D,E,F process;
    class B decision;
    class G success;
    class H error;
```

## 配置示例

在 `~/.config/lazygit/config.yml` 中添加：

```yaml
customCommands:
  - key: '<c-p>'
    command: 'git push origin {{.CurrentBranch}}'
    context: 'branches'
    description: 'Push to origin'
```

## 可用上下文变量

| 变量 | 说明 |
|------|------|
| `{{.CurrentBranch}}` | 当前分支名 |
| `{{.SelectedFile}}` | 选中的文件 |
| `{{.SelectedCommit}}` | 选中的提交哈希 |
