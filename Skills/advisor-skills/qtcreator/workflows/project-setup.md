# 项目搭建

## 决策树：选择项目类型

```
你要做什么？
├─ Qt Widgets 桌面应用 ──→ Qt Widgets Application
├─ Qt Quick/QML 应用 ──→ Qt Quick Application
├─ 纯 C++ 控制台程序 ──→ Qt Console Application
├─ 非 Qt 的纯 C++ 项目 ──→ Non-Qt Project (CMake/qmake)
└─ Qt 库/插件 ──→ Qt Library / Qt Plugin
```

## 构建系统选择

```
qmake 还是 CMake？
├─ 已有 CMakeLists.txt ──→ CMake
├─ 需要跨构建系统（不只 Qt Creator）───→ CMake
├─ 团队有 CMake 经验 ──→ CMake
├─ 纯 Qt 项目、结构简单 ──→ qmake（更简单）
├─ 需要用 Qt 的 .pro 模板语法 ──→ qmake
└─ 不确定 ──→ CMake（行业趋势，Qt 6 官方推荐）
```

**趋势**：Qt 6 已将 CMake 作为首选构建系统，qmake 仍然支持但不再是推荐方案。

## 新建项目流程

### 1. 创建项目

```
1. 文件 → 新建文件或项目
2. 选择项目模板（Application / Library / Non-Qt Project）
3. 选择构建系统（qmake / CMake）
4. 选择 Kit（编译器 + Qt 版本，详见 kit-cross-platform.md）
5. 填写项目名和路径
6. 选择版本控制（Git 推荐）
7. 完成
```

### 2. 项目结构理解

#### Qt Widgets 项目（CMake）

```
MyApp/
├── CMakeLists.txt        # 构建配置
├── main.cpp              # 程序入口
├── mainwindow.cpp/h      # 主窗口类
├── mainwindow.ui         # UI 布局文件（Qt Designer）
└── mainwindow.ui.autosave # 自动保存（可忽略）
```

#### Qt Widgets 项目（qmake）

```
MyApp/
├── MyApp.pro             # 项目配置
├── main.cpp              # 程序入口
├── mainwindow.cpp/h      # 主窗口类
└── mainwindow.ui         # UI 布局文件
```

## .pro 文件配置（qmake）

### 基础模板

```qmake
QT       += core gui widgets

TARGET = MyApp
TEMPLATE = app

SOURCES += \
    main.cpp \
    mainwindow.cpp

HEADERS += \
    mainwindow.h

FORMS += \
    mainwindow.ui
```

### 常用配置项

| 我要配... | .pro 语法 | 示例 |
|-----------|----------|------|
| 添加 Qt 模块 | `QT += module` | `QT += network sql` |
| 添加源文件 | `SOURCES += file.cpp` | `SOURCES += utils.cpp` |
| 添加头文件 | `HEADERS += file.h` | `HEADERS += utils.h` |
| 添加 UI 文件 | `FORMS += file.ui` | `FORMS += dialog.ui` |
| 添加资源文件 | `RESOURCES += file.qrc` | `RESOURCES += resources.qrc` |
| 包含路径 | `INCLUDEPATH += dir` | `INCLUDEPATH += $$PWD/include` |
| 链接库 | `LIBS += -Ldir -llib` | `LIBS += -L$$PWD/lib -lmylib` |
| 预处理器宏 | `DEFINES += MACRO` | `DEFINES += USE_FEATURE` |
| C++ 标准 | `CONFIG += c++17` | `CONFIG += c++17` |
| 子项目 | `SUBDIRS += dir` | `SUBDIRS += src tests` |

### 条件配置

```qmake
# Debug / Release 区分
CONFIG(debug, debug|release) {
    DEFINES += DEBUG_MODE
    LIBS += -L$$PWD/lib/debug
} else {
    LIBS += -L$$PWD/lib/release
}

# 平台区分
win32 {
    SOURCES += platform_win.cpp
}
unix {
    SOURCES += platform_linux.cpp
}
macx {
    SOURCES += platform_mac.cpp
}
```

### 变量速查

| 变量 | 含义 |
|------|------|
| `$$PWD` | 当前 .pro 文件所在目录 |
| `$$OUT_PWD` | 构建输出目录 |
| `$$PWD/../lib` | 项目的 lib 目录（相对路径） |

## CMakeLists.txt 配置（CMake）

### Qt 项目基础模板

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyApp VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)   # 自动处理 MOC
set(CMAKE_AUTOUIC ON)   # 自动处理 UIC
set(CMAKE_AUTORCC ON)   # 自动处理 RCC

find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets)

add_executable(MyApp
    main.cpp
    mainwindow.cpp
    mainwindow.h
    mainwindow.ui
    resources.qrc
)

target_link_libraries(MyApp PRIVATE
    Qt6::Core
    Qt6::Gui
    Qt6::Widgets
)
```

### 关键 CMake 变量

| 变量 | 作用 | 为什么重要 |
|------|------|-----------|
| `CMAKE_AUTOMOC` | 自动运行 MOC | 不用手动写 moc_*.cpp |
| `CMAKE_AUTOUIC` | 自动处理 .ui 文件 | 不用手动写 ui_*.h |
| `CMAKE_AUTORCC` | 自动处理 .qrc 文件 | 不用手动调用 rcc |
| `CMAKE_PREFIX_PATH` | Qt 安装路径 | 找不到 Qt 时设置此项 |

## 导入现有项目

### 导入 CMake 项目

```
1. 文件 → 打开文件或项目
2. 选择 CMakeLists.txt
3. 选择 Kit
4. 配置项目
5. 等待 CMake Configure 完成
```

### 导入 qmake 项目

```
1. 文件 → 打开文件或项目
2. 选择 .pro 文件
3. 选择 Kit
4. 配置项目
```

### 导入非 Qt 的纯 C++ 项目

```
1. 文件 → 新建文件或项目 → Import Existing Project
2. 选择项目目录
3. Qt Creator 会扫描目录结构
4. 手动调整 .includes 文件（配置头文件搜索路径）
```

## 常见问题

### 问题：找不到 Qt

```
CMake 报错 "Could not find Qt6"
├── Qt 没装？
│  → 安装 Qt（Qt Maintenance Tool 或在线安装器）
├── 装了但 CMake 找不到？
│  → 设置 CMAKE_PREFIX_PATH = /path/to/Qt/6.x.x/gcc_64
├── Kit 里的 Qt 版本没配？
│  → 工具 → 选项 → Kits → Qt Versions → 添加 qmake 路径
└── 多个 Qt 版本冲突？
   → 明确指定版本，或在 CMakePresets.json 中配置
```

### 问题：qmake 项目添加新文件后没参与编译

**原因**：.pro 文件中需要手动添加 SOURCES/HEADERS。

**解决**：在 Qt Creator 中右键项目 → 添加新文件，Qt Creator 会自动更新 .pro。如果是在文件管理器中添加的文件，需要手动编辑 .pro。

### 问题：构建目录和源码目录混在一起

**建议**：使用影子构建（Shadow Build），默认已开启。

```
项目 → 构建设置 → 构建目录
确保构建目录不是源码目录（如 build-MyApp-Desktop_Qt_6_5_0-Debug）
```
