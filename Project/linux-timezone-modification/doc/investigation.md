# 排查过程

## 起因

云服务器上的程序日志时间与北京时间不一致，发现是时区设置为 UTC。

## 排查步骤

1. **确认时间不对** → `date` 显示 UTC 时间，不是 CST
2. **尝试 date -s 直接改时间** → 发现改的是系统时钟而非时区，治标不治本
3. **查到 timedatectl** → `timedatectl` 显示 Time zone: UTC，确认是时区问题
4. **执行 timedatectl set-timezone Asia/Shanghai** → 立即生效，无需重启
5. **验证** → `date` 显示 CST 时间，`timedatectl` 显示 Asia/Shanghai

## 经验

- 时区问题不要用 `date -s`，那是改时钟不是改时区
- 云服务器默认 UTC 时区是常见坑，拿到新机器第一步就改
