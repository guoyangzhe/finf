# Slurm使用教程

## 什么是Slurm
Slurm是一个开源的、高度可扩展的集群管理和工作调度系统，用于Linux和Unix操作系统。Slurm最初是由Lawrence Livermore National Laboratory开发的，现在由Slurm工作组维护。Slurm的设计目标是在大型Linux集群上提供一个可扩展的、高性能的、可靠的集群管理器。

Slurm的功能包括：
* 分配和管理计算资源（计算节点）；
* 分配和管理任务（作业）；
* 监控系统状态；
* 收集和报告作业资源使用情况；
* 提供计算资源的可视化界面。

## Slurm的使用
sbatch 用于提交作业
squeue 用于查看作业
scancel 用于取消作业
sinfo 用于查看集群状态
scontrol 用于控制作业
sacct 用于查看作业的详细信息
sreport 用于生成报告

## Slurm的使用案例

### 作业提交

#### 作业提交的基本格式
```bash
sbatch [options] <jobscript>
```

#### 作业提交的常用选项
* -A, --account=name
* -c, --cpus-per-task=ncpus
* -J, --job-name=name
* -N, --nodes=nodes
* -n, --ntasks=ntasks
* -o, --output=name
* -p, --partition=name
* -t, --time=time
* -w, --nodelist=node_list
* -x, --exclude=node_list
* -C, --constraint=name
* -D, --dependency=type:jobid[:jobid...]

#### 作业提交的示例
```bash
sbatch -A account_name -p partition_name -n 1 -c 1 -t 1-00:00:00 -J job_name -o job_name.out job_script.sh
```

### 作业查看

#### 作业查看的基本格式
```bash
squeue [options]
```

#### 作业查看的常用选项
* -a, --all
* -A, --account=name
* -j, --job=job_id
* -n, --name=name
* -o, --format=format
* -p, --partition=name
* -P, --detailed
* -r, --noconvert
* -s, --states=list
* -t, --states=list
* -u, --user=list
* -h, --help

显示占用核心数：
alias squeue='squeue -o "%.8i   %.7P   %18j   %.4u   %.2t   %.11M   %.4D   %.16R   %.4C"'

#### 作业查看的示例

```bash
squeue -u user_name
# 例如
squeue -u host
```

### 作业取消

#### 作业取消的基本格式
```bash
scancel [options] <job_id>
```

#### 作业取消的常用选项
* -a, --all
* -b, --batch
* -h, --help
* -i, --interactive
* -n, --name=name
* -p, --partition=name
* -u, --user=name

#### 作业取消的示例
```bash
scancel job_id
```

### 集群状态查看

#### 集群状态查看的基本格式
```bash
sinfo [options]
```

#### 集群状态查看的常用选项
* -a, --all
* -h, --help
* -l, --long
* -o, --format=format
* -p, --partition=name
* -R, --resv
* -t, --states=list
* -u, --user=list

#### 集群状态查看的示例
```bash
sinfo -l
```

### 作业控制

#### 作业控制的基本格式
```bash
scontrol [options] <command>
```

#### 作业控制的常用选项
* -a, --all
* -b, --batch
* -d, --details
* -h, --help
* -i, --interactive
* -l, --long
* -o, --format=format
* -p, --partition=name
* -t, --states=list
* -u, --user=list

#### 作业控制的示例
```bash
scontrol show job job_id
```

### 作业详细信息查看

#### 作业详细信息查看的基本格式
```bash
sacct [options]
```

#### 作业详细信息查看的常用选项
* -a, --allusers
* -A, --account=name
* -b, --starttime=time
* -c, --clusters=cluster_list
* -d, --duplicates
* -D, --dformat=format
* -e, --endtime=time
* -h, --help
* -j, --jobs=job_list
* -l, --long
* -M, --mail
* -n, --name=name
* -o, --format=format
* -p, --parsable2
* -P, --noconvert
* -r, --reverse
* -S, --noheader
* -t, --state=state_list
* -u, --user=user_list
* -V, --version
* -w, --wide

#### 作业详细信息查看的示例
```bash
sacct -j job_id
```

### 作业报告生成

#### 作业报告生成的基本格式
```bash
sreport [options] <report> <cluster> [start] [end]
```

#### 作业报告生成的常用选项
* -a, --all
* -A, --account=name
* -b, --starttime=time
* -c, --clusters=cluster_list
* -d, --duplicates
* -D, --dformat=format
* -e, --endtime=time
* -h, --help
* -j, --jobs=job_list
* -l, --long
* -M, --mail
* -n, --name=name
* -o, --format=format
* -p, --parsable2
* -P, --noconvert
* -r, --reverse
* -S, --noheader
* -t, --state=state_list
* -u, --user=user_list
* -V, --version
* -w, --wide

