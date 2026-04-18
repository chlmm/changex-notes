# Qt 特有工作流

## 信号槽

### 连接方式对比

| 方式 | 语法 | 编译检查 | 适合 |
|------|------|---------|------|
| 函数指针（Qt 5+推荐） | `connect(sender, &Sender::signal, receiver, &Receiver::slot)` | ✅ 编译时检查 | 大多数情况 |
| Functor | `connect(sender, &Sender::signal, [=](){} )` | ✅ | 简单单次逻辑 |
| 字符串（Qt 4 风格） | `connect(sender, SIGNAL(signal()), receiver, SLOT(slot()))` | ❌ 运行时才报错 | 不推荐 |

### 信号槽工作流

```
我要让 A 的动作触发 B 的响应
1. 确定 A 发出什么信号（如 clicked、textChanged）
2. 确定 B 应该执行什么（已有槽？还是新建？）
3. 选择 connect 方式
4. 在合适的位置调用 connect（通常是构造函数）
```

### 常见信号速查

| 控件 | 信号 | 触发时机 |
|------|------|---------|
| QPushButton | clicked() | 点击按钮 |
| QLineEdit | textChanged(QString) | 文本改变 |
| | returnPressed() | 按回车 |
| QComboBox | currentIndexChanged(int) | 选中项改变 |
| QCheckBox | stateChanged(int) | 勾选状态改变 |
| QSlider | valueChanged(int) | 滑块值改变 |
| QTabWidget | currentChanged(int) | 标签页切换 |
| QTimer | timeout() | 定时器超时 |

### 自定义信号槽

```cpp
// 发送者类
class Sender : public QObject {
    Q_OBJECT
signals:
    void dataReady(const QString &data);  // 信号声明（无需实现）
};

// 接收者类
class Receiver : public QObject {
    Q_OBJECT
public slots:
    void onDataReady(const QString &data) {  // 槽声明
        // 处理数据
    }
};

// 连接
connect(sender, &Sender::dataReady, receiver, &Receiver::onDataReady);
```

**关键规则**：
- 信号只需要声明，不需要实现（MOC 生成实现）
- 槽函数可以是任意成员函数（`public slots` / `private slots` / 无标记均可）
- 信号和槽的参数必须匹配，槽的参数不能多于信号
- 发射信号用 `emit` 关键字（可选，但推荐写）

### 信号槽调试策略

```
信号槽没生效？
├── connect 返回值检查
│  auto conn = connect(...);
│  if (!conn) qWarning() << "connect failed!";
├── 检查信号签名是否匹配
│  → 参数类型必须完全一致
├── 检查对象生命周期
│  → sender/receiver 是否已被 delete
├── 跨线程问题？
│  → 默认 Qt::AutoConnection，跨线程时用 QueuedConnection
└── 检查是否重复连接
   → 同一个 connect 调用多次，槽会执行多次
```

## 资源系统 (.qrc)

### 什么时候用资源系统

```
需要嵌入小文件到可执行文件中？
├── 图标、图片 ──→ 用 qrc
├── QML 文件 ──→ 用 qrc
├── 配置文件 ──→ 用 qrc
└── 大文件（视频等）───→ 不要用 qrc，用外部文件
```

### 创建和编辑 qrc 文件

```
1. 项目中添加新文件 → Qt → Qt Resource File
2. 命名（如 resources.qrc）
3. 在 Qt Creator 的资源编辑器中：
   ├── 添加前缀（如 /images）
   └── 添加文件到前缀下
```

### qrc 文件结构

```xml
<RCC>
    <qresource prefix="/images">
        <file>icon.png</file>
        <file>logo.png</file>
    </qresource>
    <qresource prefix="/qml">
        <file>Main.qml</file>
    </qresource>
</RCC>
```

### 在代码中使用资源

```cpp
// 资源路径格式:  :/前缀/文件名
QPixmap pixmap(":/images/icon.png");
QIcon icon(":/images/logo.png");

// QML 中
Image { source: "qrc:/images/icon.png" }
```

### 注意事项

- 资源文件是只读的，运行时不能修改
- 资源会被编译进二进制文件，增大体积
- 大量图片资源考虑用 Qt 资源系统的别名机制
- 修改 qrc 中的文件后需要重新构建

## 翻译系统 (.ts)

