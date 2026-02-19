---
name: cpp-udp-module
description: 生成工业级 C++ UDP 网络模块代码。支持单播、广播、组播三种模式，跨平台（Linux/Windows），线程安全设计。
execution_mode: ai
metadata:
  category: code-generation
  language: cpp
  platform: [linux, windows, macos]
  tags: [udp, network, socket, multicast, broadcast]
---

# C++ UDP 模块生成器

## 概述

根据用户指定的参数，生成一个完整的、工业级 C++ UDP 网络模块。

## 何时使用

当用户需要：
- 创建 UDP 网络通信组件
- 实现组播/广播发现协议
- 构建实时数据流传输
- 需要跨平台 UDP socket 封装

## 使用方法

### 1. 询问用户参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `class_name` | 类名 | `UdpModule` |
| `namespace` | 命名空间 | 无 |
| `output_dir` | 输出目录 | 当前目录 |
| `buffer_size` | 接收缓冲区大小 | `65535` |
| `timeout` | 接收超时（毫秒） | `100` |

### 2. 生成文件结构

```
{output_dir}/
├── include/
│   └── udp_module.h
├── src/
│   ├── udp_module.cpp
│   └── main.cpp          # 使用示例
└── CMakeLists.txt
```

### 3. 模板替换

读取模板文件，替换以下占位符：

| 占位符 | 替换为 |
|--------|--------|
| `{{CLASS_NAME}}` | 用户指定的类名 |
| `{{NAMESPACE_BEGIN}}` | `namespace xxx {` 或空 |
| `{{NAMESPACE_END}}` | `} // namespace xxx` 或空 |
| `{{HEADER_FILE}}` | 头文件名（默认 `udp_module.h`） |
| `{{BUFFER_SIZE}}` | 缓冲区大小 |
| `{{TIMEOUT}}` | 超时时间 |

## 模板文件

| 文件 | 说明 |
|------|------|
| [templates/header.template](templates/header.template) | 头文件模板 |
| [templates/implementation.template](templates/implementation.template) | 实现文件模板 |
| [templates/example.template](templates/example.template) | 使用示例模板 |
| [templates/cmake.template](templates/cmake.template) | CMake 配置模板 |

## 核心功能

### 三种通信模式

```cpp
enum class UdpMode {
    UNICAST,    // 单播：点对点通信
    BROADCAST,  // 广播：发送到网络所有设备
    MULTICAST   // 组播：发送到订阅组
};
```

### 生命周期管理

```cpp
// 初始化
udp.init(8080, UdpMode::UNICAST);

// 启动接收线程
udp.start();

// 停止
udp.stop();
```

### 数据接收回调

```cpp
udp.setReceiveCallback([](const char* data, size_t size,
                          const std::string& from_ip, uint16_t from_port) {
    // 处理接收到的数据
});
```

### 发送数据

```cpp
// 单播发送
udp.send(data, size, "192.168.1.100", 8080);

// 广播发送
udp.sendBroadcast(data, size, 8080);

// 组播发送
udp.joinMulticastGroup("239.255.0.1");
udp.sendToMulticast(data, size, 8080);
```

## 设计参考

详细的设计文档和流程图请参考：

- [references/design.md](references/design.md) - 架构设计和流程图

## 编译说明

### Linux/macOS

```bash
mkdir build && cd build
cmake ..
make
```

### Windows (Visual Studio)

```bash
mkdir build && cd build
cmake .. -G "Visual Studio 17 2022"
cmake --build . --config Release
```

## 最佳实践

1. **回调函数中避免阻塞操作** - 回调在接收线程中执行
2. **及时调用 stop()** - 程序退出前确保停止接收线程
3. **组播地址范围** - 使用 `239.0.0.0/8`（本地管理）
4. **缓冲区大小** - 根据 MTU 和数据包大小调整
