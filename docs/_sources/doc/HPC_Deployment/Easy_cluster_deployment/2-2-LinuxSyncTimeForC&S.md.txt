# 配置服务器时间同步

## 1. 服务器时间同步

* 修改服务节点的`/etc/ntp.conf`文件，添加如下内容
```bash
nano /etc/ntp.conf
# 填入如下内容：
restrict 192.168.237.0 mask 255.255.255.0 nomodify notrap
# 在`server`部分添加一部分，并注释掉`server 0 ~ n`
server 127.127.1.0
Fudge 127.127.1.0 stratum 10
```
* 修改子节点的`/etc/ntp.conf`文件，添加如下内容
```bash
# 填入如下内容：
restrict 192.168.237.132 nomodify notrap nopeer noquery 
restrict 192.168.237.0 mask 255.255.255.0 nomodify notrap
# 在`server`部分添加一部分，并注释掉`server 0 ~ n`
server 192.168.237.132
Fudge 192.168.237.132 stratum 10
```
## 2. 启动服务
* 启动服务
```bash
service ntpd restart
ntpstat
systemctl enable ntpd
systemctl list-unit-files|grep ntpd
```

注：
ntp服务器配置完毕后，需要等待5-10分钟才能与/etc/ntp.conf中配置的标准时间进行同步。
等一段时间之后，再次使用ntpstat命令查看状态，直到所有节点都与指定的主节点连接上
```bash
(base) [root@cluster /]# pdsh -w node[1-2] ntpstat
node1: synchronised to NTP server (192.168.237.132) at stratum 7
node1:    time correct to within 1004 ms
node1:    polling server every 64 s
node2: synchronised to NTP server (192.168.237.132) at stratum 7
node2:    time correct to within 895 ms
node2:    polling server every 64 s
```
这样就是同步成功了

