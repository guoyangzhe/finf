<!-- TOC -->

- [Linux-yum只下载不安装](#linux-yum只下载不安装)
  - [通过yum命令只下载rpm包不安装](#通过yum命令只下载rpm包不安装)
    - [1. yumdownloader](#1-yumdownloader)
    - [2. yum --downloadonly](#2-yum---downloadonly)
    - [3. reposync](#3-reposync)

<!-- /TOC -->
# Linux-yum只下载不安装
## 通过yum命令只下载rpm包不安装
### 1. yumdownloader
* 如果只想通过`yum`下载软件的软件包, 但是不需要进行安装的话, 可以使用`yumdownloader`命令; `yumdownloader`命令在软件包`yum-utils`里面. 
```bash
yum install yum-utils -y
```
* 常用参数说明：
```bash
--destdir 指定下载的软件包存放路径
--resolve 解决依赖关系并下载所需的包
```
* 示例：
```bash
yumdownloader --destdir=/tmp --resolve httpd
```
* 通过`yumdownloader`下载的软件包, 会自动解决依赖关系, 并且下载所需的包, 但是不会安装.
### 2. yum --downloadonly
* yum命令的参数有很多，其中就有只是下载而不需要安装的命令，并且也会自动解决依赖；通常和 `--downloaddir` 参数一起使用。
* 示例：
```bash
yum install --downloadonly --downloaddir=/tmp/ vsftpd
yum reinstall --downloadonly --downloaddir=/tmp/ vsftpd
```
* 说明：如果该服务器已经安装了需要下载的软件包，那么使用`install`下载就不行，可以使用`reinstall`下载。 放心（不会真的安装和重新安装，因为后面加了 `--downloadonly`，表明只是下载。
* 如果提示没有`--downloadonly`选项则需要安装`yum-plugin-downloadonly`软件包；
```bash
yum install yum-plugin-downloadonly -y
```
### 3. reposync
* 该命令更加强大，可以将远端`yum`仓库里面的包全部下载到本地。这样构建自己的`yum`仓库，就不会遇到网络经常更新包而头痛的事情了。 该命令也是来自与`yum-utils`里面。
* 示例：
```bash
yum install yum-utils -y
```
* 常用参数说明：
```bash
-r    指定已经本地已经配置的 yum 仓库的 repo源的名称。
-p    指定下载的路径
-m    指定下载的包的架构
```
* 示例：
```bash
reposync -r epel -p /opt/local_epel -m x86_64
```
* 下载以后可以创建为本地软件源：
1. 创建一个新的yum安装源文件，例如：
    ```bash
    sudo vi /etc/yum.repos.d/local_epel.repo
    ```
2. 在文件中添加以下内容：
    ```bash
    [local_epel]
    name=Local EPEL Repository
    baseurl=file:///opt/local_epel
    enabled=1
    gpgcheck=0
    # 其中，name是安装源的名称，baseurl是下载的包所在的目录路径，enabled设置为1表示启用该安装源，gpgcheck设置为0表示不进行GPG验证。
    ```
3. 保存并退出文件。
4. 运行以下命令来清除yum缓存：
    ```bash
    sudo yum clean all
    ```
5. 运行以下命令来更新yum缓存并安装软件包：
    ```bash
    sudo yum update
    sudo yum install <package-name>
    ```
* 其中，`<package-name>`是您想要安装的软件包名称。

* 通过以上步骤，您就可以成功创建一个本地的yum安装源并安装下载的软件包了。