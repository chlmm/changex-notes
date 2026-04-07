#!/bin/bash

# GitHub Repo Collector - 使用 GraphQL API 批量获取 GitHub 仓库信息
# 用法: gh-repo-collect.sh <github_url_or_owner_repo> [url2] [url3] ...
# 支持单项目和多项目批量收藏

set -e

# 配置
NOTES_ROOT="/workspace/changex-notes"
INDEX_FILE="$NOTES_ROOT/Index/GitHub/Index.md"

# 检查参数
if [ -z "$1" ]; then
    echo "用法: $0 <github_url_or_owner_repo> [url2] [url3] ..."
    echo ""
    echo "示例:"
    echo "  # 单项目"
    echo "  $0 https://github.com/adhikasp/mcp-reddit"
    echo "  $0 adhikasp/mcp-reddit"
    echo ""
    echo "  # 多项目"
    echo "  $0 https://github.com/xxx/a https://github.com/yyy/b"
    exit 1
fi

# 检查 gh 是否已登录
if ! gh auth status &>/dev/null; then
    echo "错误: gh 未登录，请先执行 'gh auth login'"
    exit 1
fi

# 解析 URL 或 owner/repo 格式，提取 owner 和 name
parse_repo() {
    local input="$1"
    if [[ "$input" == https://github.com/* ]]; then
        # 从 URL 提取 owner/name
        echo "$input" | sed 's|https://github.com/||' | cut -d'/' -f1,2
    else
        echo "$input"
    fi
}

# 解析所有参数
repos=()
for arg in "$@"; do
    repo=$(parse_repo "$arg")
    repos+=("$repo")
done

# 生成 GraphQL 查询
generate_query() {
    local query="query {"
    local i=1
    for repo in "${repos[@]}"; do
        local owner=$(echo "$repo" | cut -d'/' -f1)
        local name=$(echo "$repo" | cut -d'/' -f2)
        query+="
  repo$i: repository(owner: \"$owner\", name: \"$name\") {
    url
    nameWithOwner
    name
    description
    stargazerCount
    primaryLanguage { name }
    repositoryTopics(first: 20) { nodes { topic { name } } }
  }"
        ((i++))
    done
    query+="
}"
    echo "$query"
}

# 执行 GraphQL 查询
query=$(generate_query)
result=$(gh api graphql -f query="$query")

# 处理结果并生成 YAML
process_result() {
    local count=${#repos[@]}
    
    for ((i=1; i<=count; i++)); do
        local repo_data=$(echo "$result" | jq -r ".data.repo$i")
        
        # 检查仓库是否存在
        if [ "$repo_data" = "null" ]; then
            echo "⚠️  仓库 ${repos[$((i-1))]} 不存在或无法访问"
            continue
        fi
        
        # 提取字段
        local url=$(echo "$repo_data" | jq -r '.url')
        local name=$(echo "$repo_data" | jq -r '.nameWithOwner')
        local title=$(echo "$repo_data" | jq -r '.name')
        local description=$(echo "$repo_data" | jq -r '.description // ""')
        local stars=$(echo "$repo_data" | jq -r '.stargazerCount')
        local language=$(echo "$repo_data" | jq -r '.primaryLanguage.name // "Unknown"')
        local topics=$(echo "$repo_data" | jq -r '[.repositoryTopics.nodes[].topic.name] | join(", ")')
        
        # 生成 YAML
        local yaml="---
url: $url
name: $name
title: $title
description: $description
stars: $stars
language: $language
topics: [$topics]
tags: []
comment: 
---"
        
        # 追加到 Index.md
        echo "" >> "$INDEX_FILE"
        echo "$yaml" >> "$INDEX_FILE"
        
        echo "✅ 已添加: $name ($stars ⭐)"
    done
}

# 确保目录存在
mkdir -p "$(dirname "$INDEX_FILE")"

# 处理并输出
echo "📦 正在获取 ${#repos[@]} 个项目信息..."
echo "📂 收件箱: $INDEX_FILE"
echo ""
process_result
echo ""
echo "🎉 完成！共添加 ${#repos[@]} 个项目到收件箱"
