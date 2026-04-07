---
type: reference
category: docker
title: Docker 命令速查表
description: 完整的 Docker CLI 命令参考，带标签分类便于筛选查询
---

# Docker 命令速查表

## 使用说明

本表格包含第四列"标签"，可通过 grep/sed 等工具按需筛选：

```bash
# 按分类筛选（如所有镜像管理命令）
grep "镜像管理" commands.md

# 按标签筛选（如所有删除相关命令）
grep "rm,delete" commands.md

# 按关键词搜索
grep "后台运行" commands.md
```

## 标签说明

| 标签 | 含义 |
|------|------|
| `image` | 镜像操作 |
| `container` | 容器操作 |
| `network` | 网络操作 |
| `volume` | 数据卷操作 |
| `plugin` | 插件操作 |
| `ls,list` | 列出/查看 |
| `create` | 创建 |
| `rm,delete` | 删除 |
| `run` | 运行 |
| `exec` | 执行 |
| `daily` | 日常使用 |
| `debug` | 调试用 |
| `backup` | 备份相关 |

---

## 镜像管理命令

| 分类 | 命令 | 说明 | 标签 |
|------|------|------|------|
| 镜像管理 | `docker image ls` | 查看镜像 | image,ls,list,daily |
| 镜像管理 | `docker images` | 查看镜像（简写） | image,ls,list,daily |
| 镜像管理 | `docker search [image]` | 检索镜像 | image,search |
| 镜像管理 | `docker search nginx` | 示例：检索 nginx 镜像 | image,search,example |
| 镜像管理 | `docker pull [image]` | 拉取镜像 | image,pull,download,daily |
| 镜像管理 | `docker push [image]` | 上传镜像到仓库 | image,push,upload |
| 镜像管理 | `docker push geekhour/hello-docker:latest` | 示例：上传指定镜像 | image,push,example |
| 镜像管理 | `docker save [image] -o FILE` | 保存镜像为 tar 文件 | image,save,export,backup |
| 镜像管理 | `docker save [image] > FILE` | 保存镜像（重定向方式） | image,save,export,backup |
| 镜像管理 | `docker load -i FILE` | 导入镜像 | image,load,import,backup |
| 镜像管理 | `docker history [image]` | 查看镜像构建历史 | image,history,debug |
| 镜像管理 | `docker rmi [image]` | 删除镜像 | image,rm,delete |
| 镜像管理 | `docker image rm [image]` | 删除镜像（完整写法） | image,rm,delete |
| 镜像管理 | `docker image prune` | 删除未使用的镜像（清理） | image,prune,cleanup |
| 镜像管理 | `docker import [URL/FILE]` | 从文件系统导入为镜像 | image,import |
| 镜像管理 | `docker commit [container] [image]` | 从容器创建镜像 | image,commit,create |

---

## 容器管理命令

| 分类 | 命令 | 说明 | 标签 |
|------|------|------|------|
| 容器管理 | `docker create [image]` | 创建容器（不运行） | container,create |
| 容器管理 | `docker run [image]` | 创建并运行容器 | container,run,create,daily |
| 容器管理 | `docker start [container]` | 启动已存在的容器 | container,start |
| 容器管理 | `docker stop [container]` | 停止运行中的容器 | container,stop,daily |
| 容器管理 | `docker restart [container]` | 重启容器 | container,restart |
| 容器管理 | `docker ps` | 列出运行中的容器 | container,ls,list,status,daily |
| 容器管理 | `docker ps -a` | 列出所有容器（含停止的） | container,ls,list,status,daily |
| 容器管理 | `docker container ls` | 列出容器（完整写法） | container,ls,list |
| 容器管理 | `docker container ls -a` | 列出所有容器（完整写法） | container,ls,list |
| 容器管理 | `docker exec -it [container] bash` | 进入容器执行交互式命令 | container,exec,enter,debug,daily |
| 容器管理 | `docker attach [container]` | 附加到运行中的容器 | container,attach,debug |
| 容器管理 | `docker export [container] -o FILE` | 导出容器为 tar 文件 | container,export,backup |
| 容器管理 | `docker import FILE` | 导入容器快照 | container,import,backup |
| 容器管理 | `docker logs [container]` | 查看容器日志 | container,logs,debug,daily |
| 容器管理 | `docker rm [container]` | 删除容器 | container,rm,delete |
| 容器管理 | `docker container rm [container]` | 删除容器（完整写法） | container,rm,delete |
| 容器管理 | `docker port [container]` | 查看容器端口映射 | container,port,network |
| 容器管理 | `docker top [container]` | 显示容器内进程 | container,top,process,debug |
| 容器管理 | `docker cp [FILE] [container]:[PATH]` | 复制本地文件到容器 | container,cp,copy,file |
| 容器管理 | `docker diff [container]` | 显示容器文件系统变化 | container,diff,debug |
| 容器管理 | `docker stats [container]` | 显示容器资源使用情况 | container,stats,monitor |

---

## 容器运行参数

