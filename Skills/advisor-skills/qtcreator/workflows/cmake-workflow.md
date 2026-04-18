# CMake 工作流

## Qt Creator 的 CMake 集成

Qt Creator 对 CMake 的支持方式与 VS 不同：

| 特性 | Visual Studio | Qt Creator |
|------|--------------|------------|
| CMake 配置触发 | 手动/保存时自动 | 手动/保存时自动 |
| CMakePresets 支持 | ✅ | ✅ (Qt Creator 6+) |
| 构建目录 | `out/build/` | 与 Kit 绑定的影子构建目录 |
| Kit 集成 | 无 Kit 概念 | Kit 决定编译器和 Qt 版本 |
| 运行配置 | launch.vs.json | 项目 → 运行设置 |

## 打开 CMake 项目

```
1. 文件 → 打开文件或项目
2. 选择 CMakeLists.txt
3. 选择 Kit
4. Qt Creator 自动运行 CMake Configure
5. 等待配置完成（输出面板显示进度）
```

## CMake 配置

### 配置流程

```
首次打开 / 修改 CMakeLists.txt 后
1. Qt Creator 自动检测变更
2. 弹出提示 "CMake 配置已过期"
3. 点击 "重新配置" 或自动重新配置
4. 查看输出面板确认成功
```

### 手动触发

```
项目 → 构建设置 → 运行 CMake
```

### 配置参数

```
项目 → 构建设置 → CMake → Initial Configuration
├── CMAKE_PREFIX_PATH: Qt 安装路径（通常自动设置）
├── CMAKE_BUILD_TYPE: Debug / Release
├── CMAKE_CXX_STANDARD: 17 / 20
└── 自定义变量
```

## Qt 项目的 CMakeLists.txt

### 基础模板（Qt 6）

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyApp VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Qt 自动化处理（必须开启）
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# 查找 Qt
find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets)

# 可执行文件
add_executable(MyApp
    main.cpp
    mainwindow.cpp
    mainwindow.h
    mainwindow.ui
    resources.qrc
)

# 链接 Qt 模块
target_link_libraries(MyApp PRIVATE
    Qt6::Core
    Qt6::Gui
    Qt6::Widgets
)
```

### 添加 Qt 模块

```cmake
# 网络模块
find_package(Qt6 REQUIRED COMPONENTS Network)
target_link_libraries(MyApp PRIVATE Qt6::Network)

# SQL 模块
find_package(Qt6 REQUIRED COMPONENTS Sql)
target_link_libraries(MyApp PRIVATE Qt6::Sql)

# QML 模块
find_package(Qt6 REQUIRED COMPONENTS Qml Quick)
target_link_libraries(MyApp PRIVATE Qt6::Qml Qt6::Quick)
```

### Qt 6 的 qt_add_executable

Qt 6 推荐用 `qt_add_executable` 替代 `add_executable`：

```cmake
qt_add_executable(MyApp
    main.cpp
    mainwindow.cpp
    mainwindow.h
    mainwindow.ui
)
```

**优势**：
- 自动处理平台特定的应用打包（macOS .app、Windows WinMain 等）
- 自动添加 Qt 的资源处理

### QML 模块（Qt 6）

```cmake
qt_add_qml_module(MyApp
    URI MyApp
    VERSION 1.0
    QML_FILES
        Main.qml
        Page1.qml
    RESOURCES
        images/logo.png
)
```

## CMakePresets.json

### 基础模板

```json
{
  "version": 6,
  "configurePresets": [
    {
      "name": "windows-msvc-debug",
      "displayName": "Windows MSVC Debug",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/build/${presetName}",
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug",
        "CMAKE_PREFIX_PATH": "C:/Qt/6.5.0/msvc2019_64"
      }
    },
    {
      "name": "windows-mingw-debug",
      "displayName": "Windows MinGW Debug",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/build/${presetName}",
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug",
        "CMAKE_PREFIX_PATH": "C:/Qt/6.5.0/mingw_64"
      }
    },
    {
      "name": "linux-debug",
      "displayName": "Linux Debug",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/build/${presetName}",
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug",
        "CMAKE_PREFIX_PATH": "/home/user/Qt/6.5.0/gcc_64"
      }
    }
  ],
  "buildPresets": [
    {
      "name": "windows-msvc-debug-build",
      "configurePreset": "windows-msvc-debug"
    }
  ]
}
```

### Qt Creator 中使用 Presets

```
Qt Creator 6+ 自动读取 CMakePresets.json
1. 项目 → 构建设置 → 可以选择 Preset 作为配置
2. Preset 中的 Kit 配置会覆盖 Qt Creator 的 Kit
3. 如果不用 Presets，Qt Creator 用 Kit 的设置
```

## 运行配置

### 配置运行参数

```
项目 → 运行设置
├── 可执行文件：自动检测（CMake target）
├── 命令行参数：输入参数
├── 工作目录：设置运行时目录
└── 环境变量：设置运行时环境
```

### 多运行配置

```
同一个项目可以有多个运行配置
1. 项目 → 运行设置 → 添加运行配置
2. 分别设置不同的参数
3. 在左下角选择要运行的配置
```

**场景**：同一个程序用不同的命令行参数/工作目录运行。

## 常见问题

### 问题：CMake 找不到 Qt

```
Could not find Qt6
├── CMAKE_PREFIX_PATH 没设？
│  ├── 在 CMakePresets.json 中设置
│  ├── 或在 Qt Creator 中：项目 → 构建设置 → CMake → Initial Configuration
│  └── 或在 CMakeLists.txt 中：set(CMAKE_PREFIX_PATH "path/to/Qt")
├── Kit 中的 Qt 版本没配？
│  → 工具 → 选项 → Kits → Qt Versions → 添加 qmake 路径
└── 装了多个 Qt 版本冲突？
   → 明确指定 CMAKE_PREFIX_PATH
```

### 问题：修改 CMakeLists.txt 后没有重新配置

**解决**：
- 保存 CMakeLists.txt 后 Qt Creator 通常弹出重新配置提示
- 如果没有：项目 → 构建设置 → 运行 CMake

### 问题：AUTOMOC 导致链接错误

```
场景：含 Q_OBJECT 的类定义在 .cpp 中

解决：在 .cpp 末尾添加
#include "xxx.moc"   // xxx 是当前文件名（不含扩展名）

原因：AUTOMOC 只扫描头文件，.cpp 中的 Q_OBJECT 需要手动包含 moc 输出
```

### 问题：CMake 缓存损坏

```
1. 项目 → 构建设置 → 清除 CMake 配置
2. 删除构建目录
3. 重新打开项目
4. Qt Creator 重新运行 CMake Configure
```
