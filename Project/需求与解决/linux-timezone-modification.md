# Linux 系统时区修改指南

本文档介绍如何在 Linux 系统中查看和修改时区设置。

## 1. 查看当前时区

在修改时区之前，首先需要了解当前系统的时区设置。

### 1.1 使用 date 命令查看时区

```bash
date
```

输出示例：
```
Thu Jan 25 01:29:50 CST 2024
```

或者使用 RFC-2822 格式：
```bash
date -R
```

输出示例：
```
Thu, 25 Jan 2024 01:29:50 +0800
```

其中 `+0800` 表示东八区（CST - China Standard Time）。

### 1.2 使用 timedatectl 命令查看时区（推荐）

```bash
timedatectl
```

输出示例：
```
               Local time: Thu 2024-01-25 01:29:50 CST
           Universal time: Wed 2024-01-24 17:29:50 UTC
                 RTC time: Wed 2024-01-24 17:29:50
                Time zone: Asia/Shanghai (CST, +0800)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

## 2. 查找可用时区

可以使用以下命令查看系统支持的所有时区：

```bash
timedatectl list-timezones
```

或者查找特定区域的时区：

```bash
timedatectl list-timezones | grep Asia
```

## 3. 修改时区

### 3.1 永久修改时区（推荐方法）

使用 timedatectl 命令（现代 Linux 系统）：

```bash
sudo timedatectl set-timezone Asia/Shanghai
```

### 3.2 传统方法：创建软链接

```bash
sudo ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

### 3.3 临时修改时区

仅在当前会话中修改时区：

```bash
export TZ='Asia/Shanghai'
```

## 4. 验证时区修改

修改完成后，使用以下命令验证时区是否已正确设置：

```bash
timedatectl
```

或

```bash
date -R
```

## 5. 注意事项

1. 修改时区可能需要管理员权限（sudo）
2. 使用 `timedatectl` 是现代 Linux 系统推荐的方法
3. 修改时区后，某些服务可能需要重启才能应用新的时区设置
4. 在容器环境中，时区设置可能与宿主机不同

## 6. 参考资料

- Linux 系统管理手册
- systemd 文档
- tzselect 命令手册