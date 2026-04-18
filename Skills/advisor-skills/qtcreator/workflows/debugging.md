# 调试

## 调试器选择

Qt Creator 支持多种调试器，根据平台自动选择：

| 平台 | 调试器 | 说明 |
|------|--------|------|
| Windows (MSVC) | CDB | Windows 原生调试器 |
| Windows (MinGW) | GDB | MinGW 自带 |
| Linux | GDB | 默认 |
| macOS | LLDB | 默认 |

```
调试器不工作？
├── Kit 中调试器没配置？
│  → 工具 → 选项 → Kits → 检查调试器栏
├── Windows 上 CDB 没装？
│  → 安装 Windows SDK 中的 Debugging Tools
├── Linux 上 GDB 没装？
│  → sudo apt install gdb
└── macOS 上 LLDB 权限问题？
   → 系统偏好设置 → 安全与隐私 → 允许调试
```

## 基础调试流程

### 启动调试

```
1. 设置断点 → 在感兴趣的行 切换断点
2. 开始调试
3. 程序停在断点处
4. 用 逐过程 / 逐语句 / 跳出 控制执行
5. 在局部变量和表达式窗口检查变量
6. 继续运行 (F5) 到下一个断点
```

### 逐过程 vs 逐语句

```
逐语句 ──→ 进入函数内部
逐过程 ──→ 把函数调用当作一步
跳出   ──→ 当前函数跑完，停在调用者
```

| 场景 | 操作 | 原因 |
|------|------|------|
| 当前行的函数可能有 bug | 逐语句 | 需要看内部 |
| 当前行的函数是 Qt 库函数 | 逐过程 | 不需要看 Qt 内部 |
| 已进入函数但发现不是问题 | 跳出 | 快速回到调用者 |
| 想直接跑到某一行 | 运行到光标 | 比设断点更快 |

## 断点类型

### 普通断点

最常用，程序执行到该行时暂停。

### 条件断点

**设置**：
1. 右键断点（红色圆点）→ Edit Breakpoint
2. 输入条件表达式（如 `i == 42`、`str == "error"`）
3. 程序只在条件为真时暂停

**场景**：循环中只在特定条件下暂停。

### 函数断点

**设置**：
1. 调试 → 添加断点 → 在函数处中断
2. 输入函数名

**场景**：想在某函数入口暂停，但不知道函数在哪（如虚函数、回调）。

### 信号断点（Qt 特有）

**设置**：
1. 调试 → 添加断点 → 在信号处中断
2. 输入信号签名（如 `MainWindow::mySignal`）

**场景**：排查信号槽连接问题，看信号是否发出。

## 调试窗口

### 局部变量和表达式 (Locals and Expressions)

**用途**：查看当前作用域的变量和自定义表达式。

**技巧**：
- 可以添加自定义表达式（右键 → Add Expression）
- 对 QObject 派生类，会自动显示属性值
- 指针可以展开查看指向的对象
- 支持格式化：右键 → Change Format（十六进制等）

### QObject 属性查看器

Qt Creator 的调试器能自动解析 QObject 的属性：

```
查看 QObject 时可以看到：
├── 属性值（通过 Q_PROPERTY 定义的）
├── 信号和槽
├── 对象名称 (objectName)
├── 父对象和子对象列表
└── 信号连接关系
```

**用途**：快速了解一个 Widget 的状态、子控件关系、信号连接情况。

### 调用堆栈 (Stack)

**用途**：查看程序是怎么走到当前断点的。

**关键操作**：
- 双击某一帧 → 切换到该帧的上下文
- 查看每帧的局部变量

### 寄存器窗口

**用途**：查看 CPU 寄存器值，底层调试时使用。

### 线程窗口

**用途**：查看所有线程状态，多线程调试时使用。

## QML 调试

### 启用 QML 调试

```
1. 项目 → 运行设置 → 勾选 "Enable QML Debugging"
2. 使用 Debug 配置构建
3. 开始调试
```

### QML 调试特性

