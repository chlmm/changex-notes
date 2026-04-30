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

# 设置默认命令
CMD ["/bin/bash"]
