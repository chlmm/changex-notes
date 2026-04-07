---
type: example
category: diff2html
title: 基础使用示例
description: 将 Git diff 输出转换为 HTML 文件的基本操作
---

# diff2html 基础使用示例

## 示例：对比两个 Commit

### 场景

对比两个 commit 之间的变更，并生成可视化的 HTML 报告。

### 操作步骤

1. 在 Git 仓库中生成 diff 文件
```bash
git diff 3f594a3 7fddf76 > changes.diff
```

2. 使用 diff2html 转换为 HTML
```bash
diff2html -i file -- changes.diff -F commit-diff.html
```

3. 打开生成的 HTML 文件查看对比结果

### 完整命令流程

```bash
# 进入 Git 仓库目录
cd ~/Desktop/untitled_0822/untitled

# 生成 diff 文件
git diff 3f594a3 7fddf76 > changes.diff

# 转换为 HTML
diff2html -i file -- changes.diff -F commit-diff.html
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `-i file` | 从文件读取 diff |
| `-- changes.diff` | 指定输入的 diff 文件 |
| `-F commit-diff.html` | 指定输出的 HTML 文件名 |

## 其他常用示例

### 示例：直接查看（不保存文件）

```bash
diff2html -i file -- changes.diff --open
```

### 示例：对比工作区与暂存区

```bash
git diff > changes.diff
diff2html -i file -- changes.diff -F working-tree-diff.html
```

### 示例：对比暂存区与最新提交

```bash
git diff --cached > staged.diff
diff2html -i file -- staged.diff -F staged-diff.html
```