| 特性 | 说明 |
|------|------|
| QML 断点 | 在 .qml 文件中设断点 |
| 实时属性修改 | 调试时直接修改 QML 属性值，UI 实时更新 |
| QML 对象查看 | 查看 QML 对象树和属性 |
| JavaScript 调试 | 在 QML 中的 JS 代码中设断点 |
| QML Profiler | 分析 QML 绑定和渲染性能 |

### QML 调试策略

```
QML 界面不对？
├── 绑定值不对？→ 在 QML 中设断点，查看属性值
├── 信号没触发？→ 在 onXxx 处理器中设断点
├── 模型数据不对？→ 在 C++ 模型类中设断点
└── 想实时调样式？→ 修改属性值观察变化
```

## Qt 特有调试技巧

### 查看 QWidget 栕结构

调试时可以通过 QObject 的子对象列表查看整个 Widget 树：

```
1. 在局部变量窗口找到主窗口对象
2. 展开 children 列表
3. 看到完整的控件层级
```

**用途**：排查布局问题，确认控件是否正确嵌套。

### 使用 Q_ASSERT

```cpp
Q_ASSERT(ptr != nullptr);      // Debug 模式下检查条件
Q_ASSERT_X(condition, "where", "message");  // 带位置信息
```

**注意**：`Q_ASSERT` 只在 Debug 模式下生效，Release 模式下会被编译器移除。

### 使用 qDebug 族函数

```cpp
qDebug() << "value:" << value;       // 调试输出
qWarning() << "unexpected state";    // 警告
qCritical() << "critical error";     // 严重错误
qFatal("unrecoverable error");       // 致命错误，会终止程序
```

**在调试器中查看输出**：应用输出（Application Output）面板。

### 信号槽调试

```
信号没触发？
├── 在 emit 行设断点 → 确认是否执行到
├── 检查 connect 返回值 → 确认连接是否成功
├── 检查连接类型 → Qt::DirectConnection / QueuedConnection
└── 检查对象生命周期 → 接收者是否已被销毁

槽函数没执行？
├── 检查 connect 参数 → 信号签名和槽签名是否匹配
├── 检查连接类型 → 跨线程时用 Qt::QueuedConnection
├── 检查接收者对象 → 是否已被 delete
└── 使用信号断点 → 在信号处中断，确认是否发出
```

### 调试 Qt 事件循环

```cpp
// 在事件处理函数中设断点
void MyWidget::event(QEvent *event) {
    qDebug() << "event type:" << event->type();
    QWidget::event(event);
}
```

或使用事件过滤器：

```cpp
// 安装事件过滤器观察所有事件
qApp->installEventFilter(this);

bool MyObject::eventFilter(QObject *watched, QEvent *event) {
    qDebug() << watched << event->type();
    return false;  // 不拦截，继续传递
}
```

## 远程调试

### Linux 上远程调试嵌入式设备

```
1. 目标设备上运行 gdbserver
   gdbserver :1234 ./MyApp

2. Qt Creator 中配置
   项目 → 运行设置 → 远程执行
   主机: 目标设备 IP
   端口: 1234

3. 开始调试
```

## 常见问题

### 问题：断点不命中（灰色空心圆）

```
断点不命中
├── 构建配置是 Release？→ 切换到 Debug
├── 源码和构建产物不匹配？→ 重新构建
├── 优化导致代码被内联/消除？→ Debug 模式下不应有此问题
└── 调试器没正确附加？→ 停止调试 → 重新开始
```

### 问题：调试时看不到 Qt 类的成员

**原因**：调试器没有加载 Qt 的 pretty-printer。

**解决**：
1. 确认安装了 Qt 的调试助手（Qt Creator 通常自动配置）
2. 工具 → 选项 → 调试器 → GDB → 检查 Qt 打印器路径

### 问题：调试 QML 时断点不命中

**检查**：
1. 是否勾选了 "Enable QML Debugging"？
2. 是否使用了 Debug 配置？
3. .qml 文件是否被 QRC 正确包含？