### 翻译工作流

```
1. 代码中使用 tr() 包裹可翻译文本
   label->setText(tr("Hello World"));

2. 更新翻译文件
   → 工具 → 外部 → Qt Linguist → 更新翻译 (lupdate)

3. 用 Qt Linguist 翻译
   → 打开 .ts 文件 → 逐条翻译

4. 发布翻译
   → 工具 → 外部 → Qt Linguist → 发布翻译 (lrelease)
   → 生成 .qm 文件

5. 在代码中加载翻译
   QTranslator translator;
   translator.load(":/translations/app_zh_CN.qm");
   app.installTranslator(&translator);
```

### tr() 使用规范

```cpp
// ✅ 正确
label->setText(tr("Hello"));
setText(tr("File: %1").arg(filename));

// ❌ 错误 — 变量不能被翻译工具提取
setText(msg);           // 应该用 tr()
setText("Hello " + name); // 应该用 tr("Hello %1").arg(name)

// ✅ 带上下文的 tr
QT_TR_NOOP("Hardcoded Text");  // 标记但不在类中使用
```

## QML 工作流

### QML 与 C++ 的分工

```
QML 负责：界面外观、动画、交互反馈
C++ 负责：业务逻辑、数据处理、硬件交互
```

### QML 基础结构

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: root
    width: 640
    height: 480
    title: qsTr("My App")

    Button {
        anchors.centerIn: parent
        text: qsTr("Click Me")
        onClicked: console.log("clicked")
    }
}
```

### QML 与 C++ 交互

#### C++ 暴露数据给 QML

```cpp
// 方式一：设置上下文属性
engine.rootContext()->setContextProperty("myModel", &dataModel);

// 方式二：注册 QML 类型
qmlRegisterType<MyItem>("MyModule", 1, 0, "MyItem");
```

#### QML 调用 C++ 方法

```cpp
// C++ 侧：用 Q_INVOKABLE 或 Q_PROPERTY
class Backend : public QObject {
    Q_OBJECT
    Q_PROPERTY(QString name READ name WRITE setName NOTIFY nameChanged)
public:
    Q_INVOKABLE void doSomething();
};
```

```qml
// QML 侧
Backend {
    id: backend
    Component.onCompleted: backend.doSomething()
}
```

### QML 热重载

Qt Creator 支持 QML 热重载，修改 QML 文件后界面实时更新：

```
1. 使用 Debug 配置运行
2. 修改 .qml 文件并保存
3. 按 Ctrl+Shift+R 或点击应用输出中的 "Reload" 按钮
4. 界面即时更新
```

**限制**：
- 只能热重载 QML 部分，C++ 修改需要重新编译
- 新增的 QML 组件可能需要重启
- 信号槽连接的修改可能不完全热重载

## Qt 常用工具类速查

| 类 | 用途 | 常用场景 |
|----|------|---------|
| QString | 字符串 | 几乎所有文本操作 |
| QVariant | 类型擦除容器 | 信号槽传参、设置值 |
| QStringList | 字符串列表 | 文件列表、选项列表 |
| QMap / QHash | 关联容器 | 键值对映射 |
| QList / QVector | 序列容器 | 有序元素集合 |
| QJsonDocument | JSON 处理 | 配置文件、网络通信 |
| QSettings | 持久化配置 | 保存用户偏好 |
| QTimer | 定时器 | 延迟执行、周期性任务 |
| QThread | 线程 | 后台任务 |
| QDir / QFile | 文件系统 | 读写文件、遍历目录 |

## 常见问题

### 问题：信号槽连接后槽被调用多次

**原因**：同一个 connect 被调用了多次。

**解决**：
- 确认 connect 只调用一次（检查是否在循环或事件处理中调用了 connect）
- Qt 5.15+ 可以用 `QObject::connect` 返回的 `QMetaObject::Connection` 断开

### 问题：qrc 文件修改后没生效

**解决**：清理 → 重新构建。RCC 可能有缓存。

### 问题：tr() 翻译不生效

```
排查
├── .qm 文件是否生成了？→ 运行 lrelease
├── .qm 文件路径对不对？→ 检查 load() 的路径
├── installTranslator 的时机？→ 必须在创建 UI 之前
└── 翻译文件中有没有对应条目？→ 用 Qt Linguist 检查
```
