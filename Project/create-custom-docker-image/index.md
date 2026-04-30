---
date: 2026-04-15
type: need
tags: [docker, dev-env, cpp, qt]
platform: [linux]
skill_ref: executor-skills/docker/workflows/custom-image.md
reproducible: script
---

# 创建自定义 Docker 开发环境镜像

创建包含 C++/Qt 开发工具的自定义 Docker 镜像。

## 复现方式

1. 准备好 `resources/Dockerfile`
2. 如需镜像加速，配置 `resources/daemon.json`

## 文档

- [steps](doc/steps.md) — 标准解决步骤
- [decision-tree](doc/decision-tree.md) — 此类问题的决策逻辑
- [investigation](doc/investigation.md) — 实际排查过程
