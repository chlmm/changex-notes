# 决策树：Linux 时区修改

```
需要修改 Linux 时区
│
├─ 是否有 sudo 权限？
│   ├─ 是 → 继续 ↓
│   └─ 否 → 只能用 TZ 环境变量临时修改
│
├─ 是否为 systemd 系统？
│   ├─ 是 → timedatectl set-timezone（推荐）
│   └─ 否 → ln -sf 软链接方式
│
├─ 是否为容器环境？
│   ├─ 是 → 检查宿主机时区映射 / 挂载 /etc/localtime
│   └─ 否 → 直接修改即可
│
└─ 是否需要永久生效？
    ├─ 是 → timedatectl 或软链接
    └─ 否 → export TZ 临时生效即可
```

## 关键判断点

1. **优先 timedatectl**：现代 Linux 标准工具，一步到位
2. **容器特殊处理**：容器内改时区可能不持久，需要挂载宿主机的时区文件
3. **软链接是兜底**：老系统或嵌入式环境可能没有 timedatectl
