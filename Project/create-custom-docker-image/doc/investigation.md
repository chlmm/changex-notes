# 排查过程

## 起因

需要在 Docker 中搭建 C++/Qt 开发环境，避免在宿主机上安装大量依赖污染环境。

## 排查步骤

1. **选择基础镜像** → 考虑过 Alpine（体积小）但 Qt5 生态在 Alpine 上不完善，选择 Ubuntu 22.04
2. **首次 docker build 失败** → 报错 `permission denied`，发现当前用户不在 docker 组
3. **usermod 后仍无法使用** → 已添加 docker 组但 session 未刷新，执行 `newgrp docker` 解决
4. **镜像拉取极慢** → 国内网络问题，配置中科大和网易镜像加速器
5. **构建成功但镜像体积大** → 加入 `rm -rf /var/lib/apt/lists/*` 和 `--no-install-recommends` 优化
6. **验证** → 运行容器，确认 cmake、qt、gdb 等工具均可正常使用

## 经验

- Docker 开发环境的坑主要在权限和网络，不在 Dockerfile 本身
- 先确保 docker 命令能跑，再写 Dockerfile，避免同时排查多个问题
