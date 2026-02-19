#!/usr/bin/env python3
"""
Skill Linker - 自动将 Code 文件夹内的所有 skill 软链接到 ~/.codebuddy/skills/
"""

import os
import subprocess
from pathlib import Path


def get_code_dir():
    """获取 Code 目录路径"""
    # 脚本所在目录: scripts/linker.py
    script_dir = Path(__file__).parent
    # Code 目录：script_dir 是 Code/Mine/skills/skill-linker/scripts，向上5级到 Code
    # scripts -> skill-linker -> skills -> Mine -> Code
    code_dir = script_dir.parent.parent.parent.parent
    return code_dir


def get_skills_dir():
    """获取 skills 目标目录"""
    return Path.home() / ".codebuddy" / "skills"


def find_all_skills(code_dir: Path):
    """查找所有包含 SKILL.md 的目录"""
    skills = []
    for skill_file in code_dir.rglob("SKILL.md"):
        skill_dir = skill_file.parent
        # 计算相对路径
        rel_path = skill_dir.relative_to(code_dir)
        # 生成链接名称：路径各部分用 - 连接，全部小写
        link_name = str(rel_path).replace("/", "-").lower()
        skills.append({
            "skill_dir": skill_dir,
            "rel_path": rel_path,
            "link_name": link_name
        })
    return skills


def create_symlink(skill_dir: Path, link_path: Path):
    """创建软链接"""
    # 删除已存在的链接
    if link_path.exists() or link_path.is_symlink():
        link_path.unlink()

    # 创建新链接
    link_path.symlink_to(skill_dir)
    return True


def clean_broken_links(skills_dir: Path):
    """清理无效的软链接"""
    if not skills_dir.exists():
        return

    for item in skills_dir.iterdir():
        if item.is_symlink() and not item.exists():
            item.unlink()
            print(f"Cleaned broken link: {item.name}")


def main():
    code_dir = get_code_dir()
    skills_dir = get_skills_dir()

    print(f"Code directory: {code_dir}")
    print(f"Skills directory: {skills_dir}")
    print("-" * 50)

    # 确保目标目录存在
    skills_dir.mkdir(parents=True, exist_ok=True)

    # 清理现有链接
    for item in skills_dir.iterdir():
        if item.is_symlink():
            item.unlink()

    # 查找所有 skill
    skills = find_all_skills(code_dir)

    # 创建软链接
    for skill in sorted(skills, key=lambda x: x["link_name"]):
        link_path = skills_dir / skill["link_name"]
        try:
            create_symlink(skill["skill_dir"], link_path)
            print(f"Created: {skill['link_name']} -> {skill['rel_path']}")
        except Exception as e:
            print(f"Failed: {skill['link_name']} - {e}")

    # 清理无效链接
    clean_broken_links(skills_dir)

    print("-" * 50)
    print(f"Done! {len(skills)} skills linked to {skills_dir}")


if __name__ == "__main__":
    main()
