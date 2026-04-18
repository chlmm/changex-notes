# 分支策略详解

## GitHub Flow（推荐简化流程）

最适合小团队、持续部署场景。

### 分支
- `main`: 始终可部署
- `feature/*`: 所有变更

### 流程
```bash
git checkout main && git pull
git checkout -b feature/add-dark-mode
# 开发、提交
git commit -m "feat(ui): add dark mode toggle"
git push -u origin feature/add-dark-mode
# 创建 PR → Review → 合并 → 部署
```

---

## Git Flow（完整发布流程）

适合定期发布、多版本维护的项目。

### 分支
- `main`: 生产就绪代码
- `develop`: 功能集成分支
- `feature/*`: 新功能
- `release/*`: 发布准备
- `hotfix/*`: 紧急生产修复

### 流程
```bash
# 功能开发
git checkout develop
git checkout -b feature/user-authentication

# 完成功能
git checkout develop
git merge feature/user-authentication
git branch -d feature/user-authentication

# 创建发布
git checkout -b release/1.2.0
# 测试、版本号更新

# 完成发布
git checkout main
git merge release/1.2.0
git tag -a v1.2.0 -m "Release 1.2.0"
git checkout develop
git merge release/1.2.0
```

---

## Trunk-Based Development

适合高 CI/CD 成熟度、快速迭代的团队。

### 核心原则
- 所有工作在 `main` 或极短生命周期的分支（<1天）
- 使用 Feature Flag 控制未完成功能
- 严格的自动化测试

---

## GitLab Flow

结合 Git Flow 和环境分支的折中方案。

### 分支
- `main`: 生产就绪
- `staging`: 预发布环境
- `production`: 生产环境
- `feature/*`: 功能分支

### 流程
```bash
git checkout -b feature/new-feature
# 开发
git checkout main
git merge feature/new-feature
git checkout staging
git merge main
# 预发布验证后
git checkout production
git merge staging
```

---

## 策略对比

| 策略 | 复杂度 | 发布周期 | 适用场景 |
|------|--------|----------|----------|
| GitHub Flow | 低 | 持续 | 小团队、持续部署 |
| Git Flow | 高 | 定期 | 多版本维护、版本发布 |
| Trunk-Based | 极低 | 持续 | 高 CI/CD 成熟度 |
| GitLab Flow | 中 | 灵活 | 多环境部署 |

## 选择建议

- **小团队 + 持续部署** → GitHub Flow
- **定期发布 + 版本管理** → Git Flow
- **高自动化 + 快速迭代** → Trunk-Based
- **多环境 + 灵活发布** → GitLab Flow