| 分类 | 命令 | 说明 | 标签 |
|------|------|------|------|
| 容器运行 | `docker run --name [name] [image]` | 创建运行并命名容器 | container,run,name |
| 容器运行 | `docker run -d [image]` | 后台运行容器（守护模式） | container,run,daemon,daily |
| 容器运行 | `docker run -p [hostPort]:[containerPort] [image]` | 指定端口映射 | container,run,port,network |
| 容器运行 | `docker run -P [image]` | 随机端口映射 | container,run,port,random |
| 容器运行 | `docker run -e [key=value] [image]` | 设置环境变量 | container,run,env |
| 容器运行 | `docker run -w [PATH] [image]` | 设置工作目录 | container,run,workdir |
| 容器运行 | `docker run -it [image] /bin/bash` | 交互式运行并进入 shell | container,run,interactive,daily |
| 容器运行 | `docker run -v [hostPath]:[containerPath] [image]` | 挂载数据卷 | container,run,volume |
| 容器运行 | `docker run --rm [image]` | 运行后自动删除容器 | container,run,temp |

---

## 网络管理命令

| 分类 | 命令 | 说明 | 标签 |
|------|------|------|------|
| 网络管理 | `docker network ls` | 列出可用网络 | network,ls,list |
| 网络管理 | `docker network inspect [network]` | 查看网络详细信息 | network,inspect,debug |
| 网络管理 | `docker network create [network]` | 创建新网络 | network,create |
| 网络管理 | `docker network rm [network]` | 删除网络 | network,rm,delete |
| 网络管理 | `docker network connect [network] [container]` | 连接容器到网络 | network,connect |
| 网络管理 | `docker network disconnect [network] [container]` | 断开容器网络连接 | network,disconnect |

---

## 数据卷管理命令

| 分类 | 命令 | 说明 | 标签 |
|------|------|------|------|
| 数据卷管理 | `docker volume create [volume]` | 创建数据卷 | volume,create |
| 数据卷管理 | `docker volume ls` | 查看数据卷 | volume,ls,list |
| 数据卷管理 | `docker volume inspect [volume]` | 查看数据卷详情 | volume,inspect,debug |
| 数据卷管理 | `docker volume rm [volume]` | 删除数据卷 | volume,rm,delete |
| 数据卷管理 | `docker volume prune` | 清理未使用数据卷 | volume,prune,cleanup |

---

## 插件管理命令

| 分类 | 命令 | 说明 | 标签 |
|------|------|------|------|
| 插件管理 | `docker plugin ls` | 列出插件 | plugin,ls,list |
| 插件管理 | `docker plugin install [plugin]` | 安装插件 | plugin,install |
| 插件管理 | `docker plugin enable [plugin]` | 启用插件 | plugin,enable |
| 插件管理 | `docker plugin disable [plugin]` | 禁用插件 | plugin,disable |
| 插件管理 | `docker plugin rm [plugin]` | 卸载插件 | plugin,rm,delete |

---

## 日常操作命令

| 分类 | 命令 | 说明 | 标签 |
|------|------|------|------|
| 日常操作 | `docker info` | 查看 Docker 系统信息 | info,system |
| 日常操作 | `docker version` | 查看 Docker 版本 | version |
| 日常操作 | `docker --help` | 查看帮助文档 | help |
| 日常操作 | `docker [command] --help` | 查看具体命令帮助 | help |
| 日常操作 | `docker login` | 登录 Docker Hub | login,auth |
| 日常操作 | `docker logout` | 退出 Docker Hub | logout,auth |

---

## Dockerfile 指令

| 指令 | 说明 | 标签 |
|------|------|------|
| `FROM [base_image]` | 指定基础镜像（必须是第一条指令） | dockerfile,from,base |
| `RUN [command]` | 执行命令并创建新层 | dockerfile,run,build |
| `COPY [--chown=<user>:<group>] [src] [dest]` | 复制本地文件到镜像 | dockerfile,copy,file |
| `ADD [src] [dest]` | 复制文件（支持 URL 和自动解压） | dockerfile,add,file,url |
| `WORKDIR [path]` | 设置工作目录 | dockerfile,workdir,path |
| `ENV [key]=[value]` | 设置环境变量 | dockerfile,env,variable |
| `CMD ["executable", "param1", ...]` | 容器默认执行命令（仅一条生效） | dockerfile,cmd,run |
| `ENTRYPOINT ["executable"]` | 容器入口点 | dockerfile,entrypoint |
| `EXPOSE [port]` | 声明暴露端口 | dockerfile,expose,port |
| `VOLUME [path]` | 定义匿名卷（持久化目录） | dockerfile,volume,persist |
| `LABEL [key]=[value]` | 添加元数据标签 | dockerfile,label,meta |
| `ARG [name]=[default]` | 构建参数 | dockerfile,arg,build |
| `USER [user]` | 设置运行用户 | dockerfile,user,security |

---

## 查询示例

```bash
# 1. 查看所有日常使用的命令
grep "daily" commands.md

# 2. 查看所有删除相关的命令
grep "rm,delete" commands.md

# 3. 查看所有容器运行相关的命令
grep "container,run" commands.md

# 4. 查看所有调试相关的命令
grep "debug" commands.md

# 5. 查看所有备份相关的命令
grep "backup" commands.md

# 6. 组合筛选：查看日常使用的容器命令
grep "container" commands.md | grep "daily"
```
