---
name: skill-linker
description: 自动扫描 Code 文件夹内的所有 SKILL.md，并将它们软链接到 ~/.codebuddy/skills/ 目录。软链接命名使用路径前缀避免重名，如 mine-code-skills-cpp-udp-module。当用户说"链接所有 skill"、"同步 skill"、"更新 skill 软链接"时使用。
---

# Skill Linker

自动将 Code 文件夹内的所有 skill 软链接到 `~/.codebuddy/skills/` 目录。

## 使用方式

执行脚本：

```bash
python3 {baseDirectory}/scripts/linker.py
```

## 功能

1. 遍历 Code 文件夹内所有包含 `SKILL.md` 的目录
2. 根据路径生成唯一名称（添加路径前缀避免重名）
3. 在 `~/.codebuddy/skills/` 创建软链接
4. 清理无效的软链接

## 命名规则

将路径转换为前缀格式：

```
Code/Mine/skills/video-learning-notes -> mine-skills-video-learning-notes
Code/Mine/tool-skills/docker -> mine-tool-skills-docker
Code/Mine/code-skills/cpp-udp-module -> mine-code-skills-cpp-udp-module
Code/Others/skills/git-helper -> others-skills-git-helper
Code/Others/mcp-skills/drawio-mcp-extension -> others-mcp-skills-drawio-mcp-extension
```

规则：
- 取 Code 之后的路径部分
- 全部小写
- 用 `-` 连接各层级

## 预期输出

```
Code directory: /workspace/changex-notes/Code
Skills directory: /root/.codebuddy/skills
--------------------------------------------------
Created: mine-code-skills-cpp-udp-module -> Mine/code-skills/cpp-udp-module
Created: mine-skills-book-learning-notes -> Mine/skills/book-learning-notes
Created: mine-skills-create-user-skill -> Mine/skills/create-user-skill
Created: mine-skills-project-learning-notes -> Mine/skills/project-learning-notes
Created: mine-skills-resource-collector -> Mine/skills/resource-collector
Created: mine-skills-skill-linker -> Mine/skills/skill-linker
Created: mine-skills-video-learning-notes -> Mine/skills/video-learning-notes
Created: mine-tool-skills-cmd -> Mine/tool-skills/cmd
Created: mine-tool-skills-docker -> Mine/tool-skills/docker
Created: others-mcp-skills-chrome-devtools-mcp -> Others/mcp-skills/chrome-devtools-mcp
Created: others-mcp-skills-drawio-mcp-extension -> Others/mcp-skills/drawio-mcp-extension
Created: others-mcp-skills-mcp-reddit -> Others/mcp-skills/mcp-reddit
Created: others-skills-git-helper -> Others/skills/git-helper
Created: others-skills-git-workflow -> Others/skills/git-workflow
Created: others-skills-web-design-guidelines -> Others/skills/web-design-guidelines
--------------------------------------------------
Done! 15 skills linked to /root/.codebuddy/skills
```

## 注意事项

1. 已存在的同名链接会被覆盖
2. 无效的软链接会自动清理
3. 只处理 `SKILL.md` 文件，忽略 `USER-SKILL.md`
4. 路径前缀确保不同分类下的同名 skill 不会冲突
