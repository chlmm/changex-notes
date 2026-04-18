# Kit 与跨平台

## Kit 概念

Kit 是 Qt Creator 的核心配置单元，一个 Kit = **编译器 + Qt 版本 + 调试器 + 设备** 的组合。

```
一个 Kit 定义了：
├── 编译器（MSVC / GCC / Clang / MinGW）
├── Qt 版本（Qt 5.15 / Qt 6.5 / 自定义路径）
├── 调试器（CDB / GDB / LLDB）
├── CMake 工具（版本和路径）
└── 设备（本地 / 远程 / 模拟器）
```

## Kit 配置

### 配置入口

```
工具 → 选项 → Kits
├── Kits 标签页 → 查看/新建/编辑 Kit
├── Qt Versions 标签页 → 注册 Qt 安装
├── Compilers 标签页 → 注册编译器
└── Debuggers 标签页 → 注册调试器
```

### 配置顺序（重要）

配置 Kit 必须按以下顺序，因为 Kit 依赖其他项：

```
1. 先注册编译器 → Compilers 标签页
2. 再注册 Qt 版本 → Qt Versions 标签页
3. 再注册调试器 → Debuggers 标签页
4. 最后创建 Kit → Kits 标签页 → 选择上述组件
```

### 注册 Qt 版本

```
1. Qt Versions 标签页 → 添加
2. 浏览到 qmake 的路径
   ├── Windows (MSVC): C:\Qt\6.5.0\msvc2019_64\bin\qmake.exe
   ├── Windows (MinGW): C:\Qt\6.5.0\mingw_64\bin\qmake.exe
   ├── Linux: /home/user/Qt/6.5.0/gcc_64/bin/qmake
   └── macOS: /Users/user/Qt/6.5.0/macos/bin/qmake
3. Qt Creator 自动检测版本信息
```

### 注册编译器

Qt Creator 通常自动检测系统上已安装的编译器。如果没有：

```
1. Compilers 标签页 → 添加 → 选择类型（GCC / Clang / MSVC）
2. 设置编译器路径
3. 应用
```

### 创建自定义 Kit

```
1. Kits 标签页 → 添加
2. 填写：
   ├── 名称：如 "Desktop Qt 6.5.0 MSVC 2019 64bit"
   ├── 设备类型：Desktop
   ├── 设备：本地 PC
   ├── 编译器 C：选择 MSVC 2019 x64
   ├── 编译器 C++：选择 MSVC 2019 x64
   ├── 调试器：选择 CDB
   ├── Qt 版本：选择 Qt 6.5.0 MSVC 2019 64bit
   └── CMake 工具：选择对应版本
3. 应用
```

## 常见 Kit 配置场景

### 场景一：同时支持 MSVC 和 MinGW

```
Kit 1: Desktop Qt 6.5.0 MSVC 2019 64bit
├── 编译器: MSVC 2019 x64
├── Qt: C:\Qt\6.5.0\msvc2019_64
└── 调试器: CDB

Kit 2: Desktop Qt 6.5.0 MinGW 64bit
├── 编译器: MinGW-w64 11.2
├── Qt: C:\Qt\6.5.0\mingw_64
└── 调试器: GDB
```

**为什么需要两个**：某些第三方库只提供 MSVC 版本或只提供 MinGW 版本。

### 场景二：Qt 5 和 Qt 6 并存

```
Kit 1: Desktop Qt 5.15.2 MSVC 2019 64bit
├── Qt: C:\Qt\5.15.2\msvc2019_64

Kit 2: Desktop Qt 6.5.0 MSVC 2019 64bit
├── Qt: C:\Qt\6.5.0\msvc2019_64
```

### 场景三：交叉编译（ARM / 嵌入式）

```
Kit: Embedded Linux ARM
├── 编译器: arm-linux-gnueabihf-gcc
├── Qt: /opt/qt-arm/bin/qmake
├── 调试器: arm-linux-gnueabihf-gdb
└── 设备: 远程设备 (SSH)
```

