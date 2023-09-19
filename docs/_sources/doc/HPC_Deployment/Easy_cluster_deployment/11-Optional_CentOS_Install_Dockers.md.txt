# CentOS-7安装Dockers

## 1.安装docker

    ```bash
    yum install -y yum-utils device-mapper-persistent-data lvm2
    ```

## 2.设置yum源

    ```bash
    yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    ```

## 3.查看可用版本

    ```bash
    yum list docker-ce --showduplicates | sort -r
    ```

## 4.安装docker

    ```bash
    yum -y install docker-ce-18.03.1.ce
    ```

## 5.启动docker并设置开机自启

    ```bash
    systemctl start docker
    systemctl enable docker
    ```

## 6.安装docker-compose

    ```bash
    yum install -y epel-release
    yum install -y python-pip
    pip install docker-compose
    ```

## 7.安装docker-machine

    ```bash
    base=
    curl -L
    ```

## 8. 之前的安装方法

    ```bash
    yum remove docker  docker-common docker-selinux docker-engine  # 卸载旧版本
    yum install -y yum-utils device-mapper-persistent-data lvm2  # 安装需要的软件包， yum-util 提供yum-config-manager功能，另两个是devicemapper驱动依赖
    # 设置一个yum源，下面两个都可用
    yum-config-manager --add-repo http://download.docker.com/linux/centos/docker-ce.repo # （中央仓库）

    yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo # （阿里仓库）

    yum list docker-ce --showduplicates | sort -r # 查看可用版本

    yum -y install docker-ce-18.03.1.ce # 选择一个版本并安装
    # 可能会出现错误，需安装：
    yum erase podman buildah
    sudo dnf install container-selinux

    # 启动 Docker 并设置开机自启
    systemctl start docker
    systemctl enable docker
    ```
