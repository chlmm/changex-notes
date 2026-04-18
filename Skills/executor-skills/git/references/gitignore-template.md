# 常用 .gitignore 模板

## 编译文件
```
*.pyc
*.pyo
__pycache__/
*.o
*.so
*.a
*.dll
*.exe
*.out
```

## 构建目录
```
build/
dist/
target/
bin/
obj/
```

## IDE 和编辑器文件
```
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store
*.sublime-*
*.sublime-workspace
```

## 日志
```
*.log
logs/
```

## 环境文件
```
.env
.env.local
.env.*.local
```

## 依赖
```
node_modules/
vendor/
Gemfile.lock
package-lock.json
yarn.lock
```

## 临时文件
```
tmp/
temp/
*.tmp
```

## 系统文件
```
Thumbs.db
.DS_Store
*.desktop
```

## 项目特定（按需取消注释）
```
# config/secrets.yml
# database.sqlite
# .coverage
# *.keystore
# *.jks
```

## 快速生成

访问 [gitignore.io](https://www.toptal.com/developers/gitignore) 可根据技术栈自动生成 `.gitignore` 文件。
