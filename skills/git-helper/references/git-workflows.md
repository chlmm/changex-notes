# Git Workflow Guide

## Git Flow

Git Flow is a branching model designed for projects with scheduled releases.

### Main Branches
- **main/master**: Production-ready code
- **develop**: Integration branch for features

### Supporting Branches
- **feature**: New features (merged into develop)
- **release**: Release preparation (merged into main and develop)
- **hotfix**: Production bug fixes (merged into main and develop)

### Git Flow Commands

**Initialize Git Flow:**
```bash
git flow init
```

**Start a feature:**
```bash
git flow feature start feature-name
```

**Finish a feature:**
```bash
git flow feature finish feature-name
```

**Start a release:**
```bash
git flow release start 1.0.0
```

**Finish a release:**
```bash
git flow release finish 1.0.0
```

**Start a hotfix:**
```bash
git flow hotfix start hotfix-name
```

**Finish a hotfix:**
```bash
git flow hotfix finish hotfix-name
```

## GitHub Flow

GitHub Flow is a simpler workflow ideal for continuous deployment.

### Workflow Steps
1. Create a branch from `main`
2. Make commits to the branch
3. Push to GitHub
4. Open a Pull Request
5. Discuss and review code
6. Deploy to production (optional)
7. Merge the PR

### Example
```bash
git checkout main
git pull
git checkout -b new-feature
# Make changes
git add .
git commit -m "Add new feature"
git push -u origin new-feature
# Create PR on GitHub
# After review and merge:
git checkout main
git pull
git branch -d new-feature
```

## Trunk-Based Development

All developers work on a single branch (`main`) with very short-lived branches.

### Principles
- Feature flags for incomplete features
- Small, frequent commits
- Continuous integration is essential
- No long-lived branches

### When to Use
- Teams practicing continuous deployment
- Projects with fast release cycles
- High automation and CI/CD maturity

## GitLab Flow

GitLab Flow combines Git Flow with feature-driven development and environment branches.

### Branches
- `main`: Production-ready code
- `master`: Production (alternative)
- Environment branches: `staging`, `pre-production`
- Feature branches

### Example Flow
```bash
git checkout -b feature/new-feature
# Work on feature
git checkout main
git merge feature/new-feature
git checkout staging
git merge main
# After staging verification
git checkout production
git merge staging
```

## Branching Strategies Comparison

| Strategy | Complexity | Release Cycles | Best For |
|----------|-----------|----------------|----------|
| GitHub Flow | Low | Continuous | Small teams, continuous deployment |
| Git Flow | High | Scheduled | Projects with versioned releases |
| Trunk-Based | Very Low | Continuous | High-maturity teams, fast releases |
| GitLab Flow | Medium | Flexible | Multi-environment deployments |

## Choosing the Right Workflow

**Use GitHub Flow when:**
- Small team
- Continuous deployment
- Simple release process

**Use Git Flow when:**
- Scheduled releases
- Multiple release versions maintained
- Need for release management

**Use Trunk-Based when:**
- High CI/CD maturity
- Feature flag system available
- Fast iteration needed

**Use GitLab Flow when:**
- Multiple deployment environments
- Need for environment-specific code
- Flexible branching requirements
