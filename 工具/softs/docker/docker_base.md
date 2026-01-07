| 镜像管理 | docker image ls | 查看镜像 |  |
| --- | --- | --- | --- |
| 镜像管理 | docker images | 查看镜像 |  |
| 镜像管理 | docker search [image] | 检索镜像 |  |
| 镜像管理 | docker search nginx | 检索nginx镜像 |  |
| 镜像管理 | docker pull [image] | 拉取镜像 |  |
| 镜像管理 | docker push [image] | 上传镜像 |  |
| 镜像管理 | docker push geekhour/hello-docker:latest | 上传该镜像 |  |
| 镜像管理 | docker save [image] -o FILE / | 保存镜像 |  |
| 镜像管理 | docker save [image] > FILE | 保存镜像 |  |
| 镜像管理 | docker save geekhour/hello-docker:latest > hello-docker.tar | 将该镜像保存为该压缩包 |  |
| 镜像管理 | docker load -i FILE | 导⼊镜像 |  |
| 镜像管理 | docker load -i hello-docker.tar | 将该压缩包中的镜像导入进来 |  |
| 镜像管理 | docker history [image] | 查看镜像历史 |  |
| 镜像管理 | docker rmi [image] / | 删除镜像 |  |
| 镜像管理 | docker image rm [image] | 删除镜像 |  |
| 镜像管理 | docker image prune | 删除不再使⽤的镜像 |  |
| 镜像管理 | docker import [URL/FILE] | 将⽂件系统导⼊为镜像 |  |
| 镜像管理 | docker commit [container] [image] | 从容器创建镜像 |  |
| ⽹络管理 | docker network ls | 列出可⽤⽹络 |  |
| ⽹络管理 | docker network inspect [network] | 查看⽹络详细信息 |  |
| ⽹络管理 | docker network create [network] | 创建⼀个新的⽹络 |  |
| ⽹络管理 | docker network rm [network] | 删除⼀个⽹络 |  |
| ⽹络管理 | docker network connect [network] [container] | 将容器连接到⽹络 |  |
| ⽹络管理 | docker network disconnect [network] [container] | 将容器从⽹络断开 |  |
| 插件管理 | docker plugin ls | 列出插件 |  |
| 插件管理 | docker plugin install [plugin] | 安装插件 |  |
| 插件管理 | docker plugin enable [plugin] | 启⽤插件 |  |
| 插件管理 | docker plugin disable [plugin] | 禁⽤插件 |  |
| 插件管理 | docker plugin rm [plugin] | 卸载插件 |  |
| 容器管理 | docker create [image] | 创建容器（仅创建，不运行） |  |
| 容器管理 | docker run [image] | 创建并运行容器 |  |
| 容器管理 | docker start [container] | 启动容器 |  |
| 容器管理 | docker stop [container] | 停止容器 |  |
| 容器管理 | docker restart [container] | 重启容器 |  |
| 容器管理 | docker ps  | 列出正在运行的容器 |  |
| 容器管理 | docker container Is | 列出正在运行的容器 |  |
| 容器管理 | docker ps-a  | 列出所有容器 |  |
| 容器管理 | docker container Is -a | 列出所有容器 |  |
| 容器管理 | docker exec -i [container] bash | 以交互模式进入容器 |  |
| 容器管理 | docker attach [container] | 以交互模式进入容器 |  |
| 容器管理 | docker export [container] -o FILE  | 导出容器 |  |
| 容器管理 | docker export [container] > FILE | 导出容器 |  |
| 容器管理 | docker import FILE | 导入容器快照 |  |
| 容器管理 | docker logs [container] | 查看容器日志 |  |
| 容器管理 | docker rm [container] | 删除容器 |  |
| 容器管理 | docker container rm [container] | 删除容器 |  |
| 容器管理 | docker port [container] | 查看容器端口映射 |  |
| 容器管理 | docker top [container] | 显示容器内进程 |  |
| 容器管理 | docker cp [FILE] [container]:[PATH] | 复制本地文件到容器内的指定路径 |  |
| 容器管理 | docker diff [container] | 显示容器内的变化 |  |
| 容器管理 | docker stats [container] | 显示容器资源使用情况 |  |
| 数据卷管理 | docker  volume create [volume] | 创建一个数据卷 |  |
| 数据卷管理 | docker volume Is | 查看数据卷 |  |
| 数据卷管理 | docker volume inspect [volume] | 查看数据卷详细信息 |  |
| 数据卷管理 | docker volume rm [volume] | 删除数据卷 |  |
| 数据卷管理 | docker volume prune | 删除所有未使用的数据卷 |  |
| ⽇常操作 | docker  info | 查看docker系统信息 |  |
| ⽇常操作 | docker version | 查看Docker版本 |  |
| ⽇常操作 | docker --help | 查看Docker帮助文档 |  |
| ⽇常操作 | docker [command]--help | 查看Docker命令帮助 |  |
| ⽇常操作 | docker login | 登录Docker |  |
| ⽇常操作 | docker logout | 退出Docker |  |
| 容器运⾏ | docker run --name [name][image] | 创建运行并命名容器 | docker run [options]image [command][arg…] |
| 容器运⾏ | docker run -d [image] | 创建一个容器并后台运行 |  |
| 容器运⾏ | docker run -p [hostPort]:[containerPort][image] | 创建一个容器并指定端口映射 |  |
| 容器运⾏ | docker run -P [image] | 创建一个容器并指定端口映射（随机分配） |  |
| 容器运⾏ | docker run -e [key=value][image] | 创建一个容器并指定环境变量 |  |
| 容器运⾏ | docker run -w [PATH][image] | 创建一个容器并指定工作目录 |  |
| 容器运⾏ | docker run -name [name][image] | 创建一个容器并指定容器名称 |  |
| 容器运⾏ | docker run [image][command] | 创建一个容器并在容器中执行命令（交互模式） |  |
| 容器运⾏ | docker run -d -p [hostPort]:[containerPort]-e [key=value] w [PATH] --name [name][image] | 创建一个容器，并指定容器名称，后台运行，端口映射环境变量，工作目录 |  |
| 容器运⾏ | docker run -it nginx:latest /bin/bash | 使用镜像nginx:latest来启动一个容器，并在容器内执行交互式bash shell |  |
| 容器运⾏ | docker run -it -p 3316:3306 -v/data:/data -d mysql:latest | 创建一个ysql容器，后台模式启动，主机80端口映射到容器80端口，主机/data目录映射到容器/data目录 |  |