#### 作业报告生成的示例
```bash
sreport cluster AccountUtilizationByUser cluster_name start_time end_time
```

## Slurm的配置

### 配置文件

#### 配置文件的位置
```bash
/etc/slurm/slurm.conf
```

## Slurm的常见问题

### 作业提交失败

#### 问题描述
```bash
sbatch: error: Batch job submission failed: Socket timed out on send/recv operation
```

#### 问题原因
* 作业提交的节点与控制节点之间的网络不通

#### 问题解决
* 检查作业提交的节点与控制节点之间的网络是否通畅

### 作业运行失败

#### 问题描述
```bash
srun: error: Unable to create step for job 123456: Socket timed out on send/recv operation
```

#### 问题原因
* 作业运行的节点与控制节点之间的网络不通

#### 问题解决
* 检查作业运行的节点与控制节点之间的网络是否通畅

## 重启Slurm

### 重启Slurm的基本格式
```bash
systemctl restart slurmctld
```

## 查看Slurm的版本

```bash
scontrol --version
```

## Slurm的状态为down的解决方案

```bash
(base) [root@node02 ~]# scontrol update node=node02 state=down reason=hung
(base) [root@node02 ~]# scontrol update node=node02 state=resume
```

```bash
[host@node01 ~]$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
debug01*     up   infinite      3   idle node[01-03]

[host@node01 ~]$ pbsnodes -a

.. code-block:: sh
    :caption: sinfo
    :name: test333
    :emphasize-lines: 2
    :linenos:
    
    node01
        state = free
        np = 128
        ntype = cluster
        status = rectime=1686038364,state=free,slurmstate=idle,size=0kb:0kb,ncpus=128,boards=1,sockets=2,cores=64,threads=1,availmem=1mb,opsys=linux 3.10.0-1127.el7.x86_64 #1 smp tue mar 31 23:36:51 utc 2020,arch=x86_64

    node02
        state = free
        np = 56
        ntype = cluster
        status = rectime=1686038364,state=free,slurmstate=idle,size=0kb:0kb,ncpus=56,boards=1,sockets=2,cores=28,threads=1,availmem=1mb,opsys=linux 3.10.0-1127.el7.x86_64 #1 smp tue mar 31 23:36:51 utc 2020,arch=x86_64

    node03
        state = free
        np = 40
        ntype = cluster
        status = rectime=1686038364,state=free,slurmstate=idle,size=0kb:0kb,ncpus=40,boards=1,sockets=2,cores=20,threads=1,availmem=1mb,opsys=linux 3.10.0-1127.el7.x86_64 #1 smp tue mar 31 23:36:51 utc 2020,arch=x86_64
```

```bash 
(base) [root@master ~]# scontrol show node
NodeName=master CoresPerSocket=6
   CPUAlloc=0 CPUEfctv=6 CPUTot=6 CPULoad=N/A
   AvailableFeatures=(null)
   ActiveFeatures=(null)
   Gres=(null)
   NodeAddr=master NodeHostName=master
   RealMemory=1 AllocMem=0 FreeMem=N/A Sockets=1 Boards=1
   State=IDLE+NOT_RESPONDING ThreadsPerCore=1 TmpDisk=0 Weight=1 Owner=N/A MCS_label=N/A
   Partitions=hpc
   BootTime=None SlurmdStartTime=None
   LastBusyTime=2023-07-05T21:51:27
   CfgTRES=cpu=6,mem=1M,billing=6
   AllocTRES=
   CapWatts=n/a
   CurrentWatts=0 AveWatts=0
   ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s

NodeName=node01 Arch=x86_64 CoresPerSocket=4
   CPUAlloc=0 CPUEfctv=4 CPUTot=4 CPULoad=0.04
   AvailableFeatures=(null)
   ActiveFeatures=(null)
   Gres=(null)
   NodeAddr=node01 NodeHostName=node01 Version=22.05.5
   OS=Linux 3.10.0-1160.92.1.el7.x86_64 #1 SMP Tue Jun 20 11:48:01 UTC 2023
   RealMemory=1 AllocMem=0 FreeMem=6558 Sockets=1 Boards=1
   State=IDLE ThreadsPerCore=1 TmpDisk=0 Weight=1 Owner=N/A MCS_label=N/A
   Partitions=hpc
   BootTime=2023-07-05T21:27:14 SlurmdStartTime=2023-07-05T21:50:00
   LastBusyTime=2023-07-05T21:51:51
   CfgTRES=cpu=4,mem=1M,billing=4
   AllocTRES=
   CapWatts=n/a
   CurrentWatts=0 AveWatts=0
   ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s
```
