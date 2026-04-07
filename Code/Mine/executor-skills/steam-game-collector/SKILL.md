---
name: steam-game-collector
description: 从 Steam 获取游戏信息，生成 YAML 格式的游戏收藏记录。当用户说"收藏 Steam 游戏"、"获取游戏信息"、"添加游戏"时使用。
type: tool
execution_mode: executor
---

# Steam Game Collector

使用 Steam API 获取游戏信息，生成符合 Notes 系统格式的 YAML 收藏记录。

## 使用方式

```bash
# 通过游戏名称搜索并收藏
python3 {baseDirectory}/scripts/steam-collect.py "艾尔登法环"

# 通过 Steam AppID 收藏
python3 {baseDirectory}/scripts/steam-collect.py 1245620

# 批量收藏
python3 {baseDirectory}/scripts/steam-collect.py "艾尔登法环" "黑神话：悟空" "塞尔达传说"
```

## 输出格式

```yaml
---
title: 艾尔登法环
year: 2022
developer: FromSoftware, Inc.
platform: PC
genres: [动作, RPG]
rating: 0
status: 想玩
tags: []
comment: 
---
```

## 字段说明

| 字段 | 来源 | 说明 |
|------|------|------|
| `title` | Steam API | 游戏名称 |
| `year` | Steam API | 发行年份 |
| `developer` | Steam API | 开发商 |
| `platform` | Steam API | 平台 (PC/Mac/Linux) |
| `genres` | Steam API | 游戏类型 |
| `rating` | 用户填写 | 个人评分 (0-10) |
| `status` | 用户填写 | 游玩状态 |
| `tags` | 用户填写 | 个人标签 |
| `comment` | 用户填写 | 个人备注 |

## 技术方案

使用 **Steam Store API**：

| API | 说明 | 需要 Key |
|-----|------|----------|
| `appdetails` | 获取游戏详情 | ❌ 不需要 |
| `storesearch` | 搜索游戏 | ❌ 不需要 |

## 工作流程（收件箱模式）

### 1. 快速收藏
用户提供游戏名称 → AI 执行脚本 → 自动追加到 `Index.md` 收件箱

### 2. 定期整理
用户说"整理游戏收件箱" → AI 分析游戏 → 补充评分、状态、备注 → 移动到收藏文件

## 存储位置

```
changex-notes/Index/Games/
├── Index.md        # 收件箱（待整理游戏）
└── 游戏收藏.md     # 已整理的游戏收藏
```

## 使用示例

### 快速收藏

用户说：收藏这个游戏 艾尔登法环

AI 执行：
```bash
python3 {baseDirectory}/scripts/steam-collect.py "艾尔登法环"
```

### 批量收藏

用户说：帮我收藏这几个游戏：艾尔登法环、黑神话悟空

AI 执行：
```bash
python3 {baseDirectory}/scripts/steam-collect.py "艾尔登法环" "黑神话：悟空"
```

### 整理收件箱

用户说：整理游戏收件箱

AI 会：
1. 读取 `Index.md` 中待整理的游戏
2. 询问用户每个游戏的评分、状态、备注
3. 更新后移动到 `游戏收藏.md`

## 注意事项

1. 仅支持 Steam 平台游戏
2. 非 Steam 游戏（如 Nintendo 独占）需要手动添加
3. 中英文游戏名都支持搜索
