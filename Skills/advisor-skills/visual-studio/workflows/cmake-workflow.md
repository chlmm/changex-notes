# CMake 工作流

## CMake vs MSBuild 决策

```
选哪个？
├─ 需要跨平台（Linux/macOS 也要编译）───→ CMake
├─ 使用 vcpkg 管理依赖 ───→ CMake（集成更自然）
├─ 纯 Windows 且项目简单 ───→ MSBuild（配置更直观）
├─ 需要精细控制编译选项（预编译头等）───→ MSBuild（VS 属性页更方便）
└─ 团队已有 CMake 代码库 ───→ CMake
```

## VS 中的 CMake 项目模式

VS 2022 支持两种方式使用 CMake：

| 模式 | 方式 | 适合 |
|------|------|------|
| **打开文件夹** | 文件 → 打开 → 选择 CMakeLists.txt 所在目录 | 推荐，原生 CMake 体验 |
| **CMake 项目** | 新建项目 → CMake 项目模板 | 从零开始的新项目 |

**推荐**：用"打开文件夹"模式，更接近 CMake 的原生工作方式。

## CMake 项目工作流

### 1. 打开项目

```
1. 文件 → 打开 → 文件夹
2. 选择包含顶层 CMakeLists.txt 的目录
3. VS 自动检测 CMakeLists.txt 并开始配置
```

### 2. 配置项目

首次打开或修改 CMakeLists.txt 后，VS 会自动运行 CMake Configure。

**手动触发**：项目 → 配置 CMake（或保存 CMakeLists.txt 时自动触发）

### 3. 选择配置

```
配置下拉框（顶部工具栏）
├── x64-Debug      ← 默认
├── x64-Release
└── 自定义配置（CMakePresets.json 中定义）
```

### 4. 构建

```
生成 → 全部生成        ← 构建所有目标
生成 → 仅生成 <target> ← 构建指定目标
```

### 5. 调试

```
1. 选择启动项（工具栏下拉菜单）→ 选择要调试的 target
2. 设置断点
3. 开始调试
```

## CMakePresets.json

### 为什么用 Presets

CMakePresets.json 替代了 CMakeSettings.json，是 CMake 官方标准格式，可在命令行和 VS 中通用。

### 基础模板

```json
{
  "version": 6,
  "configurePresets": [
    {
      "name": "windows-default",
      "displayName": "Windows x64 Debug",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/out/build/${presetName}",
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug",
        "CMAKE_CXX_STANDARD": "17"
      },
      "condition": {
        "type": "equals",
        "lhs": "${hostSystemName}",
        "rhs": "Windows"
      }
    },
    {
      "name": "windows-release",
      "displayName": "Windows x64 Release",
      "inherits": "windows-default",
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Release"
      }
    }
  ],
  "buildPresets": [
    {
      "name": "windows-debug",
      "configurePreset": "windows-default"
    },
    {
      "name": "windows-release-build",
      "configurePreset": "windows-release"
    }
  ]
}
```

### 关键字段说明

| 字段 | 作用 | 常用值 |
|------|------|--------|
| `generator` | 构建系统生成器 | `Ninja`（推荐）、`Visual Studio 17 2022` |
| `binaryDir` | 构建输出目录 | `${sourceDir}/out/build/${presetName}` |
| `cacheVariables` | CMake 缓存变量 | `CMAKE_BUILD_TYPE`、`CMAKE_CXX_STANDARD` |
| `inherits` | 继承其他 preset | 避免重复配置 |

## vcpkg 集成

### 方式一：CMakePresets.json 中配置（推荐）

```json
{
  "name": "windows-default",
  "cacheVariables": {
    "CMAKE_TOOLCHAIN_FILE": "$env{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
  }
}
```

**前提**：设置了 `VCPKG_ROOT` 环境变量。

### 方式二：CMakeLists.txt 中配置

```cmake
# 在 project() 之前
if(DEFINED ENV{VCPKG_ROOT})
    set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
        CACHE STRING "Vcpkg toolchain")
endif()
```

### 使用 vcpkg 安装依赖

```bash
# 在项目根目录
vcpkg install fmt:x64-windows
vcpkg install spdlog:x64-windows
```

在 CMakeLists.txt 中：
```cmake
find_package(fmt CONFIG REQUIRED)
find_package(spdlog CONFIG REQUIRED)

target_link_libraries(MyTarget PRIVATE fmt::fmt spdlog::spdlog)
```

## launch.vs.json

### 用途

配置 CMake 项目的调试启动参数（命令行参数、工作目录、环境变量等）。

### 创建方式

1. 右键 CMakeLists.txt 中的 target → 添加调试配置
2. VS 自动生成 `.vs/launch.vs.json`

### 常用配置

```json
{
  "version": "0.2.1",
  "defaults": {},
  "configurations": [
    {
      "type": "default",
      "project": "CMakeLists.txt",
      "projectTarget": "my_app.exe",
      "name": "my_app.exe",
      "args": ["--input", "test.txt"],
      "currentDir": "${workspaceRoot}/data",
      "env": {
        "MY_VAR": "hello"
      }
    }
  ]
}
```

## CMakeLists.txt 编写速查

### 基础模板

```cmake
cmake_minimum_required(VERSION 3.20)
project(MyApp VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 源文件
add_executable(MyApp main.cpp utils.cpp)

# 或用 aux_source_directory 自动收集
# aux_source_directory(src APP_SOURCES)
# add_executable(MyApp ${APP_SOURCES})

# 头文件搜索路径
target_include_directories(MyApp PRIVATE include)

# 链接库
target_link_libraries(MyApp PRIVATE some_lib)

# 子目录
add_subdirectory(lib)
```

### 添加库项目

```cmake
add_library(my_lib STATIC src/lib.cpp)
target_include_directories(my_lib PUBLIC include)
```

## 常见问题

### 问题：CMake Configure 失败

```
CMake 配置报错
├─ CMakeLists.txt 语法错误？
│  → 看输出窗口 中的错误信息
├─ 找不到依赖？
│  → 检查 CMAKE_PREFIX_PATH 或 vcpkg toolchain 是否配置
├─ Generator 不匹配？
│  → 检查 CMakePresets.json 中的 generator 设置
└─ 缓存损坏？
   → 项目 → 删除缓存并重新配置
```

### 问题：IntelliSense 对 CMake 项目不工作

```
1. 确认 CMake Configure 成功（输出窗口无错误）
2. 确认选中了正确的 CMake 配置
3. 删除 .vs 目录和 out/ 目录 → 重新打开项目
4. 考虑安装 Clangd 扩展替代 IntelliSense
```

### 问题：修改 CMakeLists.txt 后没有重新配置

**解决**：
- 保存 CMakeLists.txt 时 VS 通常会自动重新配置
- 如果没有：项目 → 配置 CMake 手动触发
