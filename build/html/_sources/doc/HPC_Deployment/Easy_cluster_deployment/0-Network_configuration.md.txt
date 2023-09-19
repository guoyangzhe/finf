# 初始准备与网络配置

centos7.9 首次安装默认网卡是关闭的
输入：`cd /etc/sysconfig/network-scripts`
可以看到网卡`ifcfg-ens33`，不是每个人都是`ens33`别跟着打自己看一下
输入：`nano ifcfg-ens33`
修改成这样：（静态IP，防止之后IP会发生变化；我用的是虚拟机`net`模式）
```bash
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static #修改
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=b53ebcc3-83e5-48bb-90a5-e779cb712629
DEVICE=ens33
ONBOOT=yes #修改

IPADDR=192.168.64.10
NETMASK=255.255.255.0
GATEWAY=192.168.64.2
DNS1=192.168.64.2
DNS2=8.8.8.8
DNS3=8.8.4.4
DNS4=114.114.114.114
```

输入：`ctrl+X y` 保存并退出
输入：`systemctl restart network`
重启后输入：`ip addr`
(服务节点和计算节点都要操作，首先保证网络畅通)
```bash
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=masternet
UUID=0824e723-d2ed-4cfc-9069-1a68f08a269d
ONBOOT=yes
IPADDR=192.168.64.10
NETMASK=255.255.255.0
GATEWAY=192.168.64.2
DNS1=192.168.64.2
DNS2=8.8.8.8
DNS3=8.8.4.4
DNS4=114.114.114.114
```