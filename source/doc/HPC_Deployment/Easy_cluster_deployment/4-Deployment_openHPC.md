# 部署OpenHPC

## 1. 安装OpenHPC
可下载的tar文件：一个包含二进制包的仓库以及任何可用的更新，另一个包含RPMS的源代码仓库。tar文件还包含一个小的bash脚本，用来配置yum在下载后使用本地的资源库。使用时，只需解压你想存放本地仓库的tarball，然后执行`make_repo.sh`脚本。
```bash
ls /opt/ohpc/repos
# 输出：
# CentOS_7  make_repo.sh  OpenHPC-1.3.9.CentOS_7.x86_64.tar OpenHPC.local.repo README
```

```bash 
# ./make_repo.sh
--> Creating OpenHPC.local.repo file in /etc/yum.repos.d
--> Local repodata stored in /opt/ohpc/repos
```

```bash
cat /etc/yum.repos.d/OpenHPC.local.repo 
# [OpenHPC-local]
# name=OpenHPC-1.3 - Base
# baseurl=file:///opt/ohpc/repos/CentOS_7
# gpgcheck=1
# gpgkey=file:///opt/ohpc/repos/CentOS_7/repodata/repomd.xml.key


# [OpenHPC-local-updates]
# name=OpenHPC-1.3.9 - Updates
# baseurl=file:///opt/ohpc/repos/CentOS_7/updates
# gpgcheck=1
# gpgkey=file:///opt/ohpc/repos/CentOS_7/updates/repodata/repomd.xml.key
```

## 2. 使用方法
```bash
yum list | grep OpenHPC  #查看所有ophc的源，可以选择安装
yum install gnu8-compilers-ohpc.x86_64  #安装示例
```
## 3. 安装OpenHPC软件包
* CentOS7使用OpenHPC安装高版本gcc, g++, gfortran等工具
```bash
yum -y install gnu8-compilers-ohpc.x86_64
```
环境变量为：
```bash
export GNU_HOME=/opt/ohpc/pub/compiler/gcc/8.3.0 && \
export PATH=$GNU_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$GNU_HOME/lib:$GNU_HOME/lib64:$LD_LIBRARY_PATH && \
export INCLUDE=$GNU_HOME/include:$INCLUDE && \
export MANPATH=$GNU_HOME/share/man:$MANPATH
```

```bash
gcc -v
```
## 4. 可能需要安装的软件包
注：根据个人情况安装，不一定需要安装
```bash
-------------------------------------- /opt/ohpc/pub/moduledeps/intel-impi ---------------------------------------
   adios/1.13.1     imb/2018.1              netcdf/4.7.1      py2-mpi4py/3.0.2        sionlib/1.7.4
   boost/1.71.0     mfem/4.0                omb/5.6.2         py3-mpi4py/3.0.1        slepc/3.12.0
   dimemas/5.4.1    mpiP/3.4.1              petsc/3.12.0      py3-mpi4py/3.0.2 (D)    superlu_dist/6.1.1
   extrae/3.7.0     mumps/5.2.1             phdf5/1.10.5      scalapack/2.0.2         tau/2.28
   geopm/1.0.0      netcdf-cxx/4.3.1        pnetcdf/1.12.0    scalasca/2.5            trilinos/12.14.1
   hypre/2.18.1     netcdf-fortran/4.5.2    ptscotch/6.0.6    scorep/6.0

----------------------------------------- /opt/ohpc/pub/moduledeps/intel -----------------------------------------
   hdf5/1.10.5              likwid/4.3.4    mvapich2/2.3.2    pdtoolkit/3.25      py3-numpy/1.15.3
   impi/2018.4.274          metis/5.1.0     ocr/1.0.1         plasma/2.8.0        scotch/6.0.6
   impi/2019.9.304 (L,D)    mpich/3.3.1     openmpi3/3.1.4    py2-numpy/1.15.3    superlu/5.2.1

------------------------------------------- /opt/ohpc/pub/modulefiles --------------------------------------------
   EasyBuild/3.9.4           cmake/3.15.4    hwloc/2.1.0               ohpc       (L)    singularity/3.4.1
   autotools          (L)    gnu/5.4.0       intel/18.0.5.274          papi/5.7.0        valgrind/3.15.0
   charliecloud/0.11         gnu7/7.3.0      intel/19.1.3.304 (L,D)    pmix/2.2.2
   clustershell/1.8.2        gnu8/8.3.0      llvm5/5.0.1               prun/1.3   (L)
```
5. 安装module
```bash
# 目前发现，部署openhpc的autotools（或其他包ohpc, EasyBuild），会自动部署好module。因此不需要单独安装。
# 实在不行再安装 environment-modules。
```