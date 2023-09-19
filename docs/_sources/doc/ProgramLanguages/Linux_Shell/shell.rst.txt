==============
Linux Shell
==============

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
应当掌握的Linux的基础知识-1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. note:: 
    Linux是一种开源的操作系统，它提供了许多强大的shell命令，以下是一些常用的命令：

    1. ls：列出当前目录下的文件和子目录。

    2. cd：切换当前目录。

    3. pwd：显示当前目录的路径。

    4. mkdir：创建一个新目录。

    5. rm：删除文件或目录。

    6. cp：复制文件或目录。

    7. mv：移动文件或目录。

    8. cat：显示文件的内容。

    9. grep：在文件中查找指定的字符串。

    10. find：在文件系统中查找文件。

    11. chmod：修改文件或目录的权限。

    12. chown：修改文件或目录的所有者。

    13. ps：显示当前正在运行的进程。

    14. top：显示系统的资源使用情况。

    15. tar：打包和解压文件。

    这些命令是Linux中最常用的命令之一，掌握它们可以帮助您更好地管理和操作Linux系统。



.. tip::
    - centos删除所有子文件夹下的同一个名称的文件：
        find ./ -type f -name "WAVECAR" -delete


应当掌握的Linux的基础知识-2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    至少会用的命令：
    cd, ls, pwd, vi, gedit, rm, mv, cp, mkdir, yum, cat, grep, head, tail, top, kill, export, reboot, poweroff, which, find, chmod, echo
    最好了解的命令：
    awk, du, df, ssh, time, ln, rpm, man, alias, ps, touch, passwd, tar, more, unset, nohup(jobs), source, nice


.. note::
    应当了解以下概念：
    - Linux的文件路径
    - 操作系统的基本目录结构
    - 相对路径与绝对路径
    - 用户权限
    - `bash`
    - `.bashrc`文件
    - 环境变量（特别是 `PATH` 和 `LD_LIBRARY_PATH` ）
    - `shell` 脚本
    - 重定向（ `>` 、 `<` 、 `<<` 、 `>>` 操作符）
    - 管道命令操作符（ `|` 和 `|tee` 符号）
    - 动态库文件
    - `rpm` 包
    - 前台与后台
    - 进程优先级

    以上知识可以通过在虚拟机中练习和使用 `Google` 搜索来学习。对于在 `Linux` 下运行计算程序而言，这些已经足够了。个人认为，没有必要专门购买Linux书籍去学习。但如果你想深入系统地学习Linux，可以考虑阅读 `《The Linux Command Line》` （William Shotts）或 `《鸟哥的Linux私房菜》` 等书籍。

    我推荐一个网站：[Linux命令大全](https://man.linuxde.net)，你可以在这个网站中找到各种Linux命令，并且有清晰易懂的讲解。


.. note::
    Linux任务管理器：
    - top
    - htop
    - atop
    - btop


.. note::
    - Linux的.bahsrc文件相当重要，不要写入乱七八糟的东西，否则会影响系统的正常运行。同时也会有未知的报错，如不能自动sftp跟踪文件夹当前路径。


.. note::
    - 安装图形界面
        yum grouplist
        yum groupinstall GNOME Desktop
        yum groupinstall Graphical* # 安装图形界面
    - 重启图形界面：
        systemctl restart gdm


.. note::
    - centos 7 查看天气：
        curl wttr.in/dalian