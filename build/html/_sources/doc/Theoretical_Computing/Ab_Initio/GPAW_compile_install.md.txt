# GPAW编译与安装

注：
手动方式安装`gpaw`最重要的是修改`customize.py`文件，在文件里把要关联的库路径添加修改正确，并把`False`改为`True`。只有把`customize.py`文件看懂，才能正确编译`gpaw`

- 官方要求的安装必要软件包

官网安装说明链接<https://wiki.fysik.dtu.dk/gpaw/install.html#>

- Python 3.5 or later（使用python3.5以上版本是因为ase需要的python版本已经是3.5了）
- NumPy 1.9 or later (base N-dimensional array package)
- SciPy 0.14 or later (library for scientific computing)
- ASE 3.18.0 or later (atomic simulation environment)
- a C-compiler
- LibXC 3.x or 4.x
- BLAS and LAPACK libraries

Optional, but highly recommended:

- an MPI library (required for parallel calculations)
- FFTW (for increased performance)
- BLACS and ScaLAPACK

## 1. 安装依赖库

安装`anaconda3`之后，一些`python`库就可以安装了，`Python`、`Numpy`、`Scipy`、`ASE`、`matplotlib`均可安装在库中

```bash
pip install **** 
```

### 1.1 安装`BLAS`、`LAPACK`（Ubuntu系统直接安装，不需要自行编译）

```bash
参考Octopus安装说明
```

### 1.2 安装SCALAPACK（可选择系统直接安装，不需要自行编译）

```bash
tar xvf scalapack_installer.tgz 
cd scalapack_installer 
```

修改`setup.py`文件，把`prefix`改为`/home/gn/gpaw2160/scalapack`，把`f90`改为`gfortran`，把`downall`改为`True`，保存退出

```bash
./setup.py --prefix=/home/gn/gpaw2160/scalapack --f90=gfortran --downall
```

创建软链接:
把编译的`libscalapack.a`拷贝到`/usr/lib64`目录下，并链接为`libscalapack-openmpi.a`

```bash
ln -s /usr/lib64/libscalapack.a /usr/lib64/libscalapack-openmpi.a
```

### 1.3 安装`FFTW`（需要重新编译）

大多数软件并不需要fftw编译并行，但gpaw需要libfftw3_mpi.so
下载
ftp://ftp.fftw.org/pub/fftw/fftw-3.3.5.tar.gz
安装

```bash
tar xvf fftw-3.3.5.tar.gz
cd fftw-3.3.5
./configure --prefix=/opt/libraries/gnu8-fftw/3.3.4 --enable-mpi --enable-shared=yes
make
make install
```

查看`/opt/libraries/gnu8-fftw/3.3.4/lib`目录中，如果有`libfftw3_mpi`文件即为成功。

### 1.4 安装`openmpi`（需要重新编译）

下载<https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.1.tar.gz>

安装

```bash
tar xvf openmpi-4.1.1.tar.gz
cd openmpi-4.1.1
./configure --prefix=/opt/libraries/gnu8-openmpi/4.1.4
make all install -j
vi ~/.bashrc
export PATH=$PATH:/sob/openmpi313/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/sob/openmpi313/lib
source ~/.bashrc
```

### 1.5 安装`libxc`（需要重新编译）

下载<https://gitlab.com/libxc/libxc/-/archive/4.3.4/libxc-4.3.4.tar.gz>

安装

```bash
tar xvf libxc-4.3.4.tar.gz cd libxc-4.3.4  ./configure --prefix=/opt/libraries/gnu8-libxc/4.3.4 --enable-shared && make && make install
```

这是一个密度泛函理论(`DFT`)的交换关联泛函库，其中你可以找到不同类型的泛函，例如：`LDA`, `GGA`, `hybrids`, 和 `mGGA`。 `Libxc`库也可以用于`Abinit`软件，目前最新版本为6.1.0。

### 1.6 安装`ELPA`（需要重新编译）

下载<https://elpa.mpcdf.mpg.de/html/Releases/2021.05.001/elpa-2021.05.001.tar.gz>

安装

```bash
./configure --prefix=/opt/libraries/gnu8-elpa/2021.05.002 FC=mpiifort CC=mpiicc CXX=mpiicpc CFLAGS="-O3 -xHost" CXXFLAGS="-O3 -xHost" FCFLAGS="-O3 -xHost" --enable-openmp

make && make install && make clean
```

### 1.7 安装`libvdwxc`（需要重新编译）

```bash
yum install fftw3 fftw3-devel
```

下载<https://gitlab.com/libvdwxc/libvdwxc/-/archive/0.4.0/libvdwxc-0.4.0.tar.gz>

安装

```bash
./configure --prefix=/opt/libraries/gnu8-libvdwxc/0.4.0 CC="gcc" FC="gfortran" CFLAGS="-O3 -march=native" FCFLAGS="-g -O2"

make -j && make install
```

## 2. 安装`gpaw`

### 2.1 下载`gpaw`源码

```bash
wget https://gitlab.com/gpaw/gpaw/-/archive/master/gpaw-master.tar.gz
tar xvf gpaw-22.8.0.tar.gz
cd gpaw-22.8.0
```

### 2.2 修改`siteconfig.py`文件

复制`siteconfig.py.example`文件为`siteconfig.py`文件

```bash
cp siteconfig.py.example siteconfig.py
```

修改`siteconfig.py`文件

```bash
nano siteconfig.py
```

改为如下内容

```bash
"""User provided customizations.

Here one changes the default arguments for compiling _gpaw.so.

Here are all the lists that can be modified:

* libraries
  List of libraries to link: -l<lib1> -l<lib2> ...
* library_dirs
  Library search directories: -L<dir1> -L<dir2> ...
* include_dirs
  Header search directories: -I<dir1> -I<dir2> ...
* extra_link_args
  Arguments forwarded directly to linker
* extra_compile_args
  Arguments forwarded directly to compiler
* runtime_library_dirs
  Runtime library search directories: -Wl,-rpath=<dir1> -Wl,-rpath=<dir2> ...
* extra_objects
* define_macros

The following lists work like above, but are only linked when compiling
the parallel interpreter:

* mpi_libraries
* mpi_library_dirs
* mpi_include_dirs
* mpi_runtime_library_dirs
* mpi_define_macros

To override use the form:

    libraries = ['somelib', 'otherlib']

To append use the form

    libraries += ['somelib', 'otherlib']
"""

# flake8: noqa

# compiler = 'gcc'
# mpicompiler = 'mpicc'
# mpilinker = 'mpicc'
# platform_id = ''

# FFTW3:
fftw = True
if fftw:
    libraries += ['fftw3']
    library_dirs += ['/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8/lib/']
# ScaLAPACK (version 2.0.1+ required):
scalapack = True
if scalapack:
    libraries += ['scalapack','openblas']
    library_dirs += ['/opt/ohpc/pub/libs/gnu8/openmpi3/scalapack/2.0.2/lib/','/opt/ohpc/pub/libs/gnu8/openblas/0.3.7/lib/']

# Use Elpa (requires ScaLAPACK and Elpa API 20171201):
if 0:
    elpa = True
    elpadir = '/opt/libraries/gnu8-elpa/2021.05.002'
    libraries += ['elpa']
    library_dirs += ['{}/lib'.format(elpadir)]
    extra_link_args += ['-Wl,-rpath={}/lib'.format(elpadir)]
    include_dirs += ['{}/include/elpa_openmp-2021.05.002'.format(elpadir)]

# LibXC:
# In order to link libxc installed in a non-standard location
# (e.g.: configure --prefix=/home/user/libxc-2.0.1-1), use:

# - static linking:
if 0:
    xc = '/opt/libraries/gnu8-libxc/4.3.4/'
    include_dirs += [xc + 'include']
    extra_link_args += [xc + 'lib/libxc.a']
    if 'xc' in libraries:
        libraries.remove('xc')

# - dynamic linking (requires rpath or setting LD_LIBRARY_PATH at runtime):
if 0:
    xc = '/opt/libraries/gnu8-libxc/4.3.4/'
    include_dirs += [xc + 'include']
    library_dirs += [xc + 'lib']
    # You can use rpath to avoid changing LD_LIBRARY_PATH:
    extra_link_args += ['-Wl,-rpath={xc}/lib'.format(xc=xc)]
    if 'xc' not in libraries:
        libraries.append('xc')


# libvdwxc:
if 0:
    libvdwxc = True
    path = '/opt/libraries/gnu8-libvdwxc/0.4.0'
    extra_link_args += ['-Wl,-rpath=%s/lib' % path]
    library_dirs += ['%s/lib' % path]
    include_dirs += ['%s/include' % path]
    libraries += ['vdwxc']

extra_compile_args += ['-fopenmp']
extra_link_args += ['-fopenmp']
```

注：`fftw`、`scalapack`、`elpa`、`libxc`、`libvdwxc`这些库的路径需要根据实际情况修改。

