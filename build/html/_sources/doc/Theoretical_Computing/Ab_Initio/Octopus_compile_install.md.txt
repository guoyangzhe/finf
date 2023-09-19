# Octopus编译与安装
## 1. 简介
- Ocotpus 是一款科学计算软件，可以对多种不同体系进行从头计算(ab initio)的模拟。在密度泛函理论(DFT)的理论框架下用量子力学来描述电子, 而核用经典的点粒子描述，电子-核相互作用以赝势近似来描述。Octopus可以进行基态计算，也可以利用时间密度泛函(TDDFT)进行时间依赖的模拟。
- Octopus 还支持MPI和OpenMP来进行并行计算，也支持OpenCL和CUDA利用GPU计算
- Octopus是一款Linux系统下的免费软件，在GNU通用公共许可证框架下发布，你可以免费下载，使用，修改。
- Octopus的安装过程比较复杂，因为它有很多依赖库。笔者根据octopus官网提供的详细安装指南，在此分享如何在个人计算机 CentOS7.9 系统中安装Octopus的全过程。

## 2. 编译器相关
### 2.1 编译器
* Octopus的代码使用标准 Fortran 2003写成，还有一些例程(routines)是使用C语言编写，所以我们需要一个C编译器和Fortran 2003 编译器。命令行下直接使用`yum`命令安装即可。
```bash
$ sudo yum install gcc           #C 编译器
$ sudo yum install gfortran      #fortran 编译器
```
*注：最好使用gnu 8.3.0或更高版本*
- 检查是否已经安装过gcc，可以输入以下命令：
```bash
gcc --version #意为查看gcc的版本
```
- 如果已经安装，则会输出相应版本号：
```bash
gcc (GCC) 8.3.0
Copyright (C) 2018 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
### 2.2 编译器标志
- 通常编译器标志(Compiler flags)为系统自动选择的优化标志，但在安装Octopus过程中，需要我们指定标志，亲测使用不同标志会导致安装报错。这里，C编译器标志指定为 -O3(大写字母O)，fortran编译器标志为 -O3 -ffree-line-length-none ，目前还不需要指定操作，在后面安装依赖库的时候才需要指定标志。
---
## 3. 依赖库
### 3.1 依赖库的安装
1. 首先，`make`, `automake`, `m4`, `libtool` 这几个包是必要条件，可以直接用`yum`安装，使用`-–version` 来检查是否安装成功。
```bash
sudo yum install make
sudo yum install automake
sudo yum install m4
sudo yum install libtool
```
- 其中make和automake是重要的编译工具，在linux环境下安装软件，一般都通过 配置->编译->安装 这个过程实现，即：
```./configure  ->  make  ->  make install```
- `m4`是是一个通用的宏处理器，大多数人需要 `m4` 仅仅是因为 `GNU autoconf`中的 `configure` 脚本依赖它。
- `libtool`是处理动态链接库的工具，可以解决库依赖的问题，将使用动态库的复杂性隐藏在统一、可移植的接口中。
2. 接下来还有5个数学库：`BLAS`，`LAPACK`，`GSL`，`FFTW3`，`LibXC`，下面逐一介绍。

- 在安装数学库之前，我们先创建一个文件夹来作为各种库的安装位置，一般放在`/opt/libraries`。
### 3.2 安装BLAS
- BLAS (Basic Linear Algebra Subprograms)即基本线性代数子程序，提供用于执行基本矢量和矩阵运算的标准构建块的例程。1级BLAS执行标量，矢量和矢量-矢量运算，2级BLAS执行矩阵矢量运算，3级BLAS执行矩阵运算。 由于BLAS高效，便携且广泛可用，因此它们通常用于开发高质量线性代数软件，例如`LAPACK`。
- 首先在网上下载压缩包：blas.tgz[http://www.netlib.org/blas/blas.tgz]
- 解压压缩包并进入新创建的 BLAS 文件夹
- 编辑 `make.inc` 文件，并修改`fortran`编译器的标志为：(可以不做修改如果不报错的话)
```bash
FORTRAN  = gfortran
OPTS     = -O3 -ffree-line-length-none
DRVOPTS  = $(OPTS)
NOOPT    =
LOADER   = gfortran
LOADOPTS =
```
- 接下来使用`make`命令来进行编译，这会花费一段时间。
```bash
make
```
- 然后在当前路径下创建新文件夹 `lib`
```bash
mkdir lib
```
- 将make命令后新产生的文件 blas_LINUX.a 复制到 ./lib/ 文件夹下并重命名
```bash
cp  blas_LINUX.a   ./lib/libblas.a
```
- 注：产生的新文件总是叫`blas_LINUX.a`，独立于你所用的操作系统，只是叫这个名字而已。
### 3.3 LAPACK
- Lapack 即 Linear Algebra PACKage，是一个线性代数包，它提供了求解联立线性方程组，线性方程组最小二乘解，特征值问题和奇异值问题的例程，还提供了相关的矩阵因子分解（`LU`，`Cholesky`，`QR`，`SVD`，`Schur`，`广义Schur`），以及相关计算。
- 首先在网上下载压缩包：lapack.tgz[http://www.netlib.org/lapack/lapack.tgz]
- 解压压缩包并进入新产生的 `lapack` 文件夹
- 复制 `make.inc.example` 文件为 `make.inc`
```bash
cp make.inc.example  make.inc
```
- 编辑 `make.inc` 文件，并修改相应编译器的标志为：(可以不做修改如果不报错的话)
```bash
FORTRAN  = gfortran
OPTS     = -O3 -ffree-line-length-none
DRVOPTS  = $(OPTS)
NOOPT    =
LOADER   = gfortran
LOADOPTS =
```
- 接下来使用 `make lib` 命令来进行编译，这会花费一段时间。
```bash
make lib
```
- 将新产生的文件 `liblapack.a` 复制到 `./lib/` 文件夹下并重命名
```bash
cp liblapack.a basedir/lib/liblapack.a
```
- 注：产生的新文件可能叫 `lapack_LINUX.a`（官方教程产生的） ，也可能叫 `liblapack.a`（笔者电脑产生的）
### 3.4 GSL
- 这是一个GNU数学函数库，该库提供了广泛的数学例程，如随机数生成器，特殊函数和最小二乘拟合。
- 首先下载压缩包 gsl-2.6.tar.gz[ftp://ftp.gnu.org/gnu/gsl/gsl-2.6.tar.gz]
- 解压压缩包并进入新产生的文件夹
- 运行配置文件：
```bash
./configure CC="gcc" --prefix=/opt/libraries/gnu8-gsl/2.7 --disable-shared --enable-static
```
- 注：`configure`命令的参数解释之 `--prefix`： 该参数指定了安装路径，这里我们把库安装在之前设好的`路径`下。
- 编译并安装
```bash
make
make install
```
### 3.5 FFTW 3
- FFTW（the Fastest Fourier Transform in the West）是一个C子程序库，用于计算一个或多个维度，任意输入大小，实数和复数数据的离散傅里叶变换（DFT）
首先下载压缩包 fftw-3.3.4.tar.gz[http://www.fftw.org/fftw-3.3.4.tar.gz]
- 解压压缩包并进入新产生的文件夹
- 配置
```bash
./configure  --prefix=/opt/libraries/gnu8-fftw/3.3.8  CC="gcc" CFLAGS="-O3" F77="gfortran" F77FLAGS="-O3 -ffree-line-length-none"
```
- 编译并安装
```bash
make
make install
```
—————————————————————————————————————————————————
### 3.6 LibXC
- 这是一个密度泛函理论(`DFT`)的交换关联泛函库，其中你可以找到不同类型的泛函，例如：`LDA`, `GGA`, `hybrids` 和 `mGGA`。 `Libxc`库也可以用于`Abinit`软件，目前最新版本为`6.1.0`。
- 首先下载压缩包 libxc-4.3.4.tar.gz[http://www.tddft.org/programs/octopus/down.php?file=libxc/4.3.4/libxc-4.3.4.tar.gz]
- 解压压缩包并进入新产生的文件夹
- 配置
```bash
./configure --prefix=/opt/libraries/gnu8-libxc/4.3.4 CC="gcc" CFLAGS="-O3" FC="gfortran" FCFLAGS="-O3 -ffree-line-length-none"
```
- 如果您没有使用稳定版本的tarball，您需要先使用“autoreconf -fi”生成configure文件。这个命令将重新生成configure文件，以便它可以适应您的环境和软件包的特定要求。在生成configure文件后，您可以运行“./configure”命令来配置软件包，并继续进行编译和安装。请注意，这个命令需要在源代码目录中运行，并且您需要安装autotools工具包才能使用它。
- 编译并安装
```bash
make
make install
```
## 4. 编译安装Octopus
### 4.1 Octopus 安装
*编译完这些库后，我们可以开始编译Octopus了*
- 首先下载最新版本的Octopus：octopus-12.2.tar.gz
- 解压压缩包并进入新产生的文件夹
- 定义几个环境变量，用来写配置脚本：
```bash
export LIBS_BLAS=/opt/libraries/gnu8-blas/3.10.0/lib/libblas.a
export LIBS_LAPACK=/opt/libraries/gnu8-lapack/3.9.1/lib/liblapack.a
export LIBS_FFT=/opt/libraries/gnu8-fftw/3.3.8/lib/libfftw3.a
```
- 接下来写配置脚本：
```bash
autoreconf -i
./configure  --prefix=/opt/apps/octopus12.2  --with-gsl-prefix=/opt/libraries/gnu8-gsl/2.7 --with-libxc-prefix=/opt/libraries/gnu8-libxc/4.3.4
```
- 注：`configure`命令的参数解释之 `--with` ：该参数指定了配置文件时去哪里寻找对应的库
- 编译并安装
```bash
make
make install
```
- 如果一切都进展顺利的话，Octopus应该会成功安装在你一开始设定的 `路径` 文件夹内，可执行文件放在 `/opt/apps/octopus12.2` 文件夹内，接下来将其路径添加到环境变量里，以便你可以只输入 `octopus` 就可运行, 而非每次都要输入 `/opt/apps/octopus12.2/octopus` 才行。
```bash
export PATH=$PATH:/opt/apps/octopus12.2/bin/octopus
```
最终整个软件的环境变量为（可能与前面的有差别，读者仔细阅读自行斟酌）：
```bash
export LIBS_BLAS=/opt/libraries/gnu8-blas/3.10.0/lib/libblas.a
export LIBS_LAPACK=/opt/libraries/gnu8-lapack/3.9.1/lib/liblapack.a
export LIBS_FFT=/opt/libraries/gnu8-fftw/3.3.8/lib/libfftw3.a

