#!/bin/bash
# 一键安装 CodeBuddy Code（NVM + Node.js 18 + CodeBuddy Code）

set -e

echo "=== 1. 安装 NVM ==="
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

echo "=== 2. 加载 NVM ==="
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

echo "=== 3. 安装 Node.js 18 ==="
nvm install 18
nvm use 18
nvm alias default 18

echo "=== 4. 安装 CodeBuddy Code ==="
npm install -g @tencent-ai/codebuddy-code

echo "=== 5. 验证安装 ==="
node -v
echo "CodeBuddy Code 安装完成！"
