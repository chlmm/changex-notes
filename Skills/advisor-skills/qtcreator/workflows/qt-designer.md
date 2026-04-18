# Qt Designer / UI 设计

## 概述

Qt Designer 是 Qt Creator 内置的可视化 UI 设计工具，用于设计 QtWidgets 界面。它生成 `.ui` 文件（XML 格式），编译时由 UIC 转换为 `ui_xxx.h`。

## 打开方式

```
1. 双击项目中的 .ui 文件
2. Qt Creator 自动切换到 Design 模式
3. 出现设计器界面：左侧控件箱 + 中间画布 + 右侧属性/信号槽面板
```

## 设计器界面布局

```
┌──────────────────────────────────────────────────┐
│ 工具栏（布局、预览、信号槽编辑）                      │
├─────────┬────────────────────┬───────────────────┤
│ 控件箱   │   画布（Form）      │ 属性编辑器         │
│ Widget   │                    │ Property          │
│ Box      │                    │ Editor            │
│         │                    │                   │
│         │                    ├───────────────────┤
│         │                    │ 信号/槽编辑器       │
│         │                    │ Signal/Slot       │
│         │                    │ Editor            │
├─────────┴────────────────────┴───────────────────┤
│ 对象检查器（Object Inspector）                      │
│ 控件层级树                                         │
└──────────────────────────────────────────────────┘
```

## 工作流：设计一个界面

### 1. 选择主窗口类型

| 类型 | 适合 | 对应类 |
|------|------|--------|
| Main Window | 带菜单栏/工具栏/状态栏的主窗口 | QMainWindow |
| Widget | 简单窗口/对话框 | QWidget |
| Dialog | 对话框（带确定/取消按钮） | QDialog |

### 2. 拖放控件

```
1. 从控件箱中拖控件到画布
2. 调整位置和大小
3. 在属性编辑器中修改属性
```

### 常用控件速查

| 分类 | 控件 | 用途 |
|------|------|------|
| 按钮 | QPushButton | 点击触发操作 |
| | QCheckBox | 勾选框 |
| | QRadioButton | 单选按钮 |
| | QToolButton | 工具栏按钮 |
| 输入 | QLineEdit | 单行文本输入 |
| | QTextEdit | 多行富文本 |
| | QSpinBox | 整数输入（带上下箭头） |
| | QDoubleSpinBox | 浮点数输入 |
| | QComboBox | 下拉选择 |
| 展示 | QLabel | 文本/图片标签 |
| | QProgressBar | 进度条 |
| | QLCDNumber | LCD 数字显示 |
| 容器 | QGroupBox | 分组框 |
| | QTabWidget | 标签页 |
| | QScrollArea | 滚动区域 |
| | QSplitter | 可拖动分割 |
| 列表 | QListView | 列表视图 |
| | QTreeView | 树形视图 |
| | QTableView | 表格视图 |

### 3. 设置布局

**布局是 Qt Designer 的核心**。不设布局的界面窗口大小变化时控件不会自动调整。

```
选择控件的父容器 → 右键 → 布局
├── 水平布局 (Horizontal)    → 控件左右排列
├── 垂直布局 (Vertical)      → 控件上下排列
├── 网格布局 (Grid)          → 控件按网格排列
├── 表单布局 (Form)          → 标签+输入框两列排列
└── 打破布局 (Break)         → 取消布局
```

**布局策略**：

```
设计界面的布局思路
├── 先放控件，大致排好位置
├── 选择同一层的控件 → 应用水平/垂直布局
├── 对嵌套的容器 → 逐层设布局
├── 最外层窗口 → 也设布局
└── 用拉伸因子 (stretch) 控制比例
```

### 4. 设置属性

在属性编辑器中修改控件属性：

