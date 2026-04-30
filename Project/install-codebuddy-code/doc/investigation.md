# 排查过程

## 起因

需要使用 CodeBuddy Code CLI 工具进行代码辅助。

## 排查步骤

1. **直接尝试 npm install** → 报错 `command not found: npm`，没有 Node.js 环境
2. **用系统包管理器装 Node.js** → Ubuntu apt 源中的 Node.js 版本太旧（12.x），不满足 >= 18 的要求
3. **改用 nvm 安装** → 安装 nvm → `nvm install 18` → 版本满足要求
4. **npm install -g 安装 CodeBuddy Code** → 报 EACCES 权限错误
5. **尝试 sudo npm install** → 能装上但 nvm 管理的 npm 不该用 sudo
6. **修正方式** → 重新 `nvm use 18` 确保 npm 指向正确，直接 `npm install -g` 成功
7. **验证** → `codebuddy` 命令可用

## 经验

- nvm 安装后需要 `source` 才能生效，新终端自动加载，当前终端需手动 source
- npm 全局安装遇到权限问题，优先检查 nvm 是否正确加载，不要用 sudo
