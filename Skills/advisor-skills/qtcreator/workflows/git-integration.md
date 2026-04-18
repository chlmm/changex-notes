# Git 集成

## 何时用 Qt Creator Git vs 命令行

```
选择策略
├── 日常提交/查看 diff ──→ Qt Creator 内置（轻量方便）
├── 查看 diff ──→ Qt Creator 内置（内置对比视图）
├── 分支切换 ──→ Qt Creator 内置（可视化）
├── 复杂操作（rebase、cherry-pick、bisect）───→ 命令行
├── 解决冲突 ──→ 看情况，简单冲突用 Qt Creator，复杂的用命令行
└── 批量操作/脚本化 ──→ 命令行
```

## 基本工作流

### 日常提交循环

```
1. 写代码
2. 工具 → Git → Current File → Diff（查看改动）
   或在编辑器左侧边栏看 diff 标记（红/绿/蓝）
3. 工具 → Git → Commit（或左侧 VCS 面板）
4. 选择要 Stage 的文件
5. 写提交信息
6. 提交
```

### 查看改动

```
工具 → Git → Current File
├── Diff → 查看当前文件的改动
├── Log → 查看提交历史
├── Blame → 查看每行的最后修改者
└── Revert → 撤销改动
```

### 编辑器中的 diff 标记

Qt Creator 在编辑器左侧边栏用颜色标记改动：

| 颜色 | 含义 |
|------|------|
| 🟢 绿色 | 新增的行 |
| 🔴 红色 | 删除的行 |
| 🔵 蓝色 | 修改的行 |

点击颜色标记可以查看该行的 diff。

## 分支管理

### 切换分支

```
1. 工具 → Git → Branches
2. 选择目标分支
3. Checkout
```

### 创建分支

```
1. 工具 → Git → Branches
2. 创建新分支
3. 基于当前分支或指定提交
```

### 合并分支

```
1. 切换到目标分支
2. 工具 → Git → Merge
3. 选择源分支
4. 解决冲突（如有）
```

## 解决冲突

### 冲突标记

Git 在冲突文件中插入标记：

```
<<<<<<< HEAD
当前分支的代码
=======
incoming 分支的代码
>>>>>>> feature-branch
```

### Qt Creator 中解决冲突

```
1. 工具 → Git → Merge → 出现冲突
2. 打开冲突文件
3. Qt Creator 会高亮冲突区域
4. 编辑文件，选择保留哪部分
5. 删除冲突标记（<<<<<<, =======, >>>>>>>）
6. 保存文件
7. 工具 → Git → Stage
8. 工具 → Git → Commit
```

**注意**：Qt Creator 的冲突解决界面不如 VS 的三方对比视图直观，复杂冲突建议用外部工具（如 VS Code、meld、kdiff3）。

### 配置外部 diff/merge 工具

```
工具 → 选项 → 版本控制 → Git
├── Diff 工具：设置外部 diff 工具路径
└── Merge 工具：设置外部 merge 工具路径
```

## 查看历史

### 提交历史

```
工具 → Git → Log
├── 查看完整提交历史
├── 点击提交查看改动内容
└── 支持搜索和过滤
```

### 文件历史

```
1. 右键文件 → Git → Log
2. 查看该文件的所有提交记录
3. 双击某次提交查看当时的文件内容
```

### Blame（标注）

```
1. 打开文件
2. 工具 → Git → Current File → Blame
3. 编辑器左侧显示每行的最后修改信息
```

## 忽略文件

### C++ / Qt 项目常见忽略项

```gitignore
# 构建输出
build/
debug/
release/
*.o
*.obj
*.pdb
*.exe
*.dll
*.so
*.dylib

# Qt 生成文件
moc_*.cpp
ui_*.h
qrc_*.cpp
*.pro.user

# CMake
CMakeCache.txt
CMakeFiles/
cmake_install.cmake

# IDE
.vscode/
.idea/
CMakeLists.txt.user

# macOS
.DS_Store

# 编译器
*.ilk
*.lib
*.exp
```

**注意**：`.pro.user` 文件是 Qt Creator 的用户配置，不应提交（包含本地 Kit 路径）。

## 常见问题

### 问题：Git 操作很慢

**原因**：项目文件太多或仓库太大。

**解决**：
- 确认 `.gitignore` 配置正确，不要跟踪构建输出
- 命令行执行 `git gc` 清理仓库
- 大仓库考虑 shallow clone

### 问题：Qt Creator 检测不到 Git 仓库

**解决**：
- 确认项目根目录有 `.git` 目录
- 工具 → 选项 → 版本控制 → Git → 检查 Git 路径是否正确
- 重新打开项目

### 问题：提交后想撤回

```
刚提交但还没推送？
└── 命令行：git reset --soft HEAD~1

已经推送了？
└── 只能 git revert 生成反向提交
```
