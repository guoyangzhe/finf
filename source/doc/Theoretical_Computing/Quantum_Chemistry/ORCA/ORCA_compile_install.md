# ORCA编译与安装

## 1. 安装Openmpi
* 准备软件安装包：
* 解压缩`openmpi-4.1.1.tar.gz`，得到`openmpi-4.1.1`文件夹，将其放置于`/opt/libraries`目录下。
* 编译安装：
```bash
cd /opt/libraries/openmpi-4.1.1
./configure --prefix=/opt/libraries/gnu8-openmpi/4.1.1 --disable-builtin-atomics
make -j 
make install
```
* 环境变量设置：
```bash
export PATH=$PATH:/opt/libraries/gnu8-openmpi/4.1.1/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/libraries/gnu8-openmpi/4.1.1/lib
```
* 测试：
```bash
mpirun -np 2 hostname
```
如果输出了两个主机名，则说明安装成功。

## 2. 安装ORCA
* 准备软件安装包：
* 解压缩`orca_5_0_4_linux_x86-64_openmpi411_shared.tar.xz`，得到`orca_5_0_4_linux_x86-64_openmpi411_shared`文件夹，将其放置于`/opt/apps`目录下。
* 环境变量设置：
```bash
export PATH=$PATH:/opt/apps/orca504_shared_openmpi411/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/apps/orca504_shared_openmpi411/
alias orca='/opt/apps/orca504_shared_openmpi411/orca'
```
* 测试：
```bash
orca -h
```
如果输出了帮助信息，则说明安装成功。


## 3. 最终的环境变量设置

```bash
#Openmpi4.1.1#
export PATH=$PATH:/opt/libraries/gnu8-openmpi/4.1.1/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/libraries/gnu8-openmpi/4.1.1/lib
#ORCA5.0.4#
export PATH=$PATH:/opt/apps/orca504_shared_openmpi411/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/apps/orca504_shared_openmpi411/
alias orca='/opt/apps/orca504_shared_openmpi411/orca'
```


## 4. 运行一个test
```bash
! BLYP def2-SVP noautostart miniprint pal4
* xyz 0 1
C 0.00000000 0.00000000 -0.56221066
H 0.00000000 -0.92444767 -1.10110537
H -0.00000000 0.92444767 -1.10110537
O 0.00000000 0.00000000 0.69618930
*
```
将以上信息保存为`test.inp`，然后运行
```bash
orca test.inp > test.out
```
查看输出文件`test.out`，如果最后一行是`ORCA TERMINATED NORMALLY`，则说明运行成功。

并行计算
```bash
mpirun -np ${NPROCS} orca $JOBNAME > $OUTPUTNAME
```

