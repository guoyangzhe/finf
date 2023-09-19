# Abinit 编译与安装

## 1. Abinit 简介

* Abinit 是一个第一性原理计算软件, 可以用于计算周期性体系的电子结构和光学性质. Abinit 的计算过程是基于密度泛函理论的, 使用平面波基组和赝势, 计算过程中使用了很多高效的算, 如快速傅里叶变换、快速多极子算法等. Abinit 的计算过程是自动化的, 用户只需要提供一个输入文件, Abinit 就可以自动完成计算过程.

* Abinit 的官方网站是: <http://www.abinit.org>, 在这里可以下载到 Abinit 的源代码和文档. Abinit 的源代码是开源的, 可以在 GitHub 上找到.

## 2. Abinit 的编译与安装

*注意：Abinit原始安装包仍然有用, 可以直接在解压后的文件夹进行编译安装, 安装成功后请不要删除编译文件.*

### 2.1 环境

* 激活环境变量

    ```bash
    # intel2019
    source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/mkl/bin/mklvars.sh intel64 && \
    source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/bin/ifortvars.sh intel64 && \
    source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/bin/iccvars.sh intel64 && \
    source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/mpi/intel64/bin/mpivars.sh intel64
    # Openmpi4.1.1
    export MPI_HOME=/opt/libraries/gnu8-openmpi/4.1.1 && \
    export PATH=$MPI_HOME/bin:$PATH && \
    export LD_LIBRARY_PATH=$MPI_HOME/lib:$LD_LIBRARY_PATH && \
    export INCLUDE=$MPI_HOME/include:$INCLUDE && \
    export MANPATH=$MPI_HOME/share/man:$MANPATH
    # libxc4.3.4
    export LIBXC_HOME=/opt/libraries/gnu8-libxc/4.3.4 && \
    export PATH=$LIBXC_HOME/bin:$PATH && \
    export LD_LIBRARY_PATH=$LIBXC_HOME/lib:$LD_LIBRARY_PATH && \
    export LIBRARY_PATH=$LIBXC_HOME/lib:$LIBRARY_PATH && \
    export INCLUDE=$LIBXC_HOME/include:$INCLUDE && \
    export C_INCLUDE_PATH=$LIBXC_HOME/include:$C_INCLUDE_PATH
    # fftw3.3.8
    export FFTW_HOME=/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8 && \
    export PATH=$FFTW_HOME/bin:$PATH && \
    export LD_LIBRARY_PATH=$FFTW_HOME/lib:$LD_LIBRARY_PATH && \
    export INCLUDE=$FFTW_HOME/include:$INCLUDE && \
    export MANPATH=$FFTW_HOME/share/man:$MANPATH && \
    export C_INCLUDE_PATH=$FFTW_HOME/include:$C_INCLUDE_PATH
    ```

### 2.2 下载源代码初步配置

* 下载 Abinit 源代码

    <https://www.abinit.org/packages>

* 配置configure

    ```bash
    tar -zxvf abinit-9.8.4.tar.gz
    cd abinit-9.8.4
    ./configure FC=mpiifort CC=mpiicc XCC=mpiicpc --prefix=/opt/apps/abinit-9.8.4 --with-fftw3=/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8 --with-libxc=/opt/libraries/gnu8-libxc/4.3.4 --enable-mpi-io=yes --with-mpi=/opt/libraries/gnu8-openmpi/4.1.1 --enable-mpi-inplace=yes --enable-openmp=yes --enable-bse-unpacked=yes --enable-gw-dpc=yes 
    # --enable-bigdft --enable-atompaw --enable-wannier90 --enable-libpsml  --enable-xmlf90
    ```

* 此时必然会报错，但这是我们希望的，因为 `目的是要在 fallbacks 目录下产生 build-abinit-fallbacks.sh`

