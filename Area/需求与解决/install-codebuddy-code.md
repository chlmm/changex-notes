# 安装 CodeBuddy Code

## 安装 NVM (Node Version Manager)

```bash
# 使用curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# 或使用wget
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

## 重新加载配置

根据你使用的 shell，重新加载配置文件：

```bash
# 如果使用 bash
source ~/.bashrc

# 如果使用 zsh
source ~/.zshrc
```

## 安装 Node.js 18

```bash
nvm install 18
```

## 切换到 Node.js 18 并设为默认版本

```bash
nvm use 18
nvm alias default 18
```

## 安装 CodeBuddy Code

```bash
npm install -g @tencent-ai/codebuddy-code
```

## 验证安装

检查 Node.js 版本和 CodeBuddy Code 是否安装成功：

```bash
node -v
codebuddy
```
