#!/bin/bash
# 复现 git 已忽略文件夹仍存在于仓库中的问题

set -e

REPO_NAME="test-gitignore-repro"
rm -rf "$REPO_NAME"
mkdir "$REPO_NAME" && cd "$REPO_NAME"

# 初始化仓库
git init

# 创建 .trash 目录并添加文件（模拟先有文件的情况）
mkdir .trash
echo "temp file" > .trash/temp.txt
git add .
git commit -m "Initial commit with .trash tracked"

# 后加 .gitignore（模拟后加忽略规则的情况）
echo ".trash/*" > .gitignore
git add .gitignore
git commit -m "Add .gitignore"

# 此时问题出现：.trash 仍被跟踪
echo ""
echo "=== 问题复现 ==="
echo ".trash 目录已在 .gitignore 中，但仍被 Git 跟踪："
git ls-files .trash

echo ""
echo "现在可以执行解决方案："
echo "  git rm -r --cached .trash"
echo "  git commit -m \"Remove .trash from tracking\""
