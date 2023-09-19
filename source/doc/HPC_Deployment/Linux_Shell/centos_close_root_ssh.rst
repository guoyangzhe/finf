================================================
CentOS-7 关闭root远程ssh登录
================================================

**在CentOS中，可以通过修改SSH配置文件来关闭root用户的远程SSH登录。以下是具体步骤：**

1. 使用root用户登录到CentOS系统。

2. 打开SSH配置文件 ``/etc/ssh/sshd_config`` ，可以使用 ``vi`` 或 ``nano`` 等编辑器进行编辑：

``vi /etc/ssh/sshd_config``

3. 找到以下行：

``#PermitRootLogin yes``

将其修改为：

``PermitRootLogin no``

这将 ``禁止root用户通过SSH远程登录`` 。

4. 保存并关闭文件。

5. 重新加载SSH配置文件：

``systemctl reload sshd``

6. 确认SSH服务已重新加载：

``systemctl status sshd``

如果服务状态为 ``active（running）`` ，则表示SSH服务已重新加载。

现在， ``root`` 用户将无法通过SSH远程登录到CentOS系统。如果需要进行系统管理操作，可以使用其他普通用户登录，并使用 ``sudo`` 命令获取root权限。