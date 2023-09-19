=====================================
CentOS-7 ZFS格式硬盘 挂载
=====================================

* 在CentOS 7上挂载ZFS格式的硬盘，需要先安装ZFS文件系统驱动程序。以下是详细步骤：

1. 添加ZFS文件系统的Yum源：

``sudo yum install http://download.zfsonlinux.org/epel/zfs-release.el7_9.noarch.rpm``

2. 安装ZFS文件系统驱动程序：

``sudo yum install zfs``

3. 加载ZFS内核模块：

``sudo modprobe zfs``

4. 创建ZFS存储池：

``sudo zpool create <pool_name> <device>``

其中， ``<pool_name>`` 是存储池的名称， ``<device>`` 是要用于创建存储池的设备路径。

5. 挂载ZFS存储池：

``sudo zfs set mountpoint=<mount_point> <pool_name>``

其中， ``<mount_point>`` 是要挂载的目录路径， ``<pool_name>`` 是存储池的名称。

6. 验证ZFS存储池是否成功挂载：

``df -h``

如果成功挂载，您应该能够看到存储池的信息。

为了使挂载在重启后仍然有效，您可以将挂载命令添加到 ``/etc/fstab`` 文件中。例如：

``<pool_name> <mount_point> zfs defaults 0 0``

这将在启动时自动挂载ZFS存储池。


.. note::
    记得最后设置gn的root权限并禁止root登录
    ``sudo passwd gn``

