# 排查过程

## 现象

在 changex-notes 项目中添加了 `.gitignore` 并写入 `.trash/*`，push 后发现 GitHub 上 .trash 目录仍然存在。

## 排查步骤

1. **怀疑 .gitignore 语法问题** → 检查语法，` .trash/*` 写法正确，排除
2. **怀疑 .gitignore 未被提交** → `git status` 显示 .gitignore 已提交，排除
3. **想到文件可能已被跟踪** → 执行 `git ls-files .trash`，发现 .trash 下的文件确实在跟踪列表中
4. **定位原因**：.trash 目录在添加 .gitignore 之前就已经被 `git add` 过了，.gitignore 只对未跟踪文件生效
5. **搜索解决方案** → 查到 `git rm --cached` 可以移除跟踪但保留本地文件
6. **执行修复** → `git rm -r --cached .trash` → `git commit` → `git push`
7. **验证** → GitHub 上 .trash 目录消失

## 经验

- 以后新项目第一步就创建 .gitignore，避免后加导致的问题
- `git ls-files` 是排查 .gitignore 不生效的首选命令
