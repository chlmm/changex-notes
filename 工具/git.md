	### 基础提交流程

```mermaid
flowchart TD
    A[修改文件] --> B{git status}
    B -->|未跟踪/修改| C[git add <file>]
    C --> D[暂存区更新]
    D --> E[git commit -m 'msg']
    E --> F[生成新提交]
    F --> G{推送远程？}
    G -->|是| H[git push origin branch]
    G -->|否| I[保留在本地]
    H --> J[远程仓库更新]
```

### 分支协作流程
```mermaid
flowchart LR
    A[main分支] -->|git checkout -b feature| B[feature分支]
    B --> C[开发新功能]
    C --> D[git commit]
    D --> E[git push -u origin feature]
    E --> F[创建 Pull Request]
    F --> G{Code Review}
    G -->|通过| H[合并到 main]
    G -->|驳回| C
    H --> I[git checkout main<br/>git pull]
    I --> J[删除 feature 分支]
```

### 3. 冲突解决流程
```mermaid
flowchart TB
    A[git pull] --> B{冲突？}
    B -->|无冲突| C[自动合并]
    B -->|有冲突| D[标记冲突文件]
    D --> E[手动编辑解决]
    E --> F[git add <resolved-file>]
    F --> G[git commit]
    G --> H[完成合并]
```

### 4. 撤销操作流程
```mermaid
flowchart LR
    A[工作区修改] -->|未add| B[git checkout -- file<br/>丢弃修改]
    A -->|已add未commit| C[git reset HEAD file<br/>撤出暂存区]
    C --> B
    A -->|已commit| D[git reset --soft HEAD~1<br/>保留工作区]
    A -->|已commit| E[git reset --hard HEAD~1<br/>彻底丢弃]
    D & E -->|已push| F[谨慎操作！<br/>git revert commit-id]
```


#### 5. 版本回退与发布流程（标签管理）
```mermaid
flowchart TB
    A[开发完成] --> B[git tag -a v1.0 -m 'Release']
    B --> C[git push origin v1.0]
    C --> D[部署到生产环境]
    D --> E{发现严重BUG？}
    E -->|是| F[git checkout v1.0]
    F --> G[创建 hotfix 分支]
    G --> H[修复并测试]
    H --> I[git tag -a v1.0.1]
    I --> J[紧急发布]
    E -->|否| K[继续迭代]
```

#### 6. 变基协作流程（保持提交历史整洁）
```mermaid
flowchart LR
    main[main分支] -->|最新代码| A[feature分支]
    A --> B[开发中...]
    B --> C{需要同步main？}
    C -->|是| D[git fetch origin]
    D --> E[git rebase origin/main]
    E -->|解决冲突| F[git add . && git rebase --continue]
    F --> G[git push -f origin feature]
    C -->|否| B
```

#### 7. 子模块管理流程（大型项目依赖）
```mermaid
flowchart TB
    A[主项目] -->|添加子模块| B[git submodule add <repo>]
    B --> C[.gitmodules文件]
    C --> D[git commit -m 'Add submodule']
    D --> E[克隆项目时]
    E --> F[git submodule init]
    F --> G[git submodule update]
    G --> H[进入子模块目录]
    H --> I[独立开发/更新]
    I --> J[主项目提交子模块指针]
```

#### 8. 代码审查工作流（现代团队标准）
```mermaid
flowchart LR
    A[创建特性分支] --> B[提交代码]
    B --> C[推送到远程]
    C --> D[创建 Merge Request/PR]
    D --> E{自动检查}
    E -->|通过| F[分配Reviewer]
    E -->|失败| G[修复CI问题]
    F --> H[评论/建议]
    H -->|需修改| I[追加提交]
    H -->|批准| J[Rebase后合并]
    J --> K[删除特性分支]
```

#### 9. 灾难恢复流程（误操作急救）
```mermaid
flowchart TB
    A[误删分支？] -->|git branch -D feature| B[git reflog]
    B --> C[找到悬空提交]
    C --> D[git checkout -b recover <commit-id>]
    A2[误覆盖文件？] -->|git checkout -- .| E[git fsck --lost-found]
    E --> F[在 .git/lost-found 恢复]
    A3[强制推送覆盖？] -->|git push -f| G[联系管理员<br/>从远程reflog恢复]
```

---

### 四、Git 全流程全景图
```mermaid
graph TD
    A[本地开发] -->|基础操作| B(工作区/暂存区/仓库)
    A -->|分支策略| C((GitFlow/GitHub Flow))
    A -->|协作规范| D[Code Review]
    B -->|历史管理| E[标签/版本发布]
    B -->|历史修复| F[变基/合并/撤销]
    C -->|企业级| G[子模块/子树]
    D -->|自动化| H[CI/CD 集成]
    E -->|生产环境| I[紧急热修复]
    F -->|极端情况| J[数据恢复]
    
    classDef core fill:#fff7e6,stroke:#fa8c16;
    classDef collab fill:#e6fffb,stroke:#08979c;
    classDef rescue fill:#fff2f0,stroke:#f5222d;
    class B,E,F core;
    class C,D,G,H collab;
    class I,J rescue;
```


### 五、关键场景速查表
| **场景类型**       | **适用流程图**         | **核心命令/工具**                     | **使用频率** |
|--------------------|-----------------------|---------------------------------------|------------|
| 日常提交           | 基础提交流程 (1)      | `git add -p`, `git commit --amend`    | ⭐⭐⭐⭐⭐      |
| 团队协作           | 分支协作 (2) + 代码审查 (8) | `git rebase`, GitHub PR/MR           | ⭐⭐⭐⭐⭐      |
| 历史修复           | 撤销操作 (4) + 灾难恢复 (9) | `git revert`, `git reflog`           | ⭐⭐⭐⭐       |
| 版本发布           | 标签管理 (5)          | `git tag --sign`, `git push --tags`   | ⭐⭐⭐⭐       |
| 多仓库管理         | 子模块流程 (7)        | `git submodule update --remote`       | ⭐⭐         |
| 历史重写           | 变基流程 (6)          | `git rebase -i`, `git filter-repo`    | ⭐⭐⭐        |
| 紧急修复           | 热修复子流程 (5)      | `git checkout v1.0 -b hotfix`         | ⭐⭐⭐        |

### 三、关键概念速查表
| **区域**   | **作用**     | **核心命令**                            |
| -------- | ---------- | ----------------------------------- |
| **工作区**  | 实际文件操作目录   | `git status`, `git diff`            |
| **暂存区**  | 下次提交的预演区   | `git add`, `git reset HEAD`         |
| **本地仓库** | 存储完整历史记录   | `git commit`, `git log`             |
| **远程仓库** | 团队协作中心     | `git push`, `git fetch`, `git pull` |
| **分支指针** | 提交历史的轻量级指针 | `git branch`, `git checkout`        |