* 报错信息如下:

    ```bash
    ==============================================================================
    === Feature triggers summary                                               ===
    ==============================================================================


    Abinit feature triggers status
    ==============================

    The following summary table indicates the status of the feature triggers,
    whether they are available and working, how they have been initialized
    and whether there are fallbacks to substitute broken ones.

    +----------------+--------+--------+--------+--------+
    |Feature         |Enabled |Init    |Working |Fallback|
    +----------------+--------+--------+--------+--------+
    |abinit_common   |no      |def     |unknown |no      |
    |bigdft          |no      |def     |unknown |disabled|
    |fft             |yes     |def     |yes     |no      |
    |fftw3           |yes     |dir     |unknown |no      |
    |gpu             |no      |def     |no      |no      |
    |hdf5            |yes     |def     |yes     |disabled|
    |levmar          |no      |def     |unknown |no      |
    |libpaw          |no      |def     |unknown |no      |
    |libpsml         |no      |def     |unknown |disabled|
    |libxc           |yes     |dir     |yes     |disabled|
    |libxml2         |no      |def     |unknown |no      |
    |linalg          |yes     |def     |yes     |disabled|
    |mpi             |yes     |dir     |yes     |no      |
    |netcdf          |yes     |def     |no      |disabled|
    |netcdf_fortran  |no      |def     |unknown |disabled|
    |papi            |no      |def     |unknown |no      |
    |pfft            |no      |def     |unknown |no      |
    |triqs           |no      |def     |unknown |no      |
    |wannier90       |no      |def     |unknown |disabled|
    |xmlf90          |no      |def     |unknown |disabled|
    +----------------+--------+--------+--------+--------+


    +------------------------------------------------------------------+
    | WARNING : NetCDF is not WORKING !                                |
    +------------------------------------------------------------------+
    | Please specify the installation directory for NetCDF             |
    +------------------------------------------------------------------+


    +------------------------------------------------------------------+
    | CAUTION : NetCDF Fortran is MANDATORY !                          |
    +------------------------------------------------------------------+
    | suggestion: use with_netcdf_fortran in the ac9 file              |
    +------------------------------------------------------------------+


    +------------------------------------------------------------------+
    | We can help you !                                                |
    +------------------------------------------------------------------+
    | Your environment does not provide mandatory libraries,           |
    | but we can build them for you.                                   |
    |                                                                  |
    | Please issue:                                                    |
    |                                                                  |
    | cd fallbacks                                                     |
    | ./build-abinit-fallbacks.sh                                      |
    |                                                                  |
    | At the end of the process, the options needed to link            |
    | the external libraries will be proposed.                         |
    |                                                                  |
    | copy/paste the options in your ac9 file and rerun configure.     |
    +------------------------------------------------------------------+


    checking that generated files are newer than configure... done
    configure: creating ./config.status
    config.status: creating fallbacks/INSTALL
    config.status: creating fallbacks/README
    config.status: creating fallbacks/build-abinit-fallbacks.sh
    config.status: creating config.h
    config.status: executing depfiles commands
    config.status: executing default commands
    checking which fallbacks to look for... none
    ```

* 下载其他依赖库（也可不下载，但是自动编译过程中会下载，如果您网络有问题，最好手动把包下载到本地，然后去执行操作）

    <https://www.abinit.org/fallbacks>

* 创建tarballs文件夹, 将依赖库放在 `tarballs` 目录下. 默认的tarballs文件夹位置在`${HOME}/.abinit/tarballs`,您也可以通过修改`build-abinit-fallbacks.sh`文件自定义, 最后将依赖库放在自定义的目录下即可.
* 比如我将其放在了 `/opt/apps/abinit-9.8.4/tarballs` 目录下

* 然后进入 `fallbacks` 目录，首先自定义修改 `build-abinit-fallbacks.sh`. (也可以不修改)

    ```bash
    cd /data1/software/abinit/abinit-9.8.4/fallbacks
    nano build-abinit-fallbacks.sh
    ```

* 修改为如下内容：

    ```bash
    # 找到--with-tardir，并修改为如下内容：
    --with-tardir="/opt/software/abinit/tarballs" # 此处定义了依赖库的下载目录
    # 修改需要配置的库
    # Configure
    ./configure \
    --prefix="${fallbacks_prefix}" \
    --with-tardir="/opt/apps/abinit-9.8.4/tarballs" \
    --with-linalg-incs=" -m64 -I/opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/mkl/include" \
    --with-linalg-libs="-lopenblas -lpthread" \
    --with-fc-vendor="gnu" \
    --with-fc-version="8.3" \
    --enable-bigdft \   # enable修改为enable
    --enable-atompaw \   # enable修改为enable
    --enable-wannier90 \   # enable修改为enable
    --enable-libpsml --enable-xmlf90 \   # enable修改为enable
    LIBS_NETCDF4_FORTRAN="-ldl -lm -lz" \
    CC="/opt/libraries/gnu8-openmpi/4.1.1/bin/mpicc" \
    CXX="/opt/libraries/gnu8-openmpi/4.1.1/bin/mpic++" \
    FC="/opt/libraries/gnu8-openmpi/4.1.1/bin/mpif90"
    ```

