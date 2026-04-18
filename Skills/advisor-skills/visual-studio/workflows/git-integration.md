# Git 集成

## 何时用 VS 内置 Git vs 命令行

```
选择策略
├─ 日常提交/拉取/推送 ──→ VS 内置 Git（可视化，方便查看改动）
├─ 复杂分支操作（rebase、cherry-pick）───→ 命令行（更灵活）
├─ 解决冲突 ──→ VS 内置（三方对比视图好用）
├─ 查看 diff ──→ VS 内置（内置对比视图）
└─ 批量操作/脚本化 ──→ 命令行
```

## 基本工作流

### 日常提交循环

```
1. 写代码
2. Git更改 → 查看改动列表
3. 逐个检查改动（双击文件打开 diff 视图）
4. Stage 要提交的文件
   ├── 全部 Stage → 点击 "+" 图标
   └── 部分 Stage → 右键文件 → Stage（或逐行 Stage）
5. 写提交信息
6. 提交
```

### 部分 Stage（交互式暂存）

VS 2022 支持行级别暂存：

1. 在 Git Changes 面板双击文件打开 diff
2. 选中要暂存的代码块
3. 右键 → Stage Selected Lines

**场景**：一个文件里有两处不相关的修改，想分开提交。

### 拉取与推送

```
拉取 ──→ Git Changes 面板 → Pull（或 同步）
推送 ──→ Git Changes 面板 → Push
同步 ──→ 同时 Pull + Push
```

## 分支管理

### 创建分支

```
1. Git Changes 面板 → 点击分支名
2. 新建分支
3. 输入分支名
4. 选择基于哪个分支创建
5. 创建后自动切换
```

### 切换分支

```
1. 点击右下角分支名
2. 选择目标分支
3. 切换

注意：如果有未提交的改动，VS 会提示：
├── Stash → 暂存改动，切完再恢复
├── 提交 → 先提交再切换
└── 丢弃 → 放弃改动（不可恢复！）
```

### 合并分支

```
1. 切换到目标分支（如 main）
2. Git → Merge From → 选择源分支
3. 解决冲突（如果有）
4. 提交合并
```

## 解决冲突

### 冲突处理流程

```
1. Pull 或 Merge 后出现冲突
2. Git Changes 面板显示冲突文件
3. 双击冲突文件 → 打开三方对比视图
   ├── 左侧：当前分支的版本
   ├── 中间：合并结果（可编辑）
   └── 右侧： incoming 版本
4. 选择接受哪一方或手动编辑
5. 标记冲突已解决
6. 提交合并结果
```

### 冲突解决策略

| 策略 | 操作 | 适合场景 |
|------|------|---------|
| 保留我的 | Accept Current | 你的改动是正确的 |
| 保留对方的 | Accept Incoming | 对方的改动是正确的 |
| 两者都保留 | 手动编辑 | 两侧改动不冲突，都要保留 |
| 手动合并 | 手动编辑 | 两侧改动有逻辑关联，需要重新整合 |

## 查看历史

### 查看文件历史

```
1. 右键文件 → View History
2. 看到该文件的所有提交记录
3. 点击某次提交查看当时的文件内容
```

### 查看行级历史（Annotate / Blame）

```
1. 打开文件
2. 右键编辑器 → Git → Annotate（或 Blame）
3. 每行前面显示最后修改该行的提交和作者
```

**用途**：快速了解某行代码是谁在什么时候改的。

## 忽略文件

### 添加 .gitignore

```
1. Git Changes 面板 → 右键未跟踪文件 → Ignore
   ├── Ignore this file → 添加到 .gitignore
   ├── Ignore this extension → 忽略所有同扩展名文件
   └── Ignore this folder → 忽略整个目录
```

### C++ 项目常见忽略项

```gitignore
# 构建输出
out/
build/
x64/
Debug/
Release/

# VS 生成文件
.vs/
*.user
*.suo
*.obj
*.pdb
*.ilk
*.lib
*.exe
*.dll

# CMake
CMakeCache.txt
CMakeFiles/
cmake_install.cmake
```

## 常见问题

### 问题：Git Changes 面板不显示改动

**原因**：VS 没有识别到 Git 仓库。

**解决**：
- 确认项目目录下有 `.git` 文件夹
- 文件 → 打开 → 文件夹 → 选择仓库根目录

### 问题：提交后想撤回

```
刚提交但还没推送？
├── Git → Undo Last Commit → 撤销提交（改动回到 Staged 状态）
└── 命令行 git reset --soft HEAD~1 效果相同

已经推送了？
└── 只能 git revert 生成反向提交（不要 force push）
```

### 问题：不小心把不该提交的文件提交了

```
1. 从 Git 跟踪中移除（但保留本地文件）：
   命令行：git rm --cached <file>
2. 添加到 .gitignore
3. 提交
```
