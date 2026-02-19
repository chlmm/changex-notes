---
name: docker
description: Docker 容器化工具使用指南。提供容器生命周期管理、镜像操作、网络配置、数据卷管理等完整命令参考。
execution_mode: ai
metadata:
  category: containerization
  platform: [windows, macos, linux]
  tags: [docker, container, devops, deployment]
---

# Docker 使用指南

## 概述

Docker 是一个开源的容器化平台，用于开发、交付和运行应用程序。通过容器化技术，可以将应用程序及其依赖打包在一起，确保在任何环境中都能一致运行。

## 核心概念

| 概念 | 说明 | 类比 |
|------|------|------|
| **镜像 (Image)** | 只读模板，包含运行应用所需的代码、库、环境 | 类 (Class) |
| **容器 (Container)** | 镜像的运行实例，可以被创建、启动、停止、删除 | 对象 (Object) |
| **仓库 (Registry)** | 存储和分发镜像的服务，如 Docker Hub | 应用商店 |
| **数据卷 (Volume)** | 持久化数据存储，独立于容器生命周期 | 外部硬盘 |
| **网络 (Network)** | 容器间通信和与外部连接的机制 | 虚拟网络 |

## 命令速查表

完整的 Docker CLI 命令参考：
📄 **[reference/commands.md](reference/commands.md)**

### 按需查询方法

由于命令较多，建议通过标签筛选按需查询：

```bash
# 1. 按资源类型筛选
grep "image" reference/commands.md      # 镜像相关命令
grep "container" reference/commands.md  # 容器相关命令
grep "network" reference/commands.md    # 网络相关命令
grep "volume" reference/commands.md     # 数据卷相关命令

# 2. 按操作类型筛选
grep "ls,list" reference/commands.md    # 列出/查看命令
grep "rm,delete" reference/commands.md  # 删除命令
grep "create" reference/commands.md     # 创建命令
grep "run" reference/commands.md        # 运行命令

# 3. 按使用场景筛选
grep "daily" reference/commands.md      # 日常使用命令
grep "debug" reference/commands.md      # 调试命令
grep "backup" reference/commands.md     # 备份相关命令
```

## 常用工作流

### 工作流 1：运行一个 Web 应用

```bash
# 1. 拉取镜像
docker pull nginx:latest

# 2. 运行容器（后台模式，映射端口）
docker run -d -p 8080:80 --name my-nginx nginx:latest

# 3. 查看运行状态
docker ps

# 4. 查看日志
docker logs my-nginx

# 5. 停止容器
docker stop my-nginx

# 6. 删除容器
docker rm my-nginx
```

### 工作流 2：构建自定义镜像

```bash
# 1. 创建 Dockerfile
cat > Dockerfile << 'EOF'
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
EOF

# 2. 构建镜像
docker build -t my-app:v1.0 .

# 3. 运行镜像
docker run -d -p 3000:3000 my-app:v1.0

# 4. 推送到仓库（可选）
docker tag my-app:v1.0 username/my-app:v1.0
docker push username/my-app:v1.0
```

### 工作流 3：数据持久化

```bash
# 1. 创建数据卷
docker volume create my-data

# 2. 运行容器并挂载数据卷
docker run -d -v my-data:/data --name db mysql:latest

# 3. 备份数据卷
docker run --rm -v my-data:/data -v $(pwd):/backup alpine tar czf /backup/backup.tar.gz -C /data .

# 4. 恢复数据卷
docker run --rm -v my-data:/data -v $(pwd):/backup alpine tar xzf /backup/backup.tar.gz -C /data
```

### 工作流 4：多容器应用（使用 Docker Compose）

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
  
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: secret
    volumes:
      - db-data:/var/lib/mysql

volumes:
  db-data:
```

```bash
# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止所有服务
docker-compose down
```

## 最佳实践

### 镜像优化

1. **使用多阶段构建** - 减小最终镜像体积
2. **选择合适的基础镜像** - 优先使用 Alpine 版本
3. **合理使用缓存** - 将不常变动的指令放在前面
4. **最小化层数** - 合并 RUN 命令

### 容器管理

1. **使用命名容器** - 便于管理和引用
2. **设置资源限制** - 防止容器占用过多资源
3. **健康检查** - 配置 HEALTHCHECK 指令
4. **日志管理** - 配置日志驱动和轮转

### 安全建议

1. **避免使用 root 用户** - Dockerfile 中使用 USER 指令
2. **扫描镜像漏洞** - 使用 `docker scan`
3. **最小权限原则** - 只开放必要的端口和权限
4. **定期更新镜像** - 及时更新基础镜像获取安全补丁

## 常见问题

**Q: 如何查看容器内的文件？**
```bash
docker exec -it <container> /bin/sh
# 或
docker cp <container>:<path> <local-path>
```

**Q: 如何清理未使用的资源？**
```bash
# 清理未使用的容器
docker container prune

# 清理未使用的镜像
docker image prune

# 清理未使用的数据卷
docker volume prune

# 一键清理所有
docker system prune -a
```

**Q: 容器无法访问外部网络？**
检查 Docker 网络配置，确保容器使用正确的网络模式：
```bash
docker network ls
docker inspect <container>
```

## 资源

- **官方文档**: https://docs.docker.com/
- **Docker Hub**: https://hub.docker.com/
- **Dockerfile 参考**: https://docs.docker.com/engine/reference/builder/
- **Compose 文档**: https://docs.docker.com/compose/
- **原文件位置**: `工具/softs/docker/docker_base.md`

## 相关技能

- **git-workflow** - 代码版本管理
- **network-tools** - 网络配置和调试