### 常⽤ Dockerfile指令

| FROM [base_image] | 指定基础镜像，必须为 Dockerfile 的第⼀条指令 |
| --- | --- |
| ADD | ⽤于将⽂件复制到镜像中，源可以使 URL 或者本地⽂件，也可
以⼀个压缩⽂件（⾃动解压） |
| COPY [--chown=<user>:<group>] [源路径] [⽬标路径] | ⽤于将⽂件拷⻉到镜像中，源只能是本地⽂件 |
| WORKDIR [PATH] | ⽤于指定⼯作⽬录，可以使⽤多个 WORKDIR 指令，如果使⽤
相对路径，则是相对于上⼀条 WORKDIR 指令所指定的⽬录 |
| ENV <key> <value> | ⽤于设置环境变量 |
| ENV <key1>=<value1> <key2>=<value2> … | ⽤于设置环境变量 |
| CMD <命令> | ⽤于指定默认的容器主进程，每个 Dockerfile 中只能有⼀条 CMD
指令，如果有多条，则只有最后⼀条会⽣效 |
| CMD ["可执⾏⽂件", "参数 1", "参数 2" ...] | ⽤于指定默认的容器主进程，每个 Dockerfile 中只能有⼀条 CMD
指令，如果有多条，则只有最后⼀条会⽣效 |
| VOLUME <路径> | ⽤于定义匿名卷（持久化⽬录） |
| VOLUME ["路径 1", "路径 2"...] | ⽤于定义匿名卷（持久化⽬录） |