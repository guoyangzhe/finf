# 设置自定义yum源

* 可以将生成的RPM通过NFS服务共享或直接复制到各节点，然后执行 `yum localinstall 包文件名` 命令安装，或采用下面建立YUM软件仓库后直接用包名方式安装。

## 1. reposync

* 该命令很强大，可以将远端`yum`仓库里面的包全部下载到本地。这样构建自己的`yum`仓库，就不会遇到网络经常更新包而头痛的事情了。 该命令也是来自与`yum-utils`里面。

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

## 2. 建立YUM仓库目录

* 进入之前下载好的本地仓库目录，执行命令：

    ```bash
    cd /opt/local_epel
    ```

* 建立YUM仓库RPM文件索引：

    ```bash
    createrepo .
    ```

    产生一个 `repodata` 目录，里面有 `repomd.xml` 文件。

* 生成`repo`配置文件，执行命令：

    ```bash
    cat >/etc/yum.repos.d/local_epel.repo<<EOF
    [local_epel]
    name=local_epel
    baseurl=file:///opt/local_epel
    gpgcheck=0
    enable=1
    EOF
    # 其中，name是安装源的名称，baseurl是下载的包所在的目录路径，enabled设置为1表示启用该安装源，gpgcheck设置为0表示不进行GPG验证。
    ```

1. 运行以下命令来清除yum缓存：

    ```bash
    yum clean all
    ```

2. 运行以下命令来更新yum缓存并安装软件包：

    ```bash
    yum makecache
    yum update
    yum install <package-name>
    ```

* 其中，`<package-name>`是您想要安装的软件包名称。

* 通过以上步骤，您就可以成功创建一个本地的yum安装源并安装下载的软件包了。

## 2. 为其它节点设置YUM仓库

* 将上述 `/etc/yum.repos.d/local_epel.repo` 文件复制到所有需安装的子节点 `/etc/yum.repos.d/` 目录下，执行命令：（需要在计算节点上安装`pdsh`）

    ```bash
    pdcp -w node[01-05] /etc/yum.repos.d/local_epel.repo /etc/yum.repos.d/
    # pdcp：是Parallel Distributed Shell (pdsh)的一个命令，用于在多个节点上执行并行的命令或复制文件。
    # -w node[1-10],login：指定要执行命令或复制文件的节点列表。node[1-10]表示节点名为node1、node2、...、node10的节点，login表示登录节点。
    # /etc/yum.repos.d/slurm.repo：要复制的源文件路径。
    # /etc/yum.repos.d/：目标目录路径，即要将源文件复制到的目录。
    ```

* 最后执行命令：

    ```bash
    pdsh -w node[01-05] yum clean all
    pdsh -w node[01-05] yum makecache
    ```

注：
*服务节点、计算节点等注意变化*
*操作前请确认NFS服务是正常的*
