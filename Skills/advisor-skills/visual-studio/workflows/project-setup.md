# 项目搭建

## 决策树：选择项目类型

```
你需要什么？
├─ 标准桌面应用/库
│  ├─ 需要 CMake 管理？─── 是 ──→ CMake 项目（见 cmake-workflow）
│  └─ 不需要 ──→ MSBuild 项目
│     ├─ 控制台程序 ──→ Windows Desktop Wizard → Console App
│     ├─ 桌面 GUI ──→ Windows Desktop Wizard → Desktop Application
│     └─ 静态库/动态库 ──→ Windows Desktop Wizard → Static/Dynamic Library
├─ 跨平台项目 ──→ CMake 项目（见 cmake-workflow）
└─ 只想快速验证代码 ──→ Console App（最简模板）
```

## MSBuild 项目搭建流程

### 1. 创建项目

1. 文件 → 新建 → 项目
2. 搜索 "C++"，选择合适的模板
3. 填写项目名、位置、解决方案名
4. 点击创建

### 2. 配置属性页

项目创建后，右键项目 → 属性，进入属性页。以下是最常需要配置的项目：

#### 包含目录（Additional Include Directories）

- **路径**: C/C++ → 常规 → 附加包含目录
- **用途**: 告诉编译器去哪找 `.h` 文件
- **常见值**: 第三方库的 include 路径，如 `$(SolutionDir)include\`
- **注意**: 使用相对路径时基于项目目录，可用 `$(SolutionDir)`、`$(ProjectDir)` 宏

#### 库目录（Library Directories）

- **路径**: 链接器 → 常规 → 附加库目录
- **用途**: 告诉链接器去哪找 `.lib` 文件

#### 链接依赖（Additional Dependencies）

- **路径**: 链接器 → 输入 → 附加依赖项
- **用途**: 指定需要链接的 `.lib` 文件名
- **注意**: 只写文件名（如 `mylib.lib`），路径在库目录中配置

#### 预处理器定义（Preprocessor Definitions）

- **路径**: C/C++ → 预处理器 → 预处理器定义
- **用途**: 定义宏，如 `_UNICODE`、`NDEBUG`、自定义条件编译宏

### 3. 配置管理

**关键概念**：VS 有两个维度管理配置：

| 维度 | 含义 | 常见值 |
|------|------|--------|
| **Configuration** | 编译模式 | Debug / Release |
| **Platform** | 目标平台 | x64 / Win32 / ARM64 |

**注意**：修改属性时确认当前选中的 Configuration 和 Platform 是否正确。常见错误是在 Debug 下改了属性但 Release 没改，导致 Release 编译失败。

### 4. 添加现有文件

1. 在解决方案资源管理器中右键项目
2. 添加 → 现有项
3. 选择 `.cpp` / `.h` 文件

**注意**：VS 不会自动包含目录下的所有文件（不像 CMake 的 `file(GLOB)`），每个文件必须显式添加到项目中。

### 5. 添加新文件

1. 右键项目 → 添加 → 新建项
2. 选择 C++ 文件 (.cpp) 或头文件 (.h)
3. 命名并确认

## 常见问题

### 问题：找不到头文件

**诊断路径**：

```
编译报错 "cannot open include file"
├─ 头文件路径没加到包含目录？
│  → 属性 → C/C++ → 常规 → 附加包含目录
├─ 路径写对了但平台选错了？
│  → 检查当前 Configuration/Platform 是否匹配
└─ 拼写问题？
   → 检查大小写，Windows 不区分但最好保持一致
```

### 问题：链接错误 LNK2019

**诊断路径**：

```
链接报错 "unresolved external symbol"
├─ .lib 文件没加？
│  → 属性 → 链接器 → 输入 → 附加依赖项
├─ 库目录没配？
│  → 属性 → 链接器 → 常规 → 附加库目录
├─ Debug/Release 不匹配？
│  → 确认链接的 lib 是对应 Configuration 编译的
└─ 函数签名不匹配？
   → 检查声明和定义是否一致（参数类型、调用约定）
```

### 问题：Debug 能跑但 Release 崩溃

**常见原因**：
- 使用了未初始化的变量（Debug 模式下内存会被清零）
- 链接了 Debug 版本的 lib
- 代码中有未定义行为（UB），Debug 下碰巧没触发

## 属性配置速查

| 我要配... | 属性页路径 |
|-----------|-----------|
| 头文件搜索路径 | C/C++ → 常规 → 附加包含目录 |
| lib 搜索路径 | 链接器 → 常规 → 附加库目录 |
| 链接哪些 lib | 链接器 → 输入 → 附加依赖项 |
| 预处理器宏 | C/C++ → 预处理器 → 预处理器定义 |
| C++ 标准版本 | C/C++ → 语言 → C++ 语言标准 |
| 运行库 | C/C++ → 代码生成 → 运行库 |
| 输出目录 | 常规 → 输出目录 |
| 中间目录 | 常规 → 中间目录 |
