# 决策树：创建自定义 Docker 开发环境

```
需要搭建 Docker 开发环境
│
├─ 选择基础镜像
│   ├─ 需要 GUI？→ ubuntu:22.04 + 桌面环境
│   └─ 纯命令行？→ ubuntu:22.04（推荐，体积小）
│
├─ 权限问题：当前用户无法执行 docker
│   ├─ 用户是否在 docker 组？→ sudo usermod -aG docker $USER
│   └─ 已添加但仍无法使用？→ newgrp docker 或重新登录
│
├─ 网络问题：镜像拉取慢
│   ├─ 国内环境？→ 配置镜像加速器
│   └─ 海外环境？→ 无需配置
│
└─ 镜像体积优化
    ├─ 清理 apt 缓存 → rm -rf /var/lib/apt/lists/*
    └─ 使用 --no-install-recommends 减少非必要包
```

## 关键判断点

1. **基础镜像选 LTS**：Ubuntu 22.04 稳定且包生态完整
2. **权限必须处理**：usermod 后必须 newgrp 或重新登录才能生效
3. **国内必配加速器**：否则 docker build 可能超时失败