export GSL_HOME=/opt/libraries/gnu8-gsl/2.7 && \
export PATH=$GSL_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$GSL_HOME/lib:$LD_LIBRARY_PATH && \
export LIBRARY_PATH=$GSL_HOME/lib:$LIBRARY_PATH && \
export INCLUDE=$GSL_HOME/include:$INCLUDE && \
export C_INCLUDE_PATH=$GSL_HOME/include:$C_INCLUDE_PATH && \
export MANPATH=$GSL_HOME/share/man:$MANPATH

export LIBXC_HOME=/opt/libraries/gnu8-libxc/4.3.4 && \
export PATH=$LIBXC_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$LIBXC_HOME/lib:$LD_LIBRARY_PATH && \
export LIBRARY_PATH=$LIBXC_HOME/lib:$LIBRARY_PATH && \
export INCLUDE=$LIBXC_HOME/include:$INCLUDE && \
export C_INCLUDE_PATH=$LIBXC_HOME/include:$C_INCLUDE_PATH && \

export OCTOPUS_HOME=/opt/apps/octopus12.2  && \
export PATH=$OCTOPUS_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$OCTOPUS_HOME/lib:$LD_LIBRARY_PATH && \
export INCLUDE=$OCTOPUS_HOME/include:$INCLUDE && \
export MANPATH=$OCTOPUS_HOME/share/man:$MANPATH

alias octopus='/opt/apps/octopus12.2/bin/octopus'
```
- 该软件的安装就完成了，接下来我们来测试一下。其中环境变量的设置可以写入 `~/.bashrc` 文件中，这样每次打开终端都会自动加载环境变量，不用每次都手动输入；也可以单独写为一个文件，之后使用软件时单独`source`该文件即可。
### 4.2 简单例子运行测试
- 新建一空文件夹并进入，建立一个文件，命名为 `inp` ，并将其内容编辑为：
```bash
CalculationMode = gs

%Coordinates
 'H' | 0 | 0 | 0
%

Spacing = 0.25 * angstrom
Radius = 4.0 * angstrom


```

- 注：文件只能命名为 `inp`， Octopus 只识别这个输入文件名
- 接下来试运行：
```bash
octopus &> output
```
- 即可运行octopus并将输出结果重定向到新建的 output 文件中。
- 将会在产生一个 `output` 文件的同时产生一些文件夹：`exec`、 `restart` 和 `static`。
- 若只运行, 则输出会在屏幕上实时显示。
```bash
octopus
```
- 注：`&>` 表示将标准输出和错误输出都重定向到文件中，若只想重定向标准输出，可以使用 `>` ；若只想重定向错误输出，可以使用 `2>` 。
- 以下是`output` 文件输出内容（仅供参考）：
```
    <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                                ___
                             .-'   `'.
                            /         \
                            |         ;
                            |         |           ___.--,
                   _.._     |0) ~ (0) |    _.---'`__.-( (_.
            __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
           ( ,.--'`   ',__ /./;   ;, '.__.'`    __
           _`) )  .---.__.' / |   |\   \__..--""  """--.,_
          `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
                | |  .' _.-' |  |  \  \  '.               `~---`
                 \ \/ .'     \  \   '. '-._)
                  \/ /        \  \    `=.__`~-.
             jgs  / /\         `) )    / / `"".`\
            , _.-'.'\ \        / /    ( (     / /
             `--~`   ) )    .-'.'      '.'.  | (
                    (/`    ( (`          ) )  '-;
                     `      '-;         (-'

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2, or (at your option)
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA

    <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

                           Running octopus

Version                : 12.2
Commit                 :
Build time             : Sun May  7 09:37:39 EDT 2023
Configuration options  : maxdim3 sse2 libxc_fxc libxc_kxc
Optional libraries     :
Architecture           : x86_64
C compiler             : gcc
C compiler flags       : -g -O2
C++ compiler           : g++
C++ compiler flags     : -g -O2
Fortran compiler       : gfortran (GCC version 8.3.0)
Fortran compiler flags : -pipe -O3 -funroll-loops -ffast-math -ffree-line-length-none

              The octopus is swimming in master (Linux)


            Calculation started on 2023/05/09 at 07:09:08


************************** Calculation Mode **************************
Input: [CalculationMode = gs]
**********************************************************************


******************************* Space ********************************
Octopus will run in 3 dimension(s).
Octopus will treat the system as periodic in 0 dimension(s).
**********************************************************************

Input: [PseudopotentialSet = standard]
Reading Coordinates from Coordinates block

****************************** Species *******************************
  Species 'H'
    type             : pseudopotential
    file             : '/opt/apps/octopus12.2/share/octopus/pseudopotentials/PSF/H.psf'
    file format      : PSF
    valence charge   : 1.0
    atomic number    :   1
    form on file     : semilocal
    orbital origin   : calculated
    lmax             : 0
    llocal           : 0
    projectors per l : 1
    total projectors : 0
    application form : local
    orbitals         : 16
    bound orbitals   :  1

**********************************************************************


***************************** Symmetries *****************************
Symmetry elements : (i) (Cinf) (sigma)
Symmetry group    : Kh
**********************************************************************

Input: [CurvMethod = curv_affine]
Input: [DerivativesStencil = stencil_star]
Input: [SpinComponents = unpolarized]
Input: [SmearingFunction = semiconducting]
Input: [SymmetrizeDensity = no]

******************************* States *******************************
Total electronic charge  =        1.000
Number of states         =        1
States block-size        =        1
**********************************************************************


************************** Parallelization ***************************
Info: Octopus will run in *serial*
**********************************************************************

Info: Generating weights for finite-difference discretization of x-gradient
Info: Generating weights for finite-difference discretization of y-gradient
Info: Generating weights for finite-difference discretization of z-gradient
Info: Generating weights for finite-difference discretization of Laplacian

******************************** Grid ********************************
Simulation Box:
  Type = minimum
  Radius  [b] =   7.559
Main mesh:
  Spacing [b] = ( 0.472, 0.472, 0.472)    volume/point [b^3] =      0.10544
  # inner mesh =      17077
  # total mesh =      30461
  Grid Cutoff [H] =    22.110166    Grid Cutoff [Ry] =    44.220331
**********************************************************************

Info: states-block size = 0.2 MiB
Input: [StatesPack = yes]
Input: [StatesOrthogonalization = cholesky_serial]
Info: the XCFunctional has been selected to match the pseudopotentials
      used in the calculation.

**************************** Theory Level ****************************
Input: [TheoryLevel = kohn_sham]

Exchange-correlation:
  Exchange
    Slater exchange (LDA)
    [1] P. A. M. Dirac, Math. Proc. Cambridge Philos. Soc. 26, 376 (1930)
    [2] F. Bloch, Z. Phys. 57, 545 (1929)
  Correlation
    Perdew & Zunger (Modified) (LDA)
    [1] J. P. Perdew and A. Zunger, Phys. Rev. B 23, 5048 (1981), modified to improve the matching between the low- and high-rs

Input: [SICCorrection = sic_none]
**********************************************************************


****************************** Hartree *******************************
Input: [DressedOrbitals = no]
The chosen Poisson solver is 'interpolating scaling functions'
**********************************************************************

Input: [FilterPotentials = filter_TS]
Info: Pseudopotential for H
  Radii for localized parts:
    local part     =  1.9 b
    non-local part =  0.0 b
    orbitals       =  8.8 b

Input: [RelativisticCorrection = non_relativistic]
Input: [DFTULevel = dft_u_none]
Input: [MagneticConstrain = 0]

****************** Approximate memory requirements *******************
Mesh
  global  :       0.5 MiB
  local   :       1.2 MiB
  total   :       1.6 MiB

States
  real    :       0.2 MiB (par_kpoints + par_states + par_domains)
  complex :       0.5 MiB (par_kpoints + par_states + par_domains)

**********************************************************************

Info: Generating external potential
      done.
Info: Octopus initialization completed.
Info: Starting calculation mode.
Info: Allocating ground state wave-functions
Info: Blocks of states
      Block       1 contains       1 states:       1 -       1
Info: Ground-state allocation done.

** Warning:
**   Could not find 'restart/gs' directory for restart.
**   No restart information will be read.


** Warning:
**   Unable to read wavefunctions.
**   Starting from scratch!

Input: [MixField = potential] (what to mix during SCF cycles)
Input: [MixingScheme = broyden]
Info: Mixing uses    4 steps and restarts after   20 steps.

**************************** Eigensolver *****************************
Input: [Eigensolver = cg]
Input: [Preconditioner = pre_filter]
Info: Generating weights for finite-difference discretization of Preconditioner
Input: [PreconditionerFilterFactor = 0.5000]
Input: [SubspaceDiagonalization = standard]
**********************************************************************

Input: [EigensolverSkipKpoints = no]
Input: [LCAOStart = lcao_states]
Input: [LCAOScaleFactor = 1.000]
Input: [LCAOMaximumOrbitalRadius = 20.00 b]
Info: Unnormalized total charge =      0.999707
Info: Renormalized total charge =      1.000000
Info: Setting up Hamiltonian.
Info: Performing initial LCAO calculation with      1 orbitals.
Info: Getting Hamiltonian matrix elements.
ETA: .......1......2.......3......4......5.......6......7.......8......9......0

Eigenvalues [H]
 #st  Spin   Eigenvalue      Occupation
   1   --    -0.233499       1.000000
Info: Ground-state restart information will be written to 'restart/gs'.
Info: SCF using real wavefunctions.
Info: Starting SCF iteration.
ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    1 ************************
 etot  = -4.47162815E-01 abs_ev   =  1.12E-03 rel_ev   =  4.78E-03
 ediff =        4.47E-01 abs_dens =  5.51E-03 rel_dens =  5.51E-03
Matrix vector products:      4
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.234620    1.000000   ( 1.0E-02)

Elapsed time for SCF step     1:          0.01
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    2 ************************
 etot  = -4.47913928E-01 abs_ev   =  1.33E-04 rel_ev   =  5.67E-04
 ediff =        7.51E-04 abs_dens =  5.10E-03 rel_dens =  5.10E-03
Matrix vector products:      8
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.234487    1.000000   ( 1.6E-03)

Elapsed time for SCF step     2:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    3 ************************
 etot  = -4.47846438E-01 abs_ev   =  3.20E-04 rel_ev   =  1.36E-03
 ediff =        6.75E-05 abs_dens =  1.61E-03 rel_dens =  1.61E-03
Matrix vector products:      7
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.234168    1.000000   ( 1.9E-04)

Elapsed time for SCF step     3:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    4 ************************
 etot  = -4.46399340E-01 abs_ev   =  1.28E-03 rel_ev   =  5.51E-03
 ediff =        1.45E-03 abs_dens =  1.11E-03 rel_dens =  1.11E-03
Matrix vector products:      7
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.232885    1.000000   ( 1.6E-04)

Elapsed time for SCF step     4:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    5 ************************
 etot  = -4.46409404E-01 abs_ev   =  3.21E-05 rel_ev   =  1.38E-04
 ediff =        1.01E-05 abs_dens =  1.26E-04 rel_dens =  1.26E-04
Matrix vector products:      7
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.232917    1.000000   ( 4.3E-05)

Elapsed time for SCF step     5:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    6 ************************
 etot  = -4.46589950E-01 abs_ev   =  1.62E-04 rel_ev   =  6.97E-04
 ediff =        1.81E-04 abs_dens =  1.18E-04 rel_dens =  1.18E-04
Matrix vector products:      6
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.233080    1.000000   ( 3.5E-05)

Elapsed time for SCF step     6:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    7 ************************
 etot  = -4.46647763E-01 abs_ev   =  4.58E-05 rel_ev   =  1.96E-04
 ediff =        5.78E-05 abs_dens =  7.06E-05 rel_dens =  7.06E-05
Matrix vector products:      8
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.233125    1.000000   ( 1.6E-05)

Elapsed time for SCF step     7:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    8 ************************
 etot  = -4.46634762E-01 abs_ev   =  1.23E-05 rel_ev   =  5.30E-05
 ediff =        1.30E-05 abs_dens =  7.34E-06 rel_dens =  7.34E-06
Matrix vector products:      6
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.233113    1.000000   ( 9.6E-06)

Elapsed time for SCF step     8:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #    9 ************************
 etot  = -4.46624331E-01 abs_ev   =  9.23E-06 rel_ev   =  3.96E-05
 ediff =        1.04E-05 abs_dens =  8.08E-06 rel_dens =  8.08E-06
Matrix vector products:      6
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.233104    1.000000   ( 6.8E-06)

Elapsed time for SCF step     9:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #   10 ************************
 etot  = -4.46629561E-01 abs_ev   =  4.73E-06 rel_ev   =  2.03E-05
 ediff =        5.23E-06 abs_dens =  3.57E-06 rel_dens =  3.57E-06
Matrix vector products:      7
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.233108    1.000000   ( 4.1E-06)

Elapsed time for SCF step    10:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #   11 ************************
 etot  = -4.46629612E-01 abs_ev   =  9.81E-09 rel_ev   =  4.21E-08
 ediff =        5.11E-08 abs_dens =  3.40E-07 rel_dens =  3.40E-07
Matrix vector products:     11
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.233108    1.000000   ( 3.9E-07)

Elapsed time for SCF step    11:          0.02
**********************************************************************

ETA: .......1......2.......3......4......5.......6......7.......8......9......0


*********************** SCF CYCLE ITER #   12 ************************
 etot  = -4.46629384E-01 abs_ev   =  1.83E-07 rel_ev   =  7.84E-07
 ediff =        2.28E-07 abs_dens =  2.71E-07 rel_dens =  2.71E-07
Matrix vector products:      9
Converged eigenvectors:      0

#  State  Eigenvalue [H]  Occupation    Error
      1       -0.233108    1.000000   ( 2.0E-07)

Elapsed time for SCF step    12:          0.03
**********************************************************************


             Info: Writing states. 2023/05/09 at 07:09:09


        Info: Finished writing states. 2023/05/09 at 07:09:09

Info: SCF converged in   12 iterations


** Warning:
**   Some of the states are not fully converged!

Info: Number of matrix-vector products:         86
Info: Finished writing information to 'restart/gs'.

             Calculation ended on 2023/05/09 at 07:09:09

                          Walltime:  00.780s

Octopus emitted 3 warnings.

```