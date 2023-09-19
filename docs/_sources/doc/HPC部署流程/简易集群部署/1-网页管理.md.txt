# 部署网页管理

* 本步骤仅管理节点需要操作

## 1. 基础知识

* 开启防火墙：`systemctl start firewalld`

* 关闭防火墙：`systemctl stop firewalld`

* 查看防火墙状态：`systemctl status firewalld`

## 2. 部署网页管理

* 安装cockpit

  ```bash
  yum install -y cockpit cockpit-docker cockpit-machines cockpit-dashboard cockpit-storaged cockpit-packagekit
  systemctl enable --now cockpit.socket
  ```

* 如果系统有开启防火墙，需要额外执行：

  ```bash
  firewall-cmd --permanent --zone=public --add-service=cockpit
  firewall-cmd --reload
  ```

* 显示success即可（成功）

## 3. 使用方法

* 直接访问ip:9090端口：`192.168.237.132:9090`

## 4. 附录

* 安装谷歌（centos7）

  ```bash
  yum install liberation-fonts
  yum install libvulkan.so.1
  yum -y install vulkan-1.1.97.0-1.el7.x86_64
  rpm -i ***.rpm
  ```

* 安装百度网盘（centos7）

  ```bash
  rpm -i ***.rpm
  # 拷贝libstdc++.so.6.0.20 到 /usr/lib64/ 目录下
  # 不拷贝libstdc++.so.6.0.20 启动百度网盘会有异常
  ```
