# Qt Creator 快捷键速查

> 按意图分类。工作流文件中只写操作名，需要查键时搜本文件。
> 操作名是规范化约定，workflow 文件和本文件必须使用相同的操作名。
> 跨平台差异：Win/Linux 和 macOS 快捷键不同时分别标注。

## 我想跳转...

| 操作名 | Win/Linux | macOS | 说明 |
|--------|-----------|-------|------|
| 跳转定义 | F2 | F2 | 跳到符号的定义处 |
| 跳转声明 | Ctrl+Shift+F2 | Cmd+Shift+F2 | 跳到符号的声明处 |
| 切换h/cpp | F4 | F4 | 在头文件和源文件间切换 |
| 查找引用 | Ctrl+Shift+U | Cmd+Shift+U | 列出所有引用该符号的位置 |
| 跟进光标 | F2 或 Ctrl+Click | F2 或 Cmd+Click | 根据上下文跳转（声明/定义/Include） |
| 转到行 | Ctrl+L | Cmd+L | 跳转到指定行号 |
| 转到符号 | Ctrl+K | Cmd+K | 按符号名搜索并跳转 |
| 后退 | Alt+Left | Cmd+[ | 导航回上一个位置 |
| 前进 | Alt+Right | Cmd+] | 导航到下一个位置 |
| 在文件中切换 | Ctrl+Tab | Cmd+Tab | 切换最近打开的文件 |

## 我想搜索...

| 操作名 | Win/Linux | macOS | 说明 |
|--------|-----------|-------|------|
| 全局搜索 | Ctrl+Shift+F | Cmd+Shift+F | 在整个项目中搜索文本 |
| 快速搜索 | Ctrl+F | Cmd+F | 在当前文件中搜索 |
| 替换 | Ctrl+H | Cmd+H | 当前文件中查找替换 |
| 增量搜索 | Ctrl+I | Cmd+I | 输入即搜索 |
| 搜索命令 | Ctrl+Shift+P | Cmd+Shift+P | 搜索并执行命令（Locator） |

## 我想编辑...

| 操作名 | Win/Linux | macOS | 说明 |
|--------|-----------|-------|------|
| 格式化文档 | Ctrl+Shift+I | Cmd+Shift+I | 使用 ClangFormat 格式化 |
| 注释 | Ctrl+/ | Cmd+/ | 注释/取消注释选中行 |
| 删除行 | Ctrl+Shift+Del | Cmd+Shift+Del | 删除当前行 |
| 复制行 | Ctrl+Ins | Cmd+Ins | 复制当前行 |
| 上移行 | Ctrl+Shift+Up | Cmd+Shift+Up | 将当前行上移 |
| 下移行 | Ctrl+Shift+Down | Cmd+Shift+Down | 将当前行下移 |
| 自动补全 | Ctrl+Space | Cmd+Space | 触发代码补全 |
| 快速修复 | Alt+Enter | Alt+Enter | 打开快速修复/重构建议 |
| 展开折叠 | Ctrl+Shift+C | Cmd+Shift+C | 折叠/展开当前代码块 |
| 全部折叠 | Ctrl+Shift+< | Cmd+Shift+< | 折叠所有代码块 |
| 全部展开 | Ctrl+Shift+> | Cmd+Shift+> | 展开所有代码块 |
| 书签切换 | Ctrl+M | Cmd+M | 在当前行添加/移除书签 |
| 书签下一 | Ctrl+. | Cmd+. | 跳转到下一个书签 |
| 书签上一 | Ctrl+, | Cmd+, | 跳转到上一个书签 |
| 分屏（左右） | Ctrl+E, 2 | Cmd+E, 2 | 左右分屏 |
| 分屏（上下） | Ctrl+E, 3 | Cmd+E, 3 | 上下分屏 |
| 取消分屏 | Ctrl+E, 1 | Cmd+E, 1 | 取消分屏 |

## 我想调试...

| 操作名 | Win/Linux | macOS | 说明 |
|--------|-----------|-------|------|
| 开始调试 | F5 | F5 | 启动调试 |
| 开始不调试 | Ctrl+R | Cmd+R | 运行不附加调试器 |
| 切换断点 | F9 | F9 | 在当前行添加/移除断点 |
| 逐过程 | F10 | F10 | 单步执行，不进入函数内部 |
| 逐语句 | F11 | F11 | 单步执行，进入函数内部 |
| 跳出 | Shift+F11 | Shift+F11 | 执行到当前函数返回 |
| 运行到光标 | Ctrl+F10 | Cmd+F10 | 运行到光标所在行 |
| 重新启动 | Ctrl+Shift+F5 | Cmd+Shift+F5 | 重新启动调试 |
| 停止调试 | Shift+F5 | Shift+F5 | 终止调试 |

## 我想查看窗口...

| 操作名 | Win/Linux | macOS | 说明 |
|--------|-----------|-------|------|
| 项目面板 | Ctrl+Shift+X | Cmd+Shift+X | 切换项目树 |
| 文件系统 | Ctrl+Shift+Y | Cmd+Shift+Y | 文件系统浏览器 |
| 打开文档 | Ctrl+Shift+O | Cmd+Shift+O | 已打开文档列表 |
| 输出面板 | Alt+数字键 | Cmd+数字键 | 切换各输出面板 |
| 问题面板 | Ctrl+Shift+M | Cmd+Shift+M | 编译错误和警告列表 |
| 搜索结果 | Ctrl+Shift+R | Cmd+Shift+R | 搜索结果面板 |
| 大纲 | Ctrl+Shift+T | Cmd+Shift+T | 当前文件的符号大纲 |
| Locator | Ctrl+K | Cmd+K | 全能搜索框 |

## 我想构建...

| 操作名 | Win/Linux | macOS | 说明 |
|--------|-----------|-------|------|
| 构建项目 | Ctrl+B | Cmd+B | 构建当前项目 |
| 构建全部 | Ctrl+Shift+B | Cmd+Shift+B | 构建所有项目 |
| 重新构建 | Ctrl+Shift+R | Cmd+Shift+R | 清理后重新构建 |
| 运行 | Ctrl+R | Cmd+R | 运行当前项目 |

## 我想重构...

| 操作名 | Win/Linux | macOS | 说明 |
|--------|-----------|-------|------|
| 重命名 | Ctrl+Shift+R | Cmd+Shift+R | 重命名符号（右键菜单中更可靠） |
| 提取函数 | — | — | 右键 → Refactor → Extract Function |
| 提取变量 | — | — | 右键 → Refactor → Extract Variable |
| 添加getter/setter | — | — | 右键 → Refactor → Generate Getter/Setter |
| 添加信号槽 | — | — | 右键 → Refactor → Connect Signal/Slot |

## Locator 命令速查

Locator（Ctrl+K）是 Qt Creator 的命令面板，支持前缀过滤：

| 前缀 | 用途 | 示例 |
|------|------|------|
| 无前缀 | 搜索文件名 | `main.cpp` |
| `:` | 搜索类/函数/变量 | `:MainWindow` |
| `.` | 搜索当前文件中的符号 | `.setupUi` |
| `!` | 运行命令 | `!Build` |
| `?` | 打开帮助文档 | `?QWidget` |
| `l` | 搜索行号 | `l42` |
| `m` | 搜索书签 | `m` |
