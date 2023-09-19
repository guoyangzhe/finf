# SSH免密登录

注：各节点执行同样命令可以利用 pdsh 命令或for循环处理：
在node[1-10]节点执行 id slurm 可用下述命令之一：
pdsh： pdsh -w node[1-10] id slurm
for循环： for i in `seq 1 10`; do ssh node$i id slurm; done

## 1. 配置服务节点
### 1.0 进入服务节点的`root`
```bash
su root
```
### 1.1 关闭防火墙服务
```bash
systemctl stop firewalld.service
systemctl disable firewalld.service
firewall-cmd --state
#显示not running
```
### 1.2 修改hosts文件
```bash
nano /etc/hosts
# 填入
192.168.64.10 master master
192.168.64.11 node01 node01
# CTRL+X y 保存退出
```
### 1.3 退出root
```bash
exit
```
## 2. 配置计算节点

### 2.0 进入计算节点的`root`
```bash
ssh root@192.168.237.128
systemctl stop firewalld.service
systemctl disable firewalld.service
firewall-cmd --state
#显示not running
```
### 2.1 修改hosts文件
```bash
nano /etc/hosts
# 填入
192.168.64.10 master master
192.168.64.11 node01 node01
# CTRL+X y 保存退出
```
### 2.2 退出root
```bash
exit
```
## 3. 配置无密登陆
### 3.1 生成密钥
```bash
ssh-keygen -t rsa
# 一路回车
```
### 3.2 将公钥复制到其他节点
```bash
ssh-copy-id master
ssh-copy-id node01
# ssh-copy-id命令用于将本地计算机上的公钥复制到远程计算机的authorized_keys文件中，以实现无密码登录。当您使用ssh-copy-id命令时，它会将您的公钥添加到远程计算机的~/.ssh/authorized_keys文件中，这样您就可以使用私钥进行无密码登录。这对于自动化脚本、远程管理和配置管理非常有用。


```
### 3.3 测试
```bash
ssh master
ssh node01
```