#!/usr/bin/env python3
"""
Steam Game Collector - 获取 Steam 游戏信息并生成 YAML 收藏记录
用法: python3 steam-collect.py "游戏名称" [游戏名称2] ...
      python3 steam-collect.py <appid>
"""

import sys
import json
import subprocess
import re
from pathlib import Path

# 配置
NOTES_ROOT = Path("/workspace/changex-notes")
INDEX_FILE = NOTES_ROOT / "Index/Games/Index.md"

# Steam API URLs
STEAM_SEARCH_URL = "https://store.steampowered.com/api/storesearch/"
STEAM_DETAILS_URL = "https://store.steampowered.com/api/appdetails"


def http_get(url: str) -> dict:
    """使用 curl 发送 HTTP GET 请求"""
    result = subprocess.run(
        ["curl", "-s", "-L", "-H", "User-Agent: Mozilla/5.0", url],
        capture_output=True,
        text=True,
        timeout=15
    )
    return json.loads(result.stdout)


def search_game(name: str) -> tuple[int, str] | None:
    """搜索游戏，返回 (appid, name)"""
    try:
        # 中文搜索
        url = f"{STEAM_SEARCH_URL}?term={name}&l=schinese&cc=CN"
        data = http_get(url)
        
        if data.get("items") and len(data["items"]) > 0:
            item = data["items"][0]
            return (item["id"], item["name"])
        
        # 英文搜索
        url = f"{STEAM_SEARCH_URL}?term={name}&l=english"
        data = http_get(url)
        if data.get("items") and len(data["items"]) > 0:
            item = data["items"][0]
            return (item["id"], item["name"])
            
    except Exception as e:
        print(f"  ⚠️  搜索失败: {e}")
    
    return None


def get_game_details(appid: int) -> dict | None:
    """获取游戏详情"""
    try:
        url = f"{STEAM_DETAILS_URL}?appids={appid}&l=schinese"
        data = http_get(url)
        
        app_data = data.get(str(appid), {})
        if app_data.get("success") and app_data.get("data"):
            return app_data["data"]
            
    except Exception as e:
        print(f"  ⚠️  获取详情失败: {e}")
    
    return None


def extract_year(release_date: str) -> str:
    """从发行日期提取年份"""
    if not release_date:
        return ""
    match = re.search(r"\d{4}", release_date)
    return match.group(0) if match else ""


def extract_platforms(platforms: dict) -> str:
    """提取平台列表"""
    result = []
    if platforms.get("windows"):
        result.append("PC")
    if platforms.get("mac"):
        result.append("Mac")
    if platforms.get("linux"):
        result.append("Linux")
    return ", ".join(result) if result else "PC"


def generate_yaml(game: dict) -> str:
    """生成 YAML 格式"""
    details = game["details"]
    
    title = details.get("name", "")
    year = extract_year(details.get("release_date", {}).get("date", ""))
    developer = details.get("developers", ["未知"])[0] if details.get("developers") else "未知"
    platform = extract_platforms(details.get("platforms", {}))
    genres = [g["description"] for g in details.get("genres", [])]
    
    yaml_content = f"""---
title: {title}
year: {year}
developer: {developer}
platform: {platform}
genres: {genres}
rating: 0
status: 想玩
tags: []
comment: 
---"""
    
    return yaml_content


def append_to_index(yaml_content: str):
    """追加到收件箱"""
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(INDEX_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + yaml_content + "\n")


def process_game(input_str: str) -> bool:
    """处理单个游戏"""
    print(f"  🔍 搜索: {input_str}")
    
    # 判断是 AppID 还是游戏名
    if input_str.isdigit():
        appid = int(input_str)
        name = input_str
    else:
        result = search_game(input_str)
        if not result:
            print(f"  ❌ 未找到游戏: {input_str}")
            return False
        appid, name = result
    
    # 获取详情
    details = get_game_details(appid)
    if not details:
        print(f"  ❌ 获取详情失败: {name}")
        return False
    
    # 生成 YAML
    yaml_content = generate_yaml({"details": details})
    
    # 追加到收件箱
    append_to_index(yaml_content)
    
    print(f"  ✅ 已添加: {details.get('name', name)}")
    return True


def main():
    if len(sys.argv) < 2:
        print("用法: python3 steam-collect.py <游戏名称或AppID> [游戏名称2] ...")
        print("\n示例:")
        print('  python3 steam-collect.py "艾尔登法环"')
        print("  python3 steam-collect.py 1245620")
        print('  python3 steam-collect.py "艾尔登法环" "黑神话：悟空"')
        sys.exit(1)
    
    games = sys.argv[1:]
    
    print(f"🎮 正在获取 {len(games)} 个游戏信息...")
    print(f"📂 收件箱: {INDEX_FILE}")
    print()
    
    success = 0
    for game in games:
        if process_game(game):
            success += 1
    
    print()
    print(f"🎉 完成！成功添加 {success}/{len(games)} 个游戏到收件箱")


if __name__ == "__main__":
    main()
