# 构建与编译

## 构建决策树

```
你要构建什么？
├── 当前项目 ──→ 构建项目
├── 所有项目 ──→ 构建全部
├── 清理后重新构建 ──→ 重新构建
├── 只想运行 ──→ 运行（自动构建未修改的不再重编）
└── 构建卡住了 ──→ 取消构建
```

## 构建配置

### Debug vs Release

| | Debug | Release |
|---|-------|---------|
| 优化 | 禁用 (`-O0`) | 启用 (`-O2`/`-O3`) |
| 调试信息 | 有 (`-g`) | 可选 |
| 断言 | 启用 | 禁用 (`NDEBUG`) |
| Qt 日志输出 | 完整 | 可能被 `QT_NO_DEBUG_OUTPUT` 屏蔽 |
| 体积 | 大 | 小 |

### 切换构建配置

```
1. 左侧项目面板 → 选择构建配置
2. Debug / Release / Profile（可选）
3. 构建项目
```

## qmake 构建配置

### CONFIG 变量

`CONFIG` 是 qmake 最重要的控制变量：

```qmake
# 构建类型（二选一）
CONFIG += debug          # Debug 模式
CONFIG += release        # Release 模式
CONFIG += debug_and_release  # 同时构建两种

# C++ 标准
CONFIG += c++17

# Qt 模块
QT += core gui widgets network sql

# 控制台应用
CONFIG += console

# 静态链接运行时（MSVC）
CONFIG += static_runtime

# 警告
CONFIG += warn_on        # 开启警告
```

### 常见构建问题

#### 问题：undefined reference to `vtable for MyClass`

**原因**：Qt 的 MOC 没有处理你的 Q_OBJECT 类。

**解决**：
1. 确认 .h 文件在 HEADERS 中
2. 确认类声明中有 `Q_OBJECT` 宏
3. 清理 → 重新构建（MOC 文件可能过期）

#### 问题：No rule to make target `moc_xxx.cpp`

**原因**：头文件被移动或重命名，但 .pro 没更新。

**解决**：
1. 检查 HEADERS 中的文件路径是否正确
2. 清理 → 重新构建

## CMake 构建配置

### CMake 配置流程

```
1. 打开 CMake 项目
2. Qt Creator 自动运行 CMake Configure
3. 查看 CMake 输出（编译输出面板）
4. 如有错误 → 修改 CMakeLists.txt → 重新配置
```

### 手动触发 CMake Configure

```
项目 → 构建设置 → CMake → 运行 CMake
```

### CMake 常见配置问题

#### 问题：CMake 找不到 Qt

```cmake
# 方案一：在 CMakeLists.txt 中指定
set(CMAKE_PREFIX_PATH "C:/Qt/6.5.0/msvc2019_64")

# 方案二：在 Qt Creator 中配置
# 项目 → 构建设置 → CMake → Initial Configuration
# 添加 CMAKE_PREFIX_PATH 变量
```

#### 问题：AUTOMOC 没生效

```cmake
# 确认这三项已开启
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
```

**注意**：如果用了 AUTOMOC 但某些 .cpp 文件仍然报 MOC 相关错误，可能需要 `#include "moc_xxx.cpp"` 手动包含。

## MOC / UIC / RCC 理解

Qt 的编译管线有三个预处理器，理解它们是排查构建问题的基础：

| 工具 | 输入 | 输出 | 触发条件 | 自动化 |
|------|------|------|---------|--------|
| **MOC** | 含 Q_OBJECT 的 .h | moc_*.cpp | 头文件中出现 Q_OBJECT | AUTOMOC |
| **UIC** | .ui 文件 | ui_*.h | FORMS 中列出 .ui | AUTOUIC |
| **RCC** | .qrc 文件 | qrc_*.cpp | RESOURCES 中列出 .qrc | AUTORCC |

### 什么时候需要手动处理

| 场景 | 解决方案 |
|------|---------|
| 类声明在 .cpp 中且含 Q_OBJECT | 在 .cpp 末尾加 `#include "xxx.moc"` |
| .ui 文件修改后没更新 | 清理 → 重新构建 |
| .qrc 添加了新资源但没生效 | 确认 .qrc 文件在 RESOURCES/资源中列出 |

## 编译错误排查策略树

```
编译报错
├── 语法错误
│  → 看行号定位，读错误信息
├── 找不到头文件
│  ├── Qt 头文件？ → 检查 QT += 对应模块
│  ├── 项目头文件？ → 检查 INCLUDEPATH / include_directories
│  └── 第三方库？ → 检查包含路径配置
├── undefined reference / LNK2019
│  ├── Qt 模块函数？ → 检查 QT += 对应模块 / target_link_libraries
│  ├── 自己的函数？ → 检查 SOURCES 是否包含对应 .cpp
│  └── 第三方库？ → 检查 LIBS / link_libraries
├── vtable 相关错误
│  → 见上方 MOC 问题排查
└── 重新构建后仍有问题
   → 清除 → 重新构建（清理 CMake 缓存 / .obj 文件）
```

## 编译优化技巧

### 加快编译速度

| 方法 | 效果 | 操作 |
|------|------|------|
| 预编译头 | ⭐⭐⭐ | CMake: `target_precompile_headers`；qmake: `PRECOMPILED_HEADER = pch.h` |
| 并行编译 | ⭐⭐ | CMake: `cmake --build . -j8`；qmake: `make -j8` |
| Unity Build | ⭐⭐ | CMake: `set(CMAKE_UNITY_BUILD ON)` |
| 减少头文件包含 | ⭐⭐ | 前向声明替代不必要的 #include |
| 增量构建 | ⭐ | 默认启用，不要每次都重新构建 |

### Qt 特有的编译时间优化

| 方法 | 说明 |
|------|------|
| 减少 Q_OBJECT 使用 | 不需要信号槽的类不要加 Q_OBJECT |
| 避免 QObject 多重继承 | 增加 MOC 处理时间 |
| PCH 包含常用 Qt 头文件 | `<QObject>`, `<QString>`, `<QWidget>` 等 |

## 常见问题

### 问题：修改了 .pro / CMakeLists.txt 但没生效

**解决**：
- qmake：右键项目 → Run qmake → 重新构建
- CMake：项目 → 构建设置 → 运行 CMake → 重新构建

### 问题：Debug 模式下 qDebug 没输出

**检查**：
- 是否定义了 `QT_NO_DEBUG_OUTPUT`？
- 输出面板是否选择了正确的输出通道？
- 应用输出（Application Output）面板查看
