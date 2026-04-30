# 决策树：.gitignore 不生效

```
.gitignore 添加了规则但文件仍被跟踪
│
├─ 文件是否已被 git add 过？
│   ├─ 是 → git rm --cached 移除跟踪，再提交
│   └─ 否 → 继续 ↓
│
├─ .gitignore 规则语法是否正确？
│   ├─ 检查路径是否相对于仓库根目录
│   ├─ 检查通配符是否正确（*.log vs /**/*.log）
│   └─ 语法正确 → 继续 ↓
│
└─ .gitignore 文件位置是否正确？
    ├─ 应在仓库根目录（或对应子目录）
    └─ 位置正确 → 检查是否有多个 .gitignore 冲突
```

## 关键判断点

1. **先查跟踪状态**：`git ls-files <path>` 比看 .gitignore 更可靠
2. **--cached 是安全操作**：不会删除本地文件，只取消 Git 跟踪
3. **预防优于修复**：项目初始化时就应配置 .gitignore