如果是在服务器上编译（有ophc和PBS）
写好siteconfig.py文件之后保存退出
加载所有能用到的库
然后开始编译
```python3 setup.py install``` (这样才能把所有的库安装上)
如果使用pip，则不能安装所有的库，会失败

以后更新gpaw，直接下载源码，编写siteconfig.py文件，进行编译即可，切记要升级一些依赖的库。

## 3. 安装`gpaw`所需的赝势文件（Install PAW datasets）

```bash
gpaw install-data ~/gpaw-21.6.0/datasets
```

## 4. 测试`gpaw`

```bash
cd path_to_gpaw/gpaw-22.8.0
python3 -c "import gpaw; print(gpaw.__version__)"
```

## 5. 最终软件的环境变量（仅作参考）

```bash
#GPAW#
conda activate gpaw

export MPI_HOME=/opt/ohpc/pub/mpi/openmpi3-gnu8/3.1.4 && \
export PATH=$MPI_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$MPI_HOME/lib:$LD_LIBRARY_PATH && \
export INCLUDE=$MPI_HOME/include:$INCLUDE && \
export MANPATH=$MPI_HOME/share/man:$MANPATH && \

export LIBXC_HOME=/opt/libraries/gnu8-libxc/4.3.4 && \
export PATH=$LIBXC_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$LIBXC_HOME/lib:$LD_LIBRARY_PATH && \
export LIBRARY_PATH=$LIBXC_HOME/lib:$LIBRARY_PATH && \
export INCLUDE=$LIBXC_HOME/include:$INCLUDE && \
export C_INCLUDE_PATH=$LIBXC_HOME/include:$C_INCLUDE_PATH && \

export FFTW_HOME=/opt/ohpc/pub/libs/gnu8/openmpi3/fftw/3.3.8 && \
export PATH=$FFTW_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$FFTW_HOME/lib:$LD_LIBRARY_PATH && \
export INCLUDE=$FFTW_HOME/include:$INCLUDE && \
export MANPATH=$FFTW_HOME/share/man:$MANPATH && \
export C_INCLUDE_PATH=$FFTW_HOME/include:$C_INCLUDE_PATH && \

export OPENBLAS_HOME=/opt/ohpc/pub/libs/gnu8/openblas/0.3.7 && \
export PATH=$OPENBLAS_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$OPENBLAS_HOME/lib:$LD_LIBRARY_PATH && \
export LIBRARY_PATH=$OPENBLAS_HOME/lib:$LIBRARY_PATH && \
export INCLUDE=$OPENBLAS_HOME/include:$INCLUDE && \

export SCALAPACK_HOME=/opt/ohpc/pub/libs/gnu8/openmpi3/scalapack/2.0.2 && \
export PATH=$SCALAPACK_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$SCALAPACK_HOME/lib:$LD_LIBRARY_PATH && \
export LIBRARY_PATH=$SCALAPACK_HOME/lib:$LIBRARY_PATH && \
export INCLUDE=$SCALAPACK_HOME/include:$INCLUDE && \

export ELPA_HOME=/opt/libraries/gnu8-elpa/2021.05.002 && \
export PATH=$ELPA_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$ELPA_HOME/lib:$LD_LIBRARY_PATH && \
export INCLUDE=$ELPA_HOME/include:$INCLUDE && \
export MANPATH=$ELPA_HOME/share/man:$MANPATH && \
export C_INCLUDE_PATH=$ELPA_HOME//include/elpa_openmp-2021.05.002/elpa/:$C_INCLUDE_PATH && \

export LIBVDWXC_HOME=/opt/libraries/gnu8-libvdwxc/0.4.0 && \
export PATH=$LIBVDWXC_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$LIBVDWXC_HOME:$LD_LIBRARY_PATH && \
export LIBRARY_PATH=$LIBVDWXC_HOME:$LIBRARY_PATH && \
export INCLUDE=$LIBVDWXC_HOME/include:$INCLUDE

#gpaw-tools
export PATH="/opt/apps/tools/gpaw-tools-23.2.0:$PATH"
```

## 6. 安装`gpaw-tools`

```bash
conda activate gpaw
pip install gpaw-tools
```

## 7. 激活环境变量后再次测试`gpaw`

```bash
gpaw info
gpaw info | grep -i 'libxc'
gpaw test
gpaw test --parallel=2
```

## 8. 编者注

- 由于作者时间有限，本文中的安装流程没有经过严格的测试，仅供参考。如果有问题，欢迎提出issue，或者直接联系作者。
- 本文存在很多问题，读者切不可照搬，待作者有时间一定进行修正。
