# 决策树：安装 CodeBuddy Code

```
需要安装 CodeBuddy Code CLI
│
├─ 是否已安装 Node.js？
│   ├─ 已安装且 >= 18 → 直接 npm install -g
│   ├─ 已安装但 < 18 → 需要升级 Node.js
│   └─ 未安装 → 继续 ↓
│
├─ Node.js 版本管理方式？
│   ├─ nvm（推荐）→ nvm install 18
│   ├─ n → n 18
│   └─ 系统包管理器 → 可能版本不够新
│
└─ npm 全局安装权限问题？
    ├─ 报 EACCES → 不要用 sudo npm install，应修复 npm 全局目录权限
    └─ 正常 → 安装完成
```

## 关键判断点

1. **Node.js 版本必须 >= 18**：CodeBuddy Code 要求 18+
2. **推荐 nvm**：不影响系统 Node.js 版本，切换方便
3. **不要 sudo npm install**：虽然能装上但会引发权限问题
