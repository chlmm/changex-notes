# 操作步骤

## 1. 将当前用户添加到 docker 组

```bash
sudo usermod -aG docker $USER
```

> 注意：将 `$USER` 替换为实际用户名，或直接使用 `whoami` 命令获取当前用户名。

## 2. 刷新组权限

```bash
newgrp docker
```

或者重新登录以使组权限生效。

## 3. 配置 Docker 镜像加速器（可选）

将 `resources/daemon.json` 复制到 `/etc/docker/daemon.json`：

```bash
sudo mkdir -p /etc/docker
sudo cp resources/daemon.json /etc/docker/daemon.json
```

## 4. 重启 Docker 服务

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## 5. 构建 Docker 镜像

在包含 Dockerfile 的目录中执行：

```bash
docker build -f resources/Dockerfile -t big-dev-image .
```

## 6. 验证镜像构建

```bash
docker images | grep big-dev-image
```

## 7. 运行容器（示例）

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
