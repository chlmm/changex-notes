---
type: reference
category: cmd
title: Windows CMD 命令速查表
description: 完整的 Windows 命令行命令参考，带标签分类便于筛选查询
---

# Windows CMD 命令速查表

## 使用说明

本表格包含第六列"标签"，可通过 grep/sed 等工具按需筛选：

```bash
# 按分类筛选（如所有文件操作命令）
grep "文件操作" commands.md

# 按标签筛选（如所有删除相关命令）
grep "delete" commands.md

# 按关键词搜索
grep "复制" commands.md
```

## 标签说明

| 标签 | 含义 |
|------|------|
| `file` | 文件操作 |
| `dir` | 目录操作 |
| `disk` | 磁盘操作 |
| `network` | 网络操作 |
| `system` | 系统信息 |
| `process` | 进程管理 |
| `user` | 用户管理 |
| `env` | 环境变量 |
| `daily` | 日常使用 |
| `admin` | 管理员权限 |
| `backup` | 备份相关 |
| `search` | 搜索查询 |
| `help` | 帮助信息 |

---

## 快捷操作与帮助

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 帮助 | `help` | 查看帮助信息 | `help` | 显示命令帮助 | help,daily |
| 快捷操作 | `tab` | 自动补全命令 | `tab` | 自动补全当前输入的命令 | shortcut,daily |
| 历史记录 | `↑ / ↓` | 查看历史命令 | `↑` / `↓` | 浏览之前执行过的命令 | shortcut,daily |
| 其他实用 | `cls` | 清屏 | `cls` | 清除命令行窗口的所有内容 | util,daily |
| 其他实用 | `exit` | 退出 CMD | `exit` | 关闭命令行窗口 | util,daily |
| 其他实用 | `pause` | 暂停执行 | `pause` | 暂停程序执行，按任意键继续 | util,script |
| 其他实用 | `timeout /t 5` | 延迟执行 | `timeout /t 5` | 延迟5秒后继续执行 | util,script |
| 其他实用 | `color 0a` | 修改窗口颜色 | `color 0a` | 黑色背景浅绿色文字 | util,ui |
| 其他实用 | `title My Window` | 修改窗口标题 | `title My Window` | 设置窗口标题 | util,ui |

---

## 电源管理命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 电源管理 | `shutdown /s` | 关机 | `shutdown /s` | 立即关闭计算机 | power,shutdown,admin |
| 电源管理 | `shutdown /r` | 重启 | `shutdown /r` | 立即重启计算机 | power,restart,admin |
| 电源管理 | `shutdown /l` | 注销 | `shutdown /l` | 注销当前用户 | power,logout |
| 电源管理 | `shutdown /h /f` | 休眠 | `shutdown /h /f` | 强制休眠计算机 | power,hibernate |
| 电源管理 | `shutdown /s /t 3600` | 定时关机 | `shutdown /s /t 3600` | 3600秒后关机 | power,schedule |
| 电源管理 | `shutdown /a` | 取消关机 | `shutdown /a` | 取消计划的关机或重启 | power,cancel |

---

