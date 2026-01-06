# 创建自定义 Docker 开发环境镜像

本文档介绍如何创建一个包含开发工具的自定义 Docker 镜像，适用于 C++/Qt 开发环境。

## 1. 创建 Dockerfile

在项目根目录创建 `Dockerfile`：

```dockerfile
# Dockerfile
FROM ubuntu:22.04

# 避免 apt 交互式提示，并清理缓存以减小镜像体积
ENV DEBIAN_FRONTEND=noninteractive

# 安装开发工具和依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        ninja-build \
        g++-11 \
        libstdc++-11-dev \
        qtbase5-dev \
        libqt5core5a \
        libqt5gui5 \
        clang-format \
        gdb \
        valgrind \
        git \
        curl \
        wget \
        vim && \
    rm -rf /var/lib/apt/lists/*

# 创建工作目录
WORKDIR /workspace

# 可选：复制项目代码（如果需要）
# COPY projects/ /workspace/projects/

# 设置默认命令
CMD ["/bin/bash"]
```

## 2. 将当前用户添加到 docker 组

```bash
sudo usermod -aG docker $USER
```

> 注意：将 `$USER` 替换为实际用户名，或直接使用 `whoami` 命令获取当前用户名。

## 3. 刷新组权限

```bash
newgrp docker
```

或者重新登录以使组权限生效。

## 4. 配置 Docker 镜像加速器（可选）

创建或修改 Docker daemon 配置文件：

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com"
  ]
}
EOF
```

## 5. 重启 Docker 服务

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## 6. 构建 Docker 镜像

在包含 Dockerfile 的目录中执行：

```bash
docker build -t big-dev-image .
```

## 7. 验证镜像构建

```bash
docker images | grep big-dev-image
```

## 8. 运行容器（示例）

```bash
# 交互式运行
docker run -it --name dev-container big-dev-image

# 挂载本地目录到容器
docker run -it -v $(pwd):/workspace/host big-dev-image
```

## 注意事项

1. **Dockerfile 语法**：确保反斜杠续行符前没有空格
2. **包管理**：Ubuntu 22.04 上某些 Qt5 包可能需要额外配置
3. **权限**：添加用户到 docker 组后需要重新登录或使用 `newgrp` 命令
4. **镜像大小**：通过清理 apt 缓存可以减小镜像体积
5. **安全**：将用户添加到 docker 组会赋予该用户 root 级别权限，请谨慎操作