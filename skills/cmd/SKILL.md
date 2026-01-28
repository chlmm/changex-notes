---
name: cmd
description: Windows CMD 命令行使用指南。提供文件操作、目录管理、网络诊断、系统管理等完整命令参考。
execution_mode: ai
metadata:
  category: command-line
  platform: [windows]
  tags: [cmd, command-line, windows, batch, shell]
---

# Windows CMD 使用指南

## 概述

Windows CMD（命令提示符）是 Windows 操作系统自带的命令行工具，提供对系统底层的控制能力。通过命令行可以高效地完成文件管理、系统配置、网络诊断等各种任务。

## 适用场景

- **批量处理文件** - 比图形界面更高效
- **系统管理维护** - 网络诊断、进程管理、用户管理
- **自动化脚本** - 编写批处理脚本 (.bat) 自动执行重复任务
- **故障排查** - 系统无法正常启动时进入安全模式使用命令行修复

## 打开 CMD 的方式

| 方式 | 操作步骤 |
|------|----------|
| **快捷键** | `Win + R` 输入 `cmd` 回车 |
| **开始菜单** | 右键开始菜单 → 命令提示符 / Windows PowerShell |
| **管理员权限** | 上述方式 + `Ctrl + Shift + Enter` |
| **文件资源管理器** | 地址栏输入 `cmd` 回车（在当前目录打开） |

## 命令速查表

完整的 CMD 命令参考：
📄 **[reference/commands.md](reference/commands.md)**

### 按需查询方法

由于命令较多，建议通过标签筛选按需查询：

```bash
# 1. 按资源类型筛选
grep "file" reference/commands.md      # 文件操作命令
grep "dir" reference/commands.md       # 目录操作命令
grep "network" reference/commands.md   # 网络操作命令
grep "system" reference/commands.md    # 系统信息命令
grep "process" reference/commands.md   # 进程管理命令

# 2. 按操作类型筛选
grep "copy" reference/commands.md      # 复制命令
grep "delete" reference/commands.md    # 删除命令
grep "create" reference/commands.md    # 创建命令
grep "search" reference/commands.md    # 搜索命令

# 3. 按使用场景筛选
grep "daily" reference/commands.md     # 日常使用命令
grep "admin" reference/commands.md     # 管理员命令
grep "backup" reference/commands.md    # 备份相关命令
```

## 常用工作流

### 工作流 1：批量重命名文件

```batch
@echo off
setlocal enabledelayedexpansion
set /a count=1
for %%f in (*.txt) do (
    ren "%%f" "document_!count!.txt"
    set /a count+=1
)
echo 完成！
pause
```

### 工作流 2：清理临时文件

```batch
@echo off
echo 开始清理临时文件...

:: 删除系统临时文件
del /q /f /s %TEMP%\*

:: 删除 Windows 临时文件
del /q /f /s C:\Windows\Temp\*

:: 清空回收站
echo Y | powershell -Command "Clear-RecycleBin -Confirm:$false"

echo 清理完成！
pause
```

### 工作流 3：网络故障诊断

```batch
@echo off
echo ===== 网络诊断工具 =====
echo.

:: 1. 显示网络配置
echo [1/5] 网络配置信息...
ipconfig /all > network_info.txt
echo 已保存到 network_info.txt

:: 2. 测试网关连通性
echo [2/5] 测试网关连通性...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr "Default Gateway"') do (
    ping -n 4 %%a
)

:: 3. 测试外网连通性
echo [3/5] 测试外网连通性...
ping -n 4 www.baidu.com

:: 4. 清空 DNS 缓存
echo [4/5] 清空 DNS 缓存...
ipconfig /flushdns

:: 5. 显示网络连接状态
echo [5/5] 当前网络连接...
netstat -an

echo.
echo ===== 诊断完成 =====
pause
```

### 工作流 4：定时备份文件夹

```batch
@echo off
set SOURCE=C:\Users\Username\Documents
set DEST=D:\Backup
set DATE=%date:~0,4%%date:~5,2%%date:~8,2%
set BACKUP_DIR=%DEST%\Backup_%DATE%

echo 开始备份...
echo 源目录: %SOURCE%
echo 目标目录: %BACKUP_DIR%

:: 创建日期目录
if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"

:: 复制文件（包含子目录）
xcopy "%SOURCE%\*" "%BACKUP_DIR%\" /s /e /h /y

echo 备份完成！
echo 备份位置: %BACKUP_DIR%
pause
```

## 最佳实践

### 路径处理

```cmd
:: 包含空格的路径使用引号
cd "C:\Program Files\My App"

:: 使用相对路径
cd ..           :: 上级目录
cd \            :: 根目录
cd \folder\sub  :: 绝对路径

:: 使用环境变量
cd %USERPROFILE%\Documents
cd %TEMP%
```

### 批处理脚本编写

```batch
@echo off              :: 关闭命令回显
setlocal               :: 开始本地化环境变量
set var=value          :: 设置变量
echo %var%             :: 使用变量
if exist file.txt (    :: 条件判断
    echo 文件存在
) else (
    echo 文件不存在
)
for %%i in (*) do (    :: 循环
    echo %%i
)
pause                  :: 暂停等待按键
exit /b 0              :: 退出并返回代码
```

### 错误处理

```batch
@echo off
command1
if %errorlevel% neq 0 (
    echo 命令1执行失败
    exit /b 1
)
command2
if %errorlevel% neq 0 (
    echo 命令2执行失败
    goto error_handler
)
echo 全部成功
exit /b 0

:error_handler
echo 发生错误，错误码: %errorlevel%
pause
exit /b %errorlevel%
```

## 常见问题

**Q: 如何以管理员身份运行 CMD？**
```
方法1: 右键开始菜单 → 命令提示符(管理员)
方法2: Win+X → A (Windows PowerShell 管理员)
方法3: Ctrl+Shift+Enter 以管理员身份运行
```

**Q: 命令太长如何换行？**
```batch
:: 使用 ^ 换行
long_command param1 ^
               param2 ^
               param3
```

**Q: 如何查看命令的帮助信息？**
```cmd
command /?          :: 查看具体命令帮助
help                :: 查看所有命令列表
help command        :: 查看特定命令帮助
```

**Q: 如何重定向输出到文件？**
```cmd
command > file.txt      :: 覆盖输出到文件
command >> file.txt     :: 追加输出到文件
command 2> error.txt    :: 仅重定向错误
command > out.txt 2>&1  :: 输出和错误都重定向
```

## 进阶工具

| 工具 | 用途 | 启动命令 |
|------|------|----------|
| **PowerShell** | 更强大的脚本环境 | `powershell` |
| **Windows Terminal** | 现代化终端 | `wt` |
| **WSL** | Linux 子系统 | `wsl` |

## 资源

- **官方文档**: https://docs.microsoft.com/windows-server/administration/windows-commands/windows-commands
- **批处理教程**: https://ss64.com/nt/
- **原文件位置**: `工具/softs/cmd/cmd_base.md`

## 相关技能

- **powershell** - 更现代的 Windows 命令行
- **bash** - Linux/macOS 命令行
- **git-workflow** - 版本控制命令
