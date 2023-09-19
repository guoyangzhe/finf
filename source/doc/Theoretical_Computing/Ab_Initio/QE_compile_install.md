# Quantum Espresso编译与安装

* 关于编译的细节可以看QE的手册 <https://www.quantum-espresso.org/Doc/user_guide/node10.html>

* 在CentOS下使用yum也可以不通过编译来安装，但有一些弊端，见此文第6节。

## 1. 安装依赖

### 1.1. 安装OpenMPI

```bash
#去https://www.open-mpi.org下载最新的OpenMPI包，解压后进入此目录，运行以下命令将之编译并安装到指定目录下。
./configure --prefix=/opt/libraries/gnu8-openmpi/4.1.1 --enable-mpi-cxx --enable-mpi-fortran --enable-shared
make all install
#新建一个文件，名为~/run_software_bashrc/before_run_qe7.2.sh，内容如下：
#openmpi-4.1.1#
export MPI_HOME=/opt/libraries/gnu8-openmpi/4.1.1 && \
export PATH=$MPI_HOME/bin:$PATH && \
export LD_LIBRARY_PATH=$MPI_HOME/lib:$LD_LIBRARY_PATH && \
export INCLUDE=$MPI_HOME/include:$INCLUDE && \
export MANPATH=$MPI_HOME/share/man:$MANPATH
#然后重新打开终端，以上设置就生效了。可以运行mpiexec -V，如果正常显示出了OpenMPI的版本，说明已经装好了。之后可以删掉OpenMPI压缩包和解压出的目录。
```

* 注：如果机子里之前还有其它MPI库，应当运行which mpiexec来看看是否确实指向的是新装的OpenMPI，如果指向的是其它的，则并行运行可能失败。比如如果你之前在机子里装过Intel编译器的时候顺带装了Intel MPI，则应当在编译QE以及运行QE前将~/.bashrc里的相应配置语句注释掉后重新进入终端，免得被利用的是Intel MPI而非新装的OpenMPI。

### 1.2. 安装Intel MKL

* 安装请查看`VASP编译与安装`或`配置HPC`中的Intel MKL安装部分。

* 环境变量如下：

```bash
#intel#
source /opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/mkl/bin/mklvars.sh intel64
```

## 2. 编译Quantum Espresso

```bash
#去http://www.quantum-espresso.org/download下载最新的Quantum Espresso包，解压后进入此目录，运行以下命令将之编译并安装到指定目录下。这里-enable-openmp使得QE也可以利用OpenMP来并行，如果不打算以OpenMP并行的话就不写这个。
./configure --prefix=/opt/apps/qe-6.5 -enable-openmp
make all install -j # 若出错，去掉-j选项再试试。
# 四核机子上经过几分钟编译完毕，可执行文件都被装到了/opt/apps/qe-6.5/bin目录下。解压出的目录和压缩包此时虽然可以删掉，但建议还是留着解压出的目录，里面有些文件以后还用得着。
# 注：QE在编译过程默认调用gfortran、gcc和mpif90。如果想改默认的编译器，应对QE目录下的make.inc文件里的编译器设置进行修改，而且在之前编译OpenMPI的时候也用相应的编译器。
```

* 在~/.bashrc里添加以下内容：

```bash
#qe72#
export PATH=$PATH:/opt/apps/qe-6.5/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/mkl/lib/intel64_lin
# 这里往LD_LIBRARY_PATH环境变量添加的Intel MKL库的目录名应当与你当前机子里的实际路径一致。
```

* 之后重新进入终端，QE的可执行文件就可以在任意目录下直接运行了。

* 以上述方式编译出来的QE没有包含EPW、PLUMED、Wannier90、WanT、YAMBO、GIPAW程序，如果需要编译的话，看官网上User's Guide for Quantum ESPRESSO文档的2.5节。

* 可选：可将最终的环境变量写入一个文件中(run_qe-6.5.sh)

```bash
#openmpi-4.1.1#
export PATH=$PATH:/opt/libraries/gnu8-openmpi/4.1.1/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/libraries/gnu8-openmpi/4.1.1/lib
#qe72#
export PATH=$PATH:/opt/apps/qe-6.5/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/intel/intel-2019up5/compilers_and_libraries_2019.5.281/linux/mkl/lib/intel64_lin
```

## 3. 测试

* 进入QE的安装目录，运行以下命令：

```bash
#测试#
# 下载测试文件
export OMP_NUM_THREADS=1
mpirun -np 4 pw.x < si.scf.in > si.scf.out
# 如果任务能正常完成，末尾显示JOB DONE，就说明已经装好了。注：如果不设置OMP_NUM_THREADS环境变量的话，机子有多少核，OpenMP就会用多少个线程。
```

* 也可以使用QE自带的测试集进行测试。做法是进入QE解压后的目录的test-suite子目录，在里面运行make run-tests-parallel命令，就会在并行运算下对所有任务进行测试，每一项对应的含义见此目录下的README。如果只想测试比如PWscf模块，则运行make run-tests-pw-parallel。

## 4. QE的输入文件

* QE的输入文件格式是自由格式，可以用任意编辑器编辑，但是必须以.in为后缀名。输入文件的内容可以参考QE的手册，或者在安装目录下的examples目录里找到相应的示例文件。

## 5. QE的输出文件

* QE的输出文件格式是自由格式，可以用任意编辑器编辑，但是必须以.out为后缀名。输出文件的内容可以参考QE的手册，或者在安装目录下的examples目录里找到相应的示例文件。

## 6. CentOS使用yum安装Quantum Espresso

```bash
#安装Quantum Espresso
yum install -y quantum-espresso
#安装Quantum Espresso的文档
yum install -y quantum-espresso-doc
#安装Quantum Espresso的示例
yum install -y quantum-espresso-examples
```

## 7. Ubuntu使用apt安装Quantum Espresso

```bash
#安装Quantum Espresso
apt install -y quantum-espresso
#安装Quantum Espresso的文档
apt install -y quantum-espresso-doc
#安装Quantum Espresso的示例
apt install -y quantum-espresso-examples
```