## 切换 Kit

### 在项目中切换

```
1. 左侧项目面板 → 选择 Kit
2. 每个 Kit 有独立的构建目录和配置
3. 切换后需要重新配置（CMake 项目自动触发）
```

### 多 Kit 同时构建

```
项目 → 构建设置 → 可以同时启用多个 Kit
每个 Kit 独立的 Build / Run 配置
```

## 跨平台代码编写策略

### 平台条件编译

```cpp
// 方法一：Qt 的宏
#ifdef Q_OS_WIN
    // Windows 特有代码
#endif

#ifdef Q_OS_LINUX
    // Linux 特有代码
#endif

#ifdef Q_OS_MACOS
    // macOS 特有代码
#endif

// 方法二：检查多个平台
#if defined(Q_OS_WIN) || defined(Q_OS_MACOS)
    // 桌面平台共有代码
#endif
```

### Qt 平台抽象

```
尽量用 Qt 的跨平台 API
├── 文件操作 → QFile / QDir / QFileInfo（不用 std::filesystem 或 WinAPI）
├── 网络操作 → QTcpSocket / QNetworkAccessManager
├── 线程    → QThread / QtConcurrent
├── 进程    → QProcess
├── 路径    → QStandardPaths（不用硬编码路径）
└── 时间    → QDateTime / QTimer
```

### 平台差异注意事项

| 方面 | Windows | Linux | macOS |
|------|---------|-------|-------|
| 路径分隔符 | `\` | `/` | `/` |
| 换行符 | `\r\n` | `\n` | `\n` |
| 可执行文件后缀 | `.exe` | 无 | 无 |
| 动态库后缀 | `.dll` | `.so` | `.dylib` |
| 应用打包 | 安装程序/绿色版 | AppImage/deb/rpm | `.app` / `.dmg` |
| 文件权限 | 较少关注 | 需要处理 | 需要处理 |

### 跨平台文件路径处理

```cpp
// ✅ 正确 — 使用 QDir
QString path = QDir::homePath() + "/config.ini";

// ✅ 正确 — 使用 QStandardPaths
QString configDir = QStandardPaths::writableLocation(QStandardPaths::AppConfigLocation);

// ❌ 错误 — 硬编码路径
QString path = "C:\\Users\\user\\config.ini";  // Linux/macOS 上不行
```

## 部署

### Windows 部署

```
1. 使用 Release 配置构建
2. 运行 windeployqt
   windeployqt MyApp.exe
3. 自动复制所需的 Qt DLL 和插件到目录
4. 打包分发
```

### Linux 部署

```
方式一：AppImage（推荐）
1. 构建程序
2. 使用 linuxdeployqt 打包
3. 生成单个 AppImage 文件

方式二：系统包
1. 创建 .deb / .rpm 包
2. 声明 Qt 依赖
```

### macOS 部署

```
1. 构建 Release 版本
2. 使用 macdeployqt
   macdeployqt MyApp.app
3. 生成 .app 包
4. 可选：创建 .dmg 安装镜像
```

## 常见问题

### 问题：Kit 显示红色警告

```
Kit 图标红色
├── 编译器未配置？→ Compilers 标签页检查
├── Qt 版本无效？→ Qt Versions 标签页检查 qmake 路径
├── 调试器缺失？→ Debuggers 标签页检查
└── CMake 未找到？→ CMake 标签页检查路径
```

### 问题：切换 Kit 后 CMake 配置失败

**原因**：不同 Kit 的构建目录可能冲突。

**解决**：
- 确保每个 Kit 使用独立的构建目录（默认如此）
- 项目 → 构建设置 → 清除 CMake 配置 → 重新配置

### 问题：同一代码在不同平台行为不一致

**排查思路**：
- 检查条件编译是否覆盖了所有平台
- 检查文件路径处理是否用了 Qt 跨平台 API
- 检查字节序问题（ARM 可能是大端）
- 检查编译器差异（MSVC 和 GCC 对模板/C++ 特性的支持不同）
