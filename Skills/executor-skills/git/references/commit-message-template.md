# Git Commit Message 模板

## Conventional Commits 格式

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## 类型

- **feat**: 新功能
- **fix**: Bug 修复
- **docs**: 文档变更
- **style**: 格式调整（不影响逻辑）
- **refactor**: 重构（非新功能、非修复）
- **perf**: 性能优化
- **test**: 测试相关
- **chore**: 构建/工具/依赖
- **ci**: CI/CD 变更

## 示例

### 简单 feat
```
feat: add user authentication
```

### 带 scope
```
feat(auth): implement OAuth2 login
```

### Fix
```
fix: resolve memory leak in image processing
```

### 带 body
```
feat(parser): add support for JSON5 format

- Add custom parser for JSON5 syntax
- Handle trailing commas
- Support unquoted property names
- Add comprehensive test coverage
```

### Breaking change
```
feat(api): remove deprecated user endpoint

BREAKING CHANGE: The /api/v1/users endpoint has been removed.
Use /api/v2/users instead.
```

### 带 footer
```
fix: correct API response format

Closes #123
```

## 最佳实践

1. **使用祈使语气**："Add feature" 而非 "Added feature"
2. **首行不超过 50 字符**
3. **首字母大写**，末尾不加句号
4. **Subject 与 Body 之间空一行**
5. **Body 每行不超过 72 字符**
6. **Body 解释 what 和 why**，而非 how

## 模板

```
<type>(<scope>): <subject>

<body>

<footer>
```
