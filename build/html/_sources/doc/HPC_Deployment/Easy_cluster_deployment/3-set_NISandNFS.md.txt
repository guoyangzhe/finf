# 配置NFS和NIS服务

* **本文默认使用的操作系统为：`CentOS 7.6-7.9`版本。其余版本的操作系统请自行调整命令。**

* **请严格按照本文的流程去执行，一般不会报错，不要随意调整安装流程。**

## 1. NFS服务s

### 1.1 NFS服务介绍

* *NFS(Network File System)网络文件系统，是一种分布式文件系统，允许网络中的计算机透明地共享资源。NFS是由Sun公司开发的，目前已经成为Unix和Linux系统中的标准服务。NFS是基于RPC(Remote Procedure Call)协议实现的，它允许网络中的计算机之间通过TCP/IP网络共享资源。NFS服务是基于客户端/服务器端的架构，NFS服务器端将共享的目录挂载到NFS客户端上，NFS客户端就可以像访问本地文件一样访问共享目录中的文件。NFS服务是基于共享目录的，所以在NFS服务器端需要先创建共享目录，然后将共享目录挂载到NFS客户端上，NFS客户端就可以访问共享目录中的文件了。*

### 1.2 服务端NFS的安装

* NFS服务的安装包是`nfs-utils`，安装命令如下：

  ```bash
  yum -y install nfs-utils
  ```

### 1.3 服务端NFS的配置

* NFS服务的配置文件是/etc/exports，配置文件中的每一行都是一个共享目录的配置信息，配置信息的格式如下：

  ```bash
  共享目录 客户端IP(权限)
  ```

  共享目录：需要共享的目录，可以是绝对路径，也可以是相对路径，如果是相对路径，则相对于`/etc/exports`文件所在的目录。

  客户端IP：可以是单个IP，也可以是IP段，也可以是域名，也可以是通配符`*`。

  权限：可以是ro(只读权限)，也可以是rw(读写权限)。

* 在管理节点上配置NFS服务器，将共享文件夹导出：

  ```bash
  sudo nano /etc/exports
  ```

* 在文件中添加以下内容：

  ```bash
  /shared_folder  *(rw,sync,no_root_squash)

  # 以下是示例：
  /home  *(rw,no_root_squash,sync)
  /share *(rw,no_root_squash,sync)
  /opt   *(rw,no_root_squash,sync)
  /data1   *(rw,no_root_squash,sync)
  /data2   *(rw,no_root_squash,sync)
  ```

* 其中，`/shared_folder`是共享文件夹的路径，`*`表示允许任何计算节点访问，`rw`表示读写权限，`sync`表示同步写入，`no_root_squash`表示允许`root`用户访问。

* **上述只要是进行共享的文件夹，在主宿主机上都要有，否则会报错。且权限要设置好（一般 `chmod 750 /share_folder` ）。**

* 在管理节点上启动NFS服务器：

  ```bash
  systemctl status nfs
  systemctl start nfs
  systemctl restart nfs
  systemctl enable nfs
  exportfs -r  # 如果您对NFS配置文件进行了更改，请使用该命令重新加载配置文件
  showmount -e master
  ```

  ```bash
  # 请确保您的网络设置正确，并且NFS端口（默认为2049）未被防火墙阻止。
  ```

### 1.4 客户端NFS的安装

* 在计算节点上安装NFS客户端软件：

  ```bash
  sudo yum install nfs-utils
  ```

* 在计算节点上创建挂载点：

  ```bash
  sudo mkdir /shared_folder
  ```

* 在计算节点上挂载共享文件夹(之后写入rc.local)：

  ```bash
  sudo mount -t nfs <管理节点IP>:/shared_folder /shared_folder
  # 写入 /etc/rc.local  示例
  mount -t nfs master:/home  /home
  mount -t nfs master:/opt  /opt
  mount -t nfs master:/share  /share
  ```

* 其中，`<管理节点IP>`是管理节点的IP地址，`/shared_folder`是共享文件夹的路径，`/shared_folder`是挂载点的路径。

* 在计算节点上启动NFS服务器（不知有没有必要，但还是enable一下吧）：

  ```bash
  systemctl status nfs
  systemctl start nfs
  systemctl restart nfs
  systemctl enable nfs
  exportfs -r  # 如果您对NFS配置文件进行了更改，请使用该命令重新加载配置文件
  showmount -e master
  ```

* 验证挂载是否成功：

  ```bash
  df -h
  ```

* 如果成功挂载，您应该能够看到共享文件夹的信息。

* 为了使挂载在重启后仍然有效，您可以将挂载命令添加到`/etc/fstab`文件中。例如：

  ```bash
  <管理节点IP>:/shared_folder /mnt/shared_folder nfs rw,sync,noauto 0 0
  ```

* 这将在启动时自动挂载共享文件夹。

### 1.5 （可选）客户端通过rc.local自动挂载

* 此外，也可将需要开机启动的命令直接写入/etc/rc.local的文件下

  ```bash
  touch /var/lock/subsys/local
  mount -t nfs node01:/home  /home
  ```

  ```bash
  # Please note that you must run 'chmod +x /etc/rc.d/rc.local' to ensure
  # that this script will be executed during boot.
  chmod +x /etc/rc.d/rc.local
  ```

### 1.6 （可选）客户端通过fstab自动挂载

* 也可将需要开机启动的命令直接写入/etc/fstab的文件下

  ```bash
  node01:/home  /home nfs rw,sync,noauto 0 0
  ```

* 之后执行以下命令

  ```bash
  mount -a
  ```

* NFS在客户端的使用方法：

  ```bash
  showmount -e master #会显示服务器的共享目录
  ```

### 1.7 （可选）客户端通过autofs自动挂载

* 也可将需要开机启动的命令直接写入/etc/auto.master的文件下

  ```bash
  /home /etc/auto.home
  ```

* 在/etc/auto.home文件下写入

  ```bash
  * -rw,sync node01:/home/&
  ```

---

## 2. NIS服务

* 在有多台linux服务器的环境中,且一台linux服务器的账号又有很多且可能会相同，所以会出现理员很难管理的现象。NIS的主要功能是对主机账号系统等系统信息提供集中的管理。
* 当NIS客户机需要进行用户登录的信息验证时，就向NIS服务器发出查询请求。当系统中的一台NIS服务器为多台NIS客户机提供服务时，用户登录系统中的任何一台NIS客户机都会从NIS服务器进行登录验证，这样就实现了集中管理用户账号的功能。
* **请注意，执行该步骤时要确保/home目录已经成功挂载并共享。**
* **系统已经重启。**

### 2.1 NIS服务端配置

* NIS服务端的安装包是ypserv，安装命令如下：

  ```bash
  yum install ypserv rpcbind
  ```

* 创建NIS域：

  ```bash
  nano /etc/sysconfig/network
  # Created by anaconda
  NISDOMAIN=master
  # 该方法永久生效，但是需要重启
  ```

* 以下这一步在自己的电脑上不需要设置，服务器上为了安全考虑需要设置。
  
  ```bash
  # 设置/etc/ypserv.conf主配置文件：

  nano /etc/ypserv.conf

  *                              : *       : shadow.byname          : port
  *                              : *       : passwd.adjunct.byname  : port
  127.0.0.1/255.255.255.0        : *       : *                      : none #本地回环id,代表的是本机，允许本机访问所有的域
  192.168.241.0/255.255.255.0    : *       : *                      : none
  *                              : *       : *                      : deny
  ```

* 启动和启用NIS服务：

  ```bash
  systemctl start ypserv # 首先要启动ypserv服务，否则建立NIS数据库会报错
  systemctl enable ypserv
  systemctl start rpcbind
  systemctl enable rpcbind
  ```

### 2.2 NIS客户端配置

* NIS客户端的安装包是ypbind，安装命令如下：

  ```bash
  yum -y install ypbind rpcbind
  ```

