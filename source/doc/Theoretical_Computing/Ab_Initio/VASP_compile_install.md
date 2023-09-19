# VASP编译与安装

## 1. 安装Intel依赖库
* 安装步骤略，可在任意网站搜索到，之后需要将intel加入到环境变量中，如下：
```bash
nano ~/.bashrc
```
填入以下内容：
```bash
source /opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mkl/bin/mklvars.sh intel64 && \
source /opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/bin/ifortvars.sh intel64 && \
source /opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/bin/iccvars.sh intel64 && \
source /opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mpi/intel64/bin/mpivars.sh intel64
```
* 保存退出后，执行以下命令使环境变量生效：
```bash
source ~/.bashrc
```
* 然后进入/opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mkl/interfaces/fftw3xf，运行make libintel64命令，过一会儿当前目录下会产生libfftw3xf_intel.a库文件。

## 2. 编译 VASP
* 首先准备安装包，下载地址：https://www.vasp.at/index.php/download （地址不对，商业软件请尊重版权）
* 解压安装包：
```bash
tar -xvf vasp.6.1.0.tar.gz
```
* 进入解压后的文件夹:
```bash
cd vasp.6.1.0
```
* 执行：
```bash
cp arch/makefile.include.linux_intel ./makefile.include
```
* 打开此文件，把其中的OFLAG参数里加入-xhost，这样编译器会使得编译出的程序能够利用当前机子CPU能支持的最高档次的指令集以加速计算，也因此就没必要手动添加其它一些VASP编译教程里诸如-xAVX、-mSSE4.2之类的选项了。
* 可选操作：修改makefile文件，将其中的
```makefile
#FFTW_INC = -I$(MKLROOT)/include
#FFTW_LIB = -L$(MKLROOT)/lib/intel64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core
```
改为
```makefile
FFTW_INC = -I/opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mkl/interfaces/fftw3xf
FFTW_LIB = -L/opt/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mkl/interfaces/fftw3xf -lfftw3xf_intel
```
* 注意:
    如果你的机器以及以后的计算不涉及GPU加速，则将makefile.include文件开头修改为：
```makefile
VERSIONS = std gam ncl
#VERSIONS = std gam ncl gpu gpu_ncl
```
打开makefile.include文件，将其中的
```makefile
OFLAG      = -O2
```
改为：
```makefile
OFLAG      = -O2 -xhost
```

* 然后开始编译：
```bash
make all #约半小时
```
* 编译成功后会在当前目录的`bin`目录下生成vasp_std等文件
* 最后在~/.bashrc文件中添加以下内容：
```bash
nano ~/.bashrc
```
```bash
export VASP_HOME=/opt/apps/vasp.6.1.0 && \
export PATH=$VASP_HOME/bin:$PATH
```
* 保存退出后，执行以下命令使环境变量生效：
```bash
source ~/.bashrc
```
* 注意:
    可以在~/.bashrc文件中添加以下内容，使得每次使用`vasp`命令即可替代`vasp_std`：
```bash
alias vasp='/opt/apps/vasp.6.1.0/bin/vasp_std' 
```


注意事项：
在AMD的机子上使用Intel 2020编译器编译VASP时，会出现错误。尽量使用其他版本的编译器。
