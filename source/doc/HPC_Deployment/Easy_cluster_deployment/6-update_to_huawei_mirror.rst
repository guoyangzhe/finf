===========================================================
CentOS-7 更新软件源
===========================================================

.. tip::
    CentOS的镜像地址为： ``https://repo.huaweicloud.com/centos/`` 

    1. 备份配置文件

    ``cp -a /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak``

    2. 配置下列方案

        下载新的 ``CentOS-Base.repo`` 文件到 ``/etc/yum.repos.d/`` 目录下，选择 ``CentOS`` 版本：

    ``CentOS 7``

        执行如下命令

    ``wget -O /etc/yum.repos.d/CentOS-Base.repo https://repo.huaweicloud.com/repository/conf/CentOS-7-reg.repo``

    3. 执行 ``yum clean all`` 清除原有 ``yum`` 缓存。

    4. 执行 ``yum makecache`` （刷新缓存）或者 ``yum repolist all`` （查看所有配置可以使用的文件，会自动刷新缓存）。

    ※ 提醒: ``CentOS 8`` 和 ``CentOS 6`` 及以下版本已被官网源下线, 若需使用, 请参考 ``CentOS-Vault`` 进行配置.