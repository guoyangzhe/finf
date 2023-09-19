# Gromacs2018.8编译与安装🎉️

## 1. 安装依赖库
* 安装fftw3.3.8
```bash
wget http://www.fftw.org/fftw-3.3.8.tar.gz
tar -zxvf fftw-3.3.8.tar.gz
cd fftw-3.3.8
./configure --prefix=/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8 --enable-shared --enable-threads --enable-openmp --enable-mpi --enable-sse2 --enable-avx --enable-avx2 --enable-avx512
make -j 4
make install
```
* 安装cmake3
```bash
wget 
tar -zxvf cmake-3.17.5.tar.gz
cd cmake-3.17.5
./bootstrap --prefix=/opt/apps/cmake-3.17.5
make -j 4
make install
# CebtOS 8.0系统自带cmake3，如果不需要安装，可以跳过这一步;CebtOS 7.0系统使用 yum install cmake3 安装
```
* 安装openmpi3.1.4
```bash
wget https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.4.tar.gz
tar -zxvf openmpi-3.1.4.tar.gz
cd openmpi-3.1.4
./configure --prefix=/opt/ohpc/pub/libs/gnu8/openmpi3/3.1.4 --enable-mpi-cxx --enable-mpi-fortran --enable-mpi-thread-multiple --with-cuda=/opt/apps/cuda-10.1 --with-cuda-libdir=/opt/apps/cuda-10.1/lib64
make -j 4
make install
```

## 2. 安装gromacs2018.8
- 下载GROMACS 2018.8压缩包，然后将之解压。进入解压后的目录，在终端里依次运行
```bash
mkdir build
cd build
export CMAKE_PREFIX_PATH=/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8
cmake3 .. -DCMAKE_INSTALL_PREFIX=/opt/apps/gmx2018.8
```
* （如果你是用的`CentOS 8`，或者手动编译的`cmake`，这里`cmake3`改为`cmake`。另外，这一步运行后也仔细看看屏幕上的提示，了解当前`CPU`支持的最佳的`SIMD`指令集有没有正确判断对。如果你的CPU较新却用较老的GROMACS，可能支持的SIMD根本没识别出来，此时GROMACS的`mdrun`运行速度会非常慢）
- 完成之后运行
```bash
make install -j  #Intel四核机子下，不到10分钟就能编译完毕。
```
- 此时程序就被编译和安装到了`/opt/apps/gmx2018.8`目录下。修改用户目录下的`.bashrc`文件（比如运行`gedit ~/.bashrc`），在末尾加入`source /opt/apps/gmx2018.8/bin/GMXRC`，然后保存。
- 之后关闭终端窗口，再次打开终端，输入`gmx -version`，看看是否输出了`GROMACS的相关信息`，是的话就说明安装成功了。之后可以把GROMACS压缩包和解压出来的目录删掉。
---
    _注意，在使用gmx mdrun跑任务时，如果一开始提示WARNING: Using the slow plain C kernels. This should not happen during routine usage on supported platforms，说明编译时没有利用CPU的SIMD指令集（正常情况理应自动检测并利用），这样编译出来的mdrun的运行速度往往比理想情况慢N倍。此时需要重新编译，在使用cmake3的时候明确指定要用的指令集，比如如果你的CPU支持AVX2指令集（XEON v3系列及之后都支持）就加上-DGMX_SIMD=AVX2_256。_

==该软件的环境变量设置如下：==
```bash
#intel#
source /opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mkl/bin/mklvars.sh intel64 && \
source /opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/bin/ifortvars.sh intel64 && \
source /opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/bin/iccvars.sh intel64 && \
source /opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mpi/intel64/bin/mpivars.sh intel64
#fftw338#
export FFTW_HOME=/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8 && \
export PATH=$FFTW_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$FFTW_HOME/lib:$LD_LIBRARY_PATH && \
export INCLUDE=$FFTW_HOME/include:$INCLUDE && \
export MANPATH=$FFTW_HOME/share/man:$MANPATH && \
export C_INCLUDE_PATH=$FFTW_HOME/include:$C_INCLUDE_PATH
#GMX2018.8#
source /opt/apps/gmx2018.8/bin/GMXRC
#Grace  yum install grace,  then in terminal run `xmgrace` to open software
#packmol
export PATH=$PATH:/opt/apps/tools/packmol-17.333
# VMD, then in terminal run `vmd` to open software
export PATH=$PATH:/opt/apps/tools/vmd-1.9.3
```
* 建议将该环境变量单独写为一个`filename.sh`文件，然后在`.bashrc`中`source`该文件，这样可以避免`.bashrc`文件过长，不便于查看(也可以单独source该文件`source filename.sh`,避免软件以及库之间冲突)。