* NIS客户端的配置文件是`/etc/yp.conf`，配置文件中的每一行都是一个NIS客户端的配置信息，配置信息的格式如下：

  ```bash
  domain <NIS域名> server <NIS服务器IP>
  # 示例：
  domain master server master
  ```

  ```bash
  注：
  rpm -qf `which yppasswd` #查看命令来源 
  显示：yp-tools-2.14-5.el7.x86_64 # (安装ypbind时会自动解决依赖关系安装yp-tools)
  # 使用yppasswd可以远程修改NIS服务器的密码
  # 查看安装了哪些软件：rpm -qa yp*
  ```

* 设置NIS域名--同master
  NIS是会通过域名来分辨不同账号的密码数据，因此必须要在服务器与客户端都指定相同的NIS域名。

  ```bash
  nano /etc/sysconfig/network
  # Created by anaconda
  NISDOMAIN=master
  # 该方法永久生效，但是需要重启
  ```

* 配置nsswitch.conf

  ```bash
  # /etc/nsswitch.conf
  passwd:     files nis
  shadow:     files nis
  group:      files nis

  hosts:      files dns myhostname nis # 添加nis
  ```

* 启动服务：

  ```bash
  systemctl start ypbind
  systemctl enable ypbind
  systemctl start rpcbind
  systemctl enable rpcbind
  ```

* 验证：

  ```bash
  systemctl status ypbind #显示running则表示成功
  systemctl status rpcbind #显示running则表示成功
  ```

* 验证：在客户端上输入`yptest`，能看到nis服务器上的用户

* **注意：如若不成功，请使用系统工具 `setup` 进行设置。**
  选择 Authentication configuration，选择 Use NIS，然后输入 NIS domain name 和 NIS server IP address，最后点击 OK 即可。

### 2.3 NIS服务端映射（该步骤可在2.1之后执行）

* 配置NIS映射表：
  *创建NIS映射表文件（例如passwd、group等）并将其复制到/var/yp目录下：*

  ```bash
  cp /etc/passwd /var/yp/passwd
  ```

* 生成NIS映射表：

  ```bash
  cd /var/yp
  make
  ```

* 查看服务：

  ```bash
  rpcinfo -p master
  ```

---

## 3. 题外话

* CentOS7挂载硬盘示例（请灵活更改自己的命令）：

  ```bash
  (base) [root@node01 /]# lsblk
  NAME            MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
  sda               8:0    1   7.3T  0 disk
  sdb               8:16   1   7.3T  0 disk
  sdc               8:32   1   7.3T  0 disk
  └─sdc1            8:33   1   7.3T  0 part /home

  (base) [root@node02 data3]# blkid
  /dev/sda2: LABEL="ROOT" UUID="6f979e18-09c9-435e-b09d-274b7f967903" TYPE="ext3" PARTUUID="873f3f46-b046-4e1c-ab5f-94de3d1f9522"
  /dev/sda1: LABEL="EFI" UUID="9991-A2DE" TYPE="vfat" PARTLABEL="EFI System Partition" PARTUUID="031855d3-56a7-441f-9a3d-392efd575f0f"
  #诸如此类

  (base) [root@node02 data3]# fdisk -l
  WARNING: fdisk GPT support is currently new, and therefore in an experimental phase. Use at your own discretion.

  Disk /dev/sda: 512.1 GB, 512110190592 bytes, 1000215216 sectors
  Units = sectors of 1 * 512 = 512 bytes
  Sector size (logical/physical): 512 bytes / 4096 bytes
  I/O size (minimum/optimal): 4096 bytes / 4096 bytes
  Disk label type: gpt
  Disk identifier: 0ED54899-BCF2-4DB7-8103-3FA21DAD0DCC


  #         Start          End    Size  Type            Name
   1         2048      2099199      1G  EFI System      EFI System Partition
   2      2099200    865996799    412G  Microsoft basic
   3    865996800   1000214527     64G  Linux swap
  WARNING: fdisk GPT support is currently new, and therefore in an experimental phase. Use at your own discretion.
  #=================================================================================================================

  (base) [root@node02 data3]# nano /etc/fstab
  #示例：
  UUID=a2fd2367-2227-4a96-a5c8-757f11c1d386        /data4                  ext4    defaults        0 0
  ```