| 常用属性 | 说明 | 示例 |
|----------|------|------|
| objectName | 控件的对象名，代码中通过此名访问 | `btnSubmit` |
| text | 显示文本 | `"提交"` |
| enabled | 是否可用 | true / false |
| visible | 是否可见 | true / false |
| tooltip | 鼠标悬停提示 | `"点击提交"` |
| stylesheet | Qt 样式表 | `"color: red;"` |

**objectName 命名建议**：

| 控件类型 | 前缀 | 示例 |
|----------|------|------|
| QPushButton | btn | btnOk, btnCancel |
| QLabel | lbl | lblTitle, lblStatus |
| QLineEdit | edit | editName, editPassword |
| QComboBox | combo | comboLanguage |
| QCheckBox | chk | chkRemember |
| QSpinBox | spin | spinAge |
| QTableWidget | table | tableData |

### 5. 信号槽连接

**在设计器中连接信号槽**：

```
1. 工具栏点击 "编辑信号/槽" 图标（或 F4）
2. 在发射信号的控件上拖拽到接收控件
3. 选择信号和槽
4. 确定
```

**注意**：设计器中的信号槽连接是静态的，在 `ui_xxx.h` 的 `setupUi()` 中生成。只能连接控件已有的信号和槽，不能连接自定义槽。

**自定义槽的连接**：在代码中用 `connect()` 手动连接。

### 6. 预览

```
工具栏 → 预览 (Ctrl+Alt+R)
├── 查看界面效果
├── 测试布局在不同大小下的表现
└── 关闭预览 → 回到设计器
```

### 7. 保存

保存 .ui 文件后，下次构建时 UIC 会自动重新生成 `ui_xxx.h`。

## 在代码中使用 UI

### 方式一：多重继承（推荐）

```cpp
// mainwindow.h
#include <QMainWindow>
QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow {
    Q_OBJECT
public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
private:
    Ui::MainWindow *ui;    // UI 指针
};
```

```cpp
// mainwindow.cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    // 通过 ui-> 访问控件
    connect(ui->btnOk, &QPushButton::clicked, this, &MainWindow::onOk);
}

MainWindow::~MainWindow() {
    delete ui;
}
```

### 访问控件的规律

```
设计器中 objectName 为 "btnOk" 的控件
→ 代码中通过 ui->btnOk 访问
```

### 自动关联的槽函数

Qt 会自动将命名规则为 `on_objectName_signal` 的槽函数与对应控件的信号连接：

```cpp
// 不需要手动 connect，Qt 自动连接
void MainWindow::on_btnOk_clicked() {
    // btnOk 的 clicked 信号触发时自动调用
}
```

**注意**：这种自动关联只在 `setupUi()` 中设置，且要求槽函数命名严格匹配。

## 策略树：UI 问题排查

```
界面不对？
├── 控件没显示？
│  ├── 布局是否正确？→ 检查布局设置
│  ├── visible 属性是否为 true？
│  └── 父容器是否太小？
├── 大小不对？
│  ├── 没设布局？→ 设置布局
│  ├── sizePolicy 不对？→ 修改 sizePolicy
│  └── 最小/最大尺寸限制？→ 检查 minimumSize/maximumSize
├── 样式不对？
│  ├── stylesheet 语法错误？→ 检查 CSS 语法
│  └── 需要调 QSS？→ 参考 Qt 样式表文档
└── 信号槽没响应？
   ├── objectName 是否匹配？→ 检查命名
   ├── 槽函数命名是否符合 on_xxx_yyy 规则？
   └── 是否手动 connect 了？→ 检查 connect 语句
```

## 常见问题

### 问题：修改了 .ui 但代码中看不到变化

**原因**：UIC 还没重新生成 `ui_xxx.h`。

**解决**：构建项目，或手动运行 UIC。

### 问题：设计器中控件被其他控件遮挡，选不中

**解决**：
- 在对象检查器（Object Inspector）中选中目标控件
- 或在画布上右键 → 选择被遮挡的控件

### 问题：布局混乱，想重新开始

**解决**：
1. 右键容器 → 打破布局
2. 重新拖放控件
3. 重新设置布局