* 然后运行 `build-abinit-fallbacks.sh`，开始编译依赖库

    ```bash
    ./build-abinit-fallbacks.sh
    ```

* 默认安装的依赖库：

```bash
    +----------------+--------+--------+--------+--------+
    |Fallback        |Status  |Install |Custom  |Tricks  |
    +----------------+--------+--------+--------+--------+
    |atompaw         |unknown |no      |no      |unknown |
    |bigdft          |unknown |no      |no      |unknown |
    |hdf5            |ok      |yes     |no      |yes     |
    |libpsml         |unknown |no      |no      |unknown |
    |libxc           |ok      |yes     |no      |yes     |
    |linalg          |ok      |no      |no      |unknown |
    |netcdf4         |ok      |yes     |no      |partial |
    |netcdf4_fortran |ok      |yes     |yes     |yes     |
    |wannier90       |unknown |no      |no      |unknown |
    |xmlf90          |broken  |no      |no      |unknown |
    +----------------+--------+--------+--------+--------+
```

* 编译完成后，会在当前目录下生成一个 `install_fb` 目录，里面包含了所有的依赖库(默认只安装四个依赖库：hdf5, libxc, netcdf4, netcdf4_fortran, 可以enable将其他库安装上)

* 完成后的输出如下：

    ```bash

    The fallbacks are now ready to use.
    You can link these fallbacks with Abinit by copying the following options to your ac9 file.

    with_libxc=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/libxc/6.0.0

    with_hdf5=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/hdf5/1.10.8

    with_netcdf=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/netcdf4/4.9.0

    with_netcdf_fortran=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/netcdf4_fortran/4.6.0

    with_xmlf90=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/xmlf90/1.5.6

    with_libpsml=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/libpsml/1.1.12

    with_wannier90=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/wannier90/2.0.1.1

    ```

### 2.3 编译安装Abinit

* 然后回到源代码目录`/opt/apps/abinit-9.8.4`, 运行 configure

    ```bash
    cd ..
    ./configure FC=mpiifort CC=mpiicc XCC=mpiicpc --prefix=/opt/apps/abinit-9.8.4 --with-fftw3=/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8 --enable-mpi-io=yes --with-mpi=/opt/libraries/gnu8-openmpi/4.1.1 --enable-mpi-inplace=yes --enable-openmp=yes --enable-bse-unpacked=yes --enable-gw-dpc=yes with_libxc=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/libxc/6.0.0 with_hdf5=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/hdf5/1.10.8 with_netcdf=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/netcdf4/4.9.0 with_netcdf_fortran=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/netcdf4_fortran/4.6.0 with_xmlf90=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/xmlf90/1.5.6 with_libpsml=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/libpsml/1.1.12 with_wannier90=/opt/apps/abinit-9.8.4/fallbacks/install_fb/gnu/8.3/wannier90/2.0.1.1
    ```

* 然后运行 make

    ```bash
    make -j 8
    ```

* 最后运行 make install

    ```bash
    make install
    ```

* 完成后的输出如下：

    ```bash
    Keywords to use with the make command for abichecks tests directory:

    tests_abirules     Launch the abirules tests
                    Warning: for some of the tests, the file make.log
                    must be present in the top directory. This means one has
                    to compile with the command: `make > make.log 2>&1`

    tests_buildsys     Launch the buildsys tests

    tests_libpaw       Launch the libpaw tests

    ==============================================================================
    [This file can be found at doc/help_make/help_make_abichecks.txt]
    make[2]: Entering directory `/opt/apps/abinit-9.8.4/abichecks'
    make[2]: Nothing to be done for `install-exec-am'.
    make[2]: Nothing to be done for `install-data-am'.
    make[2]: Leaving directory `/opt/apps/abinit-9.8.4/abichecks'
    make[1]: Leaving directory `/opt/apps/abinit-9.8.4/abichecks'
    Making install in doc
    make[1]: Entering directory `/opt/apps/abinit-9.8.4/doc'
    make[2]: Entering directory `/opt/apps/abinit-9.8.4/doc'
    make[2]: Nothing to be done for `install-exec-am'.
    make[2]: Nothing to be done for `install-data-am'.
    make[2]: Leaving directory `/opt/apps/abinit-9.8.4/doc'
    make[1]: Leaving directory `/opt/apps/abinit-9.8.4/doc'
    Making install in tests
    make[1]: Entering directory `/opt/apps/abinit-9.8.4/tests'
    make[2]: Entering directory `/opt/apps/abinit-9.8.4/tests'
    make[2]: Nothing to be done for `install-exec-am'.
    make[2]: Nothing to be done for `install-data-am'.
    make[2]: Leaving directory `/opt/apps/abinit-9.8.4/tests'
    make[1]: Leaving directory `/opt/apps/abinit-9.8.4/tests'
    make[1]: Entering directory `/opt/apps/abinit-9.8.4'
    make[2]: Entering directory `/opt/apps/abinit-9.8.4'
    make[2]: Nothing to be done for `install-exec-am'.
    /bin/install -c -d -m 755 /opt/apps/abinit-9.8.4/lib/pkgconfig
    /bin/install -c -m 644 -m 644 config.pc \
    /opt/apps/abinit-9.8.4/lib/pkgconfig/abinit.pc
    make[2]: Leaving directory `/opt/apps/abinit-9.8.4'
    make[1]: Leaving directory `/opt/apps/abinit-9.8.4'
    ```

* 之后就可以在`/opt/apps/abinit-9.8.4/bin`目录下找到编译好的 Abinit 了.

### 2.4 测试

* 进入 abinit-9.8.2/tests 目录下测试一下：

    ```bash
    cd /opt/apps/abinit-9.8.4/tests
    ./runtests.py fast -j 4
    ```

### 2.5 Abinit 的使用

* 查看版本：

    ```bash
    abinit --version
    ```

* 查看帮助：

    ```bash
    abinit --help
    ```

* 查看帮助文档：

    ```bash
    abinit --help=topics
    ```

* 查看build信息：

    ```bash
    abinit -b
    ```

### 2.6 最终环境变量

* 最终环境变量如下：

    ```bash
    #intel2019#
    source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/mkl/bin/mklvars.sh intel64 && \
    source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/bin/ifortvars.sh intel64 && \
    source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/bin/iccvars.sh intel64 && \
    source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/mpi/intel64/bin/mpivars.sh intel64

    #Openmpi4.1.1#
    export MPI_HOME=/opt/libraries/gnu8-openmpi/4.1.1 && \
    export PATH=$MPI_HOME/bin:$PATH && \
    export LD_LIBRARY_PATH=$MPI_HOME/lib:$LD_LIBRARY_PATH && \
    export INCLUDE=$MPI_HOME/include:$INCLUDE && \
    export MANPATH=$MPI_HOME/share/man:$MANPATH

    # FFTW-3.3.8
    export FFTW_HOME=/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8 && \
    export PATH=$FFTW_HOME/bin:$PATH && \
    export LD_LIBRARY_PATH=$FFTW_HOME/lib:$LD_LIBRARY_PATH && \
    export INCLUDE=$FFTW_HOME/include:$INCLUDE && \
    export MANPATH=$FFTW_HOME/share/man:$MANPATH && \
    export C_INCLUDE_PATH=$FFTW_HOME/include:$C_INCLUDE_PATH

    #Abinit-9.8.4#
    export ABI_HOME=/opt/apps/abinit-9.8.4
    export PATH=$ABI_HOME/bin:$PATH
    export MANPATH=$ABI_HOME/src/98_main/:$MANPATH      # Do not change this line: path to executable
    export ABI_TESTS=$ABI_HOME/tests/                   # Do not change this line: path to tests dir
    export ABI_PSPDIR=$ABI_TESTS/Psps_for_tests/        # Do not change this line: path to pseudos dir
    ```

### 2.6 并行计算

* Abinit 的并行计算需要使用 MPI，下面是一个简单的并行计算的例子：

    ```bash
    mpirun -np 4 abinit < input.files > output.files
    # 示例：
    mpirun -np ${NPROCS} abinit < t00.abi > t00.out
    ```
