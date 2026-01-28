---
name: zerotier
description: ZeroTier - 虚拟局域网工具。创建虚拟网络，实现设备间安全互联，类似 VPN 但更轻量。
execution_mode: user
metadata:
  category: network-tools
  platform: [windows, macos, linux, ios, android]
  tags: [虚拟网络, VPN, 组网, 远程访问]
---

# ZeroTier 使用指南

## 概述

ZeroTier 是一个虚拟局域网工具，可以将分布在不同地点的设备组成一个虚拟局域网，实现设备间的安全互联和远程访问。

## 功能特性

- 创建虚拟局域网
- 跨平台支持
- P2P 直连优先
- 加密通信
- 无需公网 IP

## 安装

### 各平台安装

**Windows**:
[TBD - 安装步骤]

**macOS**:
```bash
brew install zerotier-one
```

**Linux**:
```bash
curl -s https://install.zerotier.com | sudo bash
```

## 基础使用

### 创建网络

**操作步骤**:
1. 访问 https://my.zerotier.com
2. 注册/登录账号
3. 点击 "Create A Network"
4. 记录 Network ID

### 加入网络

**操作步骤**:
```bash
zerotier-cli join <Network ID>
```

### 授权设备

**操作步骤**:
1. 在 ZeroTier Central 网页中查看新加入的设备
2. 勾选 "Auth" 授权该设备
3. 设备会自动获得虚拟 IP 地址

## 进阶配置

### 路由设置

[TBD - 路由配置]

### 访问控制

[TBD - 访问控制配置]

## 使用场景

- 远程办公内网访问
- 游戏联机
- 文件共享
- 远程开发环境

## 资源

- **官网**: https://www.zerotier.com/
- **原文件位置**: `工具/softs/index/zerotier.md`