## 目录操作命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 目录操作 | `cd` | 显示当前目录位置 | `cd` | 显示当前所在的目录路径 | dir,path,daily |
| 目录操作 | `cd ..` | 回到上级目录 | `cd ..` | 返回到上一级目录 | dir,navigate,daily |
| 目录操作 | `cd \` | 返回根目录 | `cd \` | 返回到当前磁盘的根目录 | dir,navigate |
| 目录操作 | `cd \test1\test2` | 进入文件夹（绝对路径） | `cd \test1\test2` | 进入test2文件夹 | dir,navigate |
| 目录操作 | `cd /d d:\test` | 切换磁盘和目录 | `cd /d d:\test` | 切换到D盘并进入test文件夹 | dir,disk,navigate |
| 磁盘操作 | `d:` | 切换磁盘 | `d:` | 切换到D盘 | disk,navigate,daily |
| 目录操作 | `tree` | 显示目录结构 | `tree d:\test` | 显示D盘test目录的树形结构 | dir,tree,view |
| 目录操作 | `dir` | 显示目录中文件列表 | `dir` | 列出当前目录下的所有文件 | dir,ls,list,daily |
| 文件操作 | `md test` 或 `mkdir test` | 新建文件夹 | `md test` | 创建名为test的文件夹 | dir,create,folder,daily |

---

## 文件操作命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 文件操作 | `copy` | 复制文件 | `copy file1.txt d:\backup\` | 将file1.txt复制到D盘backup文件夹 | file,copy,backup,daily |
| 文件操作 | `xcopy` | 复制目录和文件 | `xcopy source\ dest\ /s /e` | 递归复制source目录到dest目录 | file,copy,dir,backup |
| 文件操作 | `move` | 移动文件 | `move file.txt d:\data\` | 将file.txt移动到D盘data文件夹 | file,move,daily |
| 文件操作 | `del` | 删除文件 | `del temp.txt` | 删除temp.txt文件 | file,delete,rm,daily |
| 文件操作 | `erase` | 删除文件 | `erase *.tmp` | 删除所有.tmp扩展名的文件 | file,delete,rm |
| 文件操作 | `rd` 或 `rmdir` | 删除空文件夹 | `rd emptyfolder` | 删除名为emptyfolder的空文件夹 | dir,delete,rm |
| 文件操作 | `rd /s` | 删除文件夹及其内容 | `rd /s folder` | 删除folder文件夹及其所有内容 | dir,delete,rm,recursive |
| 文件操作 | `ren` 或 `rename` | 重命名文件 | `ren old.txt new.txt` | 将old.txt重命名为new.txt | file,rename,daily |
| 文件操作 | `type` | 显示文件内容 | `type readme.txt` | 在控制台显示readme.txt的内容 | file,view,cat,daily |
| 文件操作 | `more` | 分页显示文件 | `more largefile.txt` | 分页显示largefile.txt的内容 | file,view,page |
| 文件操作 | `find` | 在文件中搜索文本 | `find "error" log.txt` | 在log.txt中搜索包含"error"的行 | file,search,text |
| 文件操作 | `findstr` | 高级文件搜索 | `findstr /r "^[0-9]" data.txt` | 搜索以数字开头的行 | file,search,regex |
| 文件操作 | `attrib` | 查看/修改文件属性 | `attrib +h secret.txt` | 将secret.txt设置为隐藏属性 | file,attr,hidden |
| 文件操作 | `fc` | 比较两个文件 | `fc file1.txt file2.txt` | 比较两个文件的差异 | file,compare,diff |

---

## 文本操作命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 文本操作 | `echo Hello World` | 显示文本 | `echo Hello World` | 在屏幕上显示"Hello World" | text,print,daily |
| 文本操作 | `echo. > file.txt` | 创建空文件 | `echo. > new.txt` | 创建名为new.txt的空文件 | file,create,empty |
| 文本操作 | `echo data >> file.txt` | 追加文本到文件 | `echo data >> log.txt` | 将"data"追加到log.txt末尾 | file,append,text |

---

## 网络操作命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 网络操作 | `ping` | 测试网络连接 | `ping www.baidu.com` | 测试与百度的网络连通性 | network,test,daily |
| 网络操作 | `ping -n 4` | 发送指定数量的ping包 | `ping -n 4 192.168.1.1` | 发送4个ping包 | network,test,count |
| 网络操作 | `ipconfig` | 查看IP配置 | `ipconfig` | 显示本机的网络配置信息 | network,ip,config,daily |
| 网络操作 | `ipconfig /all` | 查看详细网络配置 | `ipconfig /all` | 显示详细的网络配置信息 | network,ip,detail |
| 网络操作 | `ipconfig /release` | 释放IP地址 | `ipconfig /release` | 释放当前网络接口的IP地址 | network,ip,release,admin |
| 网络操作 | `ipconfig /renew` | 重新获取IP地址 | `ipconfig /renew` | 从DHCP重新获取IP地址 | network,ip,renew,admin |
| 网络操作 | `ipconfig /flushdns` | 清空DNS缓存 | `ipconfig /flushdns` | 清空本地的DNS解析缓存 | network,dns,clear,admin |
| 网络操作 | `tracert` | 跟踪网络路由 | `tracert www.google.com` | 跟踪到谷歌的网络路由路径 | network,trace,route |
| 网络操作 | `netstat` | 查看网络连接状态 | `netstat` | 显示当前活动的网络连接 | network,connection,status |
| 网络操作 | `netstat -an` | 查看所有网络连接 | `netstat -an` | 显示所有连接（数字形式） | network,connection,all |
| 网络操作 | `nslookup` | 查询DNS记录 | `nslookup www.example.com` | 查询域名的DNS解析信息 | network,dns,query |
| 网络操作 | `net use` | 网络连接映射 | `net use z: \\server\share` | 将远程共享文件夹映射为Z盘 | network,share,map,admin |

---

## 用户管理命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 用户管理 | `net user` | 查看系统用户 | `net user` | 显示系统中的所有用户账户 | user,list,admin |
| 用户管理 | `net user /add` | 创建新用户 | `net user test 123456 /add` | 创建用户名为test的用户 | user,create,admin |
| 用户管理 | `net user /delete` | 删除用户 | `net user test /delete` | 删除用户名为test的用户 | user,delete,admin |

---

## 系统信息命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 系统信息 | `systeminfo` | 查看系统详细信息 | `systeminfo` | 显示操作系统的详细配置信息 | system,info,detail |
| 系统信息 | `ver` | 查看系统版本 | `ver` | 显示Windows版本信息 | system,version |
| 系统信息 | `hostname` | 查看计算机名 | `hostname` | 显示当前计算机的主机名 | system,hostname,network |
| 系统信息 | `date` | 查看/设置日期 | `date` | 显示或设置系统日期 | system,date,time |
| 系统信息 | `time` | 查看/设置时间 | `time` | 显示或设置系统时间 | system,date,time |
| 系统信息 | `whoami` | 查看当前用户 | `whoami` | 显示当前登录的用户名 | system,user,current |
| 系统信息 | `vol c:` | 查看磁盘卷标 | `vol c:` | 显示C盘的卷标和序列号 | system,disk,volume |
| 系统信息 | `wmic os get name` | Windows管理接口 | `wmic os get name` | 获取操作系统名称信息 | system,wmi,query |

---

## 进程管理命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 进程管理 | `tasklist` | 查看运行中的进程 | `tasklist` | 显示当前运行的所有进程列表 | process,list,daily |
| 进程管理 | `tasklist /v` | 查看详细进程信息 | `tasklist /v` | 显示详细的进程信息 | process,detail |
| 进程管理 | `taskkill /f /im` | 结束进程（按名称） | `taskkill /f /im notepad.exe` | 强制结束名为notepad.exe的进程 | process,kill,force,admin |
| 进程管理 | `taskkill /f /pid` | 结束进程（按PID） | `taskkill /f /pid 1234` | 强制结束PID为1234的进程 | process,kill,force,admin |

---

## 环境变量命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 环境变量 | `set` | 查看环境变量 | `set` | 显示当前所有环境变量 | env,list,all |
| 环境变量 | `set var=value` | 设置环境变量 | `set PATH=%PATH%;C:\test` | 将C:\test添加到PATH | env,set,path |
| 环境变量 | `echo %var%` | 查看环境变量值 | `echo %PATH%` | 显示PATH环境变量的值 | env,view,echo |

---

## 磁盘管理命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 磁盘管理 | `format d: /q` | 格式化磁盘 | `format d: /q` | 快速格式化D盘 | disk,format,admin,danger |
| 磁盘管理 | `chkdsk c: /f` | 检查磁盘错误 | `chkdsk c: /f` | 检查C盘并修复错误 | disk,check,repair,admin |
| 磁盘管理 | `diskpart` | 磁盘分区工具 | `diskpart` | 启动磁盘分区管理工具 | disk,partition,admin |
| 磁盘管理 | `defrag c:` | 磁盘碎片整理 | `defrag c:` | 对C盘进行碎片整理 | disk,defrag,optimize |

---

## 压缩解压命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 压缩解压 | `compact /c file.txt` | 压缩文件 | `compact /c file.txt` | 压缩file.txt文件 | file,compress |
| 压缩解压 | `compact /u file.txt` | 解压文件 | `compact /u file.txt` | 解压file.txt文件 | file,decompress |

---

## 快速启动命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 快速启动 | `calc` | 启动计算器 | `calc` | 打开Windows计算器 | app,calc |
| 快速启动 | `notepad` | 启动记事本 | `notepad` | 打开Windows记事本 | app,notepad |
| 快速启动 | `cmd` | 打开新CMD窗口 | `cmd` | 启动新的命令行窗口 | app,cmd |
| 快速启动 | `cmd /c "echo test"` | 执行命令后关闭 | `cmd /c "echo test"` | 执行命令后关闭窗口 | app,cmd,script |
| 快速启动 | `explorer` | 打开资源管理器 | `explorer .` | 在当前目录打开资源管理器 | app,explorer,daily |

---

## 文件关联命令

| 类型 | 命令 | 功能解释 | 示例 | 示例功能解释 | 标签 |
|------|------|----------|------|--------------|------|
| 文件关联 | `assoc .txt` | 查看文件关联 | `assoc .txt` | 查看.txt文件的关联程序 | file,assoc,extension |
| 文件关联 | `ftype txtfile` | 查看文件类型 | `ftype txtfile` | 查看txtfile类型关联的命令 | file,type,assoc |

---

## 查询示例

```bash
# 1. 查看所有日常使用的命令
grep "daily" commands.md

# 2. 查看所有文件删除相关的命令
grep "delete" commands.md
# 或
grep "rm" commands.md

# 3. 查看所有网络相关的命令
grep "network" commands.md

# 4. 查看所有管理员权限命令
grep "admin" commands.md

# 5. 查看所有备份相关的命令
grep "backup" commands.md

# 6. 组合筛选：日常使用的文件操作命令
grep "file" commands.md | grep "daily"
```
