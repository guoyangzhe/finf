# 部署Slurm

- **一台服务器，一台计算节点，操作系统为CentOS7.6-7.9**
- 请确保服务器和计算节点的网络通畅，否则请先配置网络
- 请确保服务器和计算节点的ssh免密登录，否则请先配置ssh免密登录
- 请确保服务器和计算节点的时间同步，否则请先配置时间同步
- 请确保NFS&NIS服务已经配置完成，否则请先配置NFS&NIS服务

## 1. Slurm简介

**在cluster上源码编译slurm(依官方说明)**

- 简介：  <http://hmli.ustc.edu.cn/doc/linux/slurm-install/slurm-install.html>

> Slurm(Simple Linux Utility for Resource Management， <http://slurm.schedmd.com/> )是开源的、具有容错性和高度可扩展的`Linux`集群超级计算系统资源管理和作业调度系统。超级计算系统可利用`Slurm`对资源和作业进行管理，以避免相互干扰，提高运行效率。所有需运行的作业，无论是用于程序调试还是业务计算，都可以通过交互式并行 `srun` 、批处理式 `sbatch` 或分配式 `salloc` 等命令提交，提交后可以利用相关命令查询作业状态等。

- 架构：

> Slurm采用`slurmctld`服务（守护进程）作为中心管理器用于监测资源和作业，为了提高可用性，还可以配置另一个备份冗余管理器。
>
> 各计算节点需启动`slurmd`守护进程，以便被用于作为远程`shell`使用：等待作业、执行作业、返回状态、再等待更多作业。

> `slurmdbd(Slurm DataBase Daemon)`数据库守护进程（非必需，建议采用，也可以记录到纯文本中等），可以将多个slurm管理的集群的记账信息记录在同一个数据库中。

> 还可以启用`slurmrestd(Slurm REST API Daemon)`服务（非必需），该服务可以通过`REST API`与Slurm进行交互，所有功能都对应的API。

> 用户工具包含 `srun` 运行作业、 `scancel` 终止排队中或运行中的作业、 `sinfo` 查看系统状态、 `squeue` 查看作业状态、 `sacct` 查看运行中或结束了的作业及作业步信息等命令。`sview` 命令可以图形化显示系统和作业状态（可含有网络拓扑）。`scontrol` 作为管理工具，可以监控、修改集群的配置和状态信息等。用于管理数据库的命令是 `sacctmgr` ，可认证集群、有效用户、有效记账账户等。

- 官方文档：

> 1. 确保时钟、用户和组（`UIDs和GIDs`）在整个集群中是同步的。
> 2. 安装`MUNGE`用于认证。确保你的集群中的所有节点都有相同的`munge.key`。确保在你启动Slurm守护程序之前，`MUNGE守护程序munged已经启动`。
> 3. `rpmbuild -ta slurm*.tar.bz2` #使用该命令进行编译
> 4. `rpm --install &lt;the rpm files&gt;` #安装包
> 5. Install the configuration file in `<sysconfdir>/slurm.conf`.  #在每个节点安装配置文件
 NOTE: You will need to install this configuration file on all nodes of the cluster.
> 6. Controller: `systemctl enable slurmctld` # slurmctld服务
 Database: `systemctl enable slurmdbd` #当前示例中，master是登陆节点，同时也是控制和数据库
 Compute Nodes: `systemctl enable slurmd` # node1 是计算节点

- **注：不同节点类型所需安装包**
- 管理节点(`Head Node`，运行`slurmctld`服务)、计算节点(`Compute Node`)和用户登录节点(`Login Node`)：

> `slurm`
>
> `slurm-perlapi`
>
> `slurm-slurmctld`（仅管理节点需要）
>
> `slurm-slurmd`（仅计算节点需要，用户登录节点如采用无配置模式，则也需要）

- SlurmDBD节点：

> `slurm`
>
> `slurm-slurmdbd`
>
> 注意 （可选）
>
> 管理节点：`slurm-slurmctld` `slurm-slurmdbd` 务必安装，并安装提示的依赖的其他包
>
> 计算节点：以上两个不必安装，安装其他的包  安装就是 `rpm -i XXX.rpm`

## 2. 配置Munge(所有节点)

- 安装epel源 (在所有节点上执行)

  ```sh
  yum -y install epel-release
  ```

- 安装munge (在所有节点上执行)

  ```sh
  yum -y install munge munge-libs munge-devel
  ```

- 生成munge.key (在管理节点上执行)

  ```sh
  /usr/sbin/create-munge-key -r
  ```

- 将munge.key文件复制到其他节点 (在管理节点上执行)

  ```sh
  scp /etc/munge/munge.key root@node1:/etc/munge/
  scp /etc/munge/munge.key root@node2:/etc/munge/
  ```

- 修改权限 (在所有节点上执行)

  ```sh
  chown munge: /etc/munge/munge.key
  chmod 400 /etc/munge/munge.key
  ```

- 启动munge服务 (在所有节点上执行)

  ```sh
  systemctl enable munge
  systemctl start munge
  ```

- 验证munge服务 (在所有节点上执行)

  ```sh
  # 本地查看凭据
  munge -n
  # 本地解码
  munge -n | unmunge
  # 远程解码
  munge -n | ssh node01 unmunge
  # 基准测试
  remunge
  ```

## 3. 部署Slurm

### 3.1 服务端部署Slurm

- **安装依赖包**

  ```sh
  yum -y install mariadb mariadb-devel mariadb-server munge munge-devel hwloc-libs hwloc-devel hdf5-devel pam-devel perl-ExtUtils-MakeMaker python3 readline-devel
  ```

### 3.1.1 使用OpenHPC安装Slurm (未测试)

- CentOS7 使用自带的库或者OpenHPC 1.3.9安装Slurm的步骤如下：
  
    首先，确保你的CentOS系统已经安装了OpenHPC 1.3.9。你可以通过以下命令来检查：

  ```sh
  yum list installed | grep openhpc
  ```

- 安装Slurm的依赖包：

  ```sh
  yum -y install slurm slurm-slurmctld slurm-slurmdbd slurm-perlapi
  ```

- 配置Slurm。你需要编辑Slurm的配置文件，通常位于/etc/slurm/slurm.conf。你可以根据你的需求进行配置，包括节点信息、分区、用户权限等。
- 启动Slurm服务

  ```sh
  systemctl enable slurmctld
  systemctl restart slurmctld
  ```

- 验证Slurm的安装。你可以使用以下命令来检查Slurm的状态：

  ```sh
  systemctl status slurmctld
  ```

  ```sh
  sinfo
  ```

### 3.1.2 源码编译安装Slurm

- **下载源码包**

  ```sh
  wget https://download.schedmd.com/slurm/slurm-22.05.5.tar.bz2
  ```

- **编译安装**

  ```sh
  rpmbuild -ta slurm-22.05.5.tar.bz2 #（编译会报错H5PT，使用conda deactivate，不要使用python库）
  # 耐心等待 成功后将在/root/rpmbuild/RPMS/x86_64/ 目录下生成12个RPM包（这些是二进制包）
  ```

- **安装包**

  ```sh
  cd /root/rpmbuild/RPMS/x86_64 # （为了方便，安装全部的包→12个包）
  rpm -ivh *rpm   
  #之后可以选择卸载掉不需要的包 如： rpm -e slurm-slurmd
  # 在Slurm中，有一些包需要安装在服务节点，而另一些包需要安装在计算节点。以下是Slurm的12个包以及它们应该安装的节点类型：
      1. slurm：服务节点和计算节点都需要安装。
      2. slurm-slurmctld：服务节点上安装，用于控制Slurm集群。
      3. slurm-slurmd：计算节点上安装，用于执行作业。
      4. slurm-slurmdbd：服务节点上安装，用于Slurm数据库。
      5. slurm-munge：服务节点和计算节点都需要安装，用于加密通信。
      6. slurm-pam_slurm：服务节点和计算节点都需要安装，用于PAM认证。
      7. slurm-perlapi：服务节点和计算节点都需要安装，用于Perl API。
      8. slurm-plugins：服务节点和计算节点都需要安装，用于插件支持。
      9. slurm-slurmrestd：服务节点上安装，用于RESTful API支持。
      10. slurm-slurm-torque：服务节点上安装，用于与Torque集成。
      11. slurm-slurm-topology-hwloc：服务节点和计算节点都需要安装，用于硬件拓扑支持。
      12. slurm-slurm-topology-override：服务节点和计算节点都需要安装，用于硬件拓扑覆盖。
  # 请注意，具体的安装需求可能会因你的集群配置和需求而有所不同。建议你参考Slurm的官方文档和指南来确定正确的安装方式。
  ```

- **配置Slurm**

  ```sh
  # 生成配置文件
  nano /etc/slurm/slurm.conf
  nano /etc/slurm/slurmdbd.conf
  nano /etc/slurm/cgroup.conf
  # 修改权限
  chown root.root /etc/slurm/slurmdbd.conf
  chmod 600 /etc/slurm/slurmdbd.conf
  chown root /etc/slurm/slurm.conf
  mkdir /var/spool/slurmctld
  chown root.root /var/spool/slurmctld
  ```

- **启动服务**

  ```sh
  systemctl restart slurmctld
  systemctl enable slurmctld
  systemctl status slurmctld
  systemctl restart slurmdbd
  systemctl enable slurmdbd
  systemctl status slurmdbd
  ```

### 3.2 客户端部署Slurm

- **安装依赖包**

  ```sh
  yum -y install mariadb mariadb-devel mariadb-server munge munge-devel hwloc-libs hwloc-devel hdf5-devel pam-devel perl-ExtUtils-MakeMaker python3 readline-devel
  ```

- 在服务端复制安装包到共享文件夹

  ```sh
  cp ./rpmbuild/RPMS/x86_64/* /opt/slurm-packages
  ```

- 进入计算节点，安装依赖包

  ```sh
  cd /opt/slurm-packages
  rpm -ivh *rpm  #（可以之后删除计算节点上不需要的包）
  ```

- **将配置文件发送到计算节点**

  ```sh
  scp /etc/slurm/slurm.conf root@node01:/etc/slurm/
  scp /etc/slurm/cgroup.conf root@node01:/etc/slurm/
  pdsh -w node01 chown root.root /etc/slurm/ -R
  pdsh -w node01 systemctl restart slurmd
  pdsh -w node01 systemctl enable slurmd
  pdsh -w node01 systemctl status slurmd
  ```

## 4. 一些小的问题

- [ ] *如果修改了配置文件 `slurm.conf` ,则请在 `master` 上执行 `scontrol reconfig` 命令更新配置文件。*
- [ ] *目前集群所有机器的配置文件是一样的，如果修改了请把所有机器的 `conf` 都相应修改掉*
- [ ] *查看各个节点的情况 `scontrol show node` 如果出现 `not responding` 说机器通信有问题*
- [ ] *如果要看上述3中的机器的具体原因可以查看每台机器的具体日志，目录为 `/var/log/slurmd.log`
在master上还可以查看 `/var/log/slurmctld.log`*
- [ ] *如果某个节点 `down` 很久了，后来你找到原因了，觉得解决了。此时因为长时间 down 需要 `update` 整个集群，命令为 `scontrol updatenode=master,slaver1,slaver2,slaver3 state=idle`*
- [ ] *建立slurm用户的时候查看 `id slurm` 会显示 `uid=1001(slurm),gid=1001(slurm),group=1001(slurm)` 【我的集群上】。注意每台机器上都要建一个 `slurm` 账户，当你查看发现有的机器上 `id slurm` 不一致的时候，可能有的机器是1000，这时候需要修改uid和gid为1001，所有节点一定要保持一致！然后如果之前手动建立的 `munge` 文件夹是在1000时候建立的，改了之后要把之前的文件夹删掉重新建一遍！*
- [ ] *`Sview` 来图形化查看任务状态，这个需要在本地有一个 `vnc` 的客户端，在 `master` 上开一个 `vncsever` 就可以连了，然后 `sview` ，否则直接命令窗登陆会看到 `cannot open display` 。*
