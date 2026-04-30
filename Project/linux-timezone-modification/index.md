---
date: 2026-01-25
type: need
tags: [linux, timezone, system-admin]
platform: [linux]
skill_ref: null
reproducible: manual
---

# Linux 系统时区修改

Linux 系统查看和修改时区设置。

## 复现方式

1. 登录 Linux 服务器（云服务器或本地虚拟机均可）
2. 执行 `date` 或 `timedatectl` 查看当前时区
3. 若时区不是 Asia/Shanghai 则可复现需求

## 文档

- [steps](doc/steps.md) — 标准解决步骤
- [decision-tree](doc/decision-tree.md) — 此类问题的决策逻辑
- [investigation](doc/investigation.md) — 实际排查过程
