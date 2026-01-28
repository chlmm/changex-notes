# Git Commit Message Template

## Conventional Commits Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect code meaning (formatting, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvement
- **test**: Adding or updating tests
- **chore**: Build process or auxiliary tool changes
- **ci**: CI/CD configuration changes

## Examples

### Simple feat
```
feat: add user authentication
```

### With scope
```
feat(auth): implement OAuth2 login
```

### Fix
```
fix: resolve memory leak in image processing
```

### With body
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

### With footer
```
fix: correct API response format

Closes #123
```

## Commit Message Best Practices

1. **Use imperative mood**: "Add feature" not "Added feature"
2. **Limit subject line**: Max 50 characters
3. **Capitalize subject line**: First letter uppercase
4. **No period at end**: Subject line shouldn't end with punctuation
5. **Separate body**: Blank line between subject and body
6. **Wrap body**: 72 characters per line
7. **Explain why**: Body should explain what and why, not how

## Template for Copying

```
<type>(<scope>): <subject>

<body>

<footer>
```
