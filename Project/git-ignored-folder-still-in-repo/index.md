---
date: 2026-04-29
type: question
tags: [git, gitignore, tracking]
platform: [linux, macos, windows]
skill_ref: executor-skills/git/workflows/cleanup-cached-files.md
reproducible: script
---

# Git 已忽略文件夹仍存在于仓库中的问题

`.gitignore` 后加导致已跟踪文件无法被忽略。

## 复现方式

运行 `scripts/setup-repro.sh` 创建模拟 git 仓库，内含已被跟踪的 .trash 目录。

## 文档

- [steps](doc/steps.md) — 标准解决步骤
- [decision-tree](doc/decision-tree.md) — 此类问题的决策逻辑
- [investigation](doc/investigation.md) — 实际排查过程
