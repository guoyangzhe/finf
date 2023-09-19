# FDTD Cluster Usage

* 安装的版本为：Lumerical FDTD 2016a Build 736 Linux64
*Tested on CentOS7 - Linux 3.10.0-1160.92.1.el7.x86_64*

## 1. 安装

* Step 0: uninstall old versions DEVICE, FDTD, INTERCONNECT MODE and Lumerical_FlexLM

* Step 1: unpack and install the programs DEVICE, FDTD, INTERCONNECT
        MODE and Lumerical_FlexLM

* Step 2: Stop service "Lumerical FlexNet License Manager":
        run command from terminal console as root:
        # /etc/init.d/lumladmin stop

* Step 3: Extract all files from archive
        "lumerical.2016a.build.736.linux.x64.patch.tar.gz"
        under programs directory and overwrite.
        Default programs directory is /opt/lumerical

* Step 4: Start service "Lumerical FlexNet License Manager",
        run command from terminal console as root:
        # /etc/init.d/lumladmin start

* Example complete instalation procedure, see file

"lumerical_install_(screen_of_terminal).pdf"

```bash
Tested on CentOS7 - Linux 3.10.0-327.3.1.el7.x86_64
running on:
VMware Workstation 12.0.0 build-2985596
```

![Alt text](../../../../media/fdtd/Lumerical.2016a.build.736_ALL_CentOS7.png)

![Alt text](../../../../media/fdtd/RPM-DEPENDENCIES-rpmreaper_DEVICE.png)

![Alt text](../../../../media/fdtd/RPM-DEPENDENCIES-rpmreaper_FDTD.png)

![Alt text](../../../../media/fdtd/RPM-DEPENDENCIES-rpmreaper_INTERCONNECT.png)

![Alt text](../../../../media/fdtd/RPM-DEPENDENCIES-rpmreaper_MODE.png)

![Alt text](../../../../media/fdtd/RPM-DEPENDENCIES-rpmreaper_lumerical-flexlm.png)

```bash
Using username "root".
root@xxx.xxx.xxx.xxx's password:
Last login: Tue Jan 12 04:19:59 2016 from xxx.xxx.xxx.xxx
[root@localhost ~]# pwd
/root
[root@localhost ~]# cd /home/tester/Downloads/
[root@localhost Downloads]# ls -la
total 1085228
drwxrwxr-x. 2 tester tester 4096 Jan 12 08:34 .
drwx------. 8 tester tester 4096 Jan 12 05:19 ..
-rw-r--r--. 1 root root 173417058 Jan 12 08:31 DEVICE-5.0.736.tar.gz
-rw-r--r--. 1 root root 285134174 Jan 12 08:31 FDTD_Solutions-8.15.736.tar.gz
-rw-r--r--. 1 root root 146006583 Jan 12 08:31 INTERCONNECT-5.5.736.tar.gz
-rw-r--r--. 1 root root 223137242 Jan 12 05:32 lumerical.2016a.build.736.linux.x64.patch.tar.gz
-rw-r--r--. 1 root root 28788198 Jan 12 08:31 Lumerical_FlexLM-1.6.700.tar.gz
-rw-r--r--. 1 root root 254771147 Jan 12 08:31 MODE_Solutions-7.7.736.tar.gz
[root@localhost Downloads]# gunzip DEVICE-5.0.736.tar.gz
[root@localhost Downloads]# tar -xvf DEVICE-5.0.736.tar
./DEVICE-5.0.736/
./DEVICE-5.0.736/license.txt
./DEVICE-5.0.736/rpm_install_files/
./DEVICE-5.0.736/rpm_install_files/DEVICE-5.0.736-1.el5.x86_64.rpm
./DEVICE-5.0.736/install.sh
[root@localhost Downloads]# yum install DEVICE-5.0.736/rpm_install_files/DEVICE-5.0.736-1.el5.x86_64.rpm
Loaded plugins: fastestmirror, langpacks
Examining DEVICE-5.0.736/rpm_install_files/DEVICE-5.0.736-1.el5.x86_64.rpm: DEVICE-5.0.736-1.el5.x86_64
Marking DEVICE-5.0.736/rpm_install_files/DEVICE-5.0.736-1.el5.x86_64.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package DEVICE.x86_64 0:5.0.736-1.el5 will be installed
--> Finished Dependency Resolution
Dependencies Resolved
============================================================================================================================
Package Arch Version Repository Size
============================================================================================================================
Installing:
DEVICE x86_64 5.0.736-1.el5 /DEVICE-5.0.736-1.el5.x86_64 510 M
Transaction Summary
============================================================================================================================
Install 1 Package
Total size: 510 M
Installed size: 510 M
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Installing : DEVICE-5.0.736-1.el5.x86_64 1/1
Verifying : DEVICE-5.0.736-1.el5.x86_64 1/1
Installed:
DEVICE.x86_64 0:5.0.736-1.el5
Complete!
[root@localhost Downloads]# gunzip FDTD_Solutions-8.15.736.tar.gz
[root@localhost Downloads]# tar -xvf FDTD_Solutions-8.15.736.tar
./FDTD_Solutions-8.15.736/
./FDTD_Solutions-8.15.736/license.txt
./FDTD_Solutions-8.15.736/rpm_install_files/
./FDTD_Solutions-8.15.736/rpm_install_files/FDTD-8.15.736-1.el5.x86_64.rpm
./FDTD_Solutions-8.15.736/install.sh
[root@localhost Downloads]# yum install FDTD_Solutions-8.15.736/rpm_install_files/FDTD-8.15.736-1.el5.x86_64.rpm
Loaded plugins: fastestmirror, langpacks
Examining FDTD_Solutions-8.15.736/rpm_install_files/FDTD-8.15.736-1.el5.x86_64.rpm: FDTD-8.15.736-1.el5.x86_64
Marking FDTD_Solutions-8.15.736/rpm_install_files/FDTD-8.15.736-1.el5.x86_64.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package FDTD.x86_64 0:8.15.736-1.el5 will be installed
--> Finished Dependency Resolution
Dependencies Resolved
============================================================================================================================
Package Arch Version Repository Size
============================================================================================================================
Installing:
FDTD x86_64 8.15.736-1.el5 /FDTD-8.15.736-1.el5.x86_64 831 M
Transaction Summary
============================================================================================================================
Install 1 Package
Total size: 831 M
Installed size: 831 M
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Installing : FDTD-8.15.736-1.el5.x86_64 1/1
Verifying : FDTD-8.15.736-1.el5.x86_64 1/1
Installed:
FDTD.x86_64 0:8.15.736-1.el5
Complete!
[root@localhost Downloads]# gunzip INTERCONNECT-5.5.736.tar.gz
[root@localhost Downloads]# tar -xvf INTERCONNECT-5.5.736.tar
./INTERCONNECT-5.5.736/
./INTERCONNECT-5.5.736/license.txt
./INTERCONNECT-5.5.736/rpm_install_files/
1
./INTERCONNECT-5.5.736/rpm_install_files/INTERCONNECT-5.5.736-1.el5.x86_64.rpm
./INTERCONNECT-5.5.736/install.sh
[root@localhost Downloads]# yum install INTERCONNECT-5.5.736/rpm_install_files/INTERCONNECT-5.5.736-1.el5.x86_64.rpm
Loaded plugins: fastestmirror, langpacks
Examining INTERCONNECT-5.5.736/rpm_install_files/INTERCONNECT-5.5.736-1.el5.x86_64.rpm: INTERCONNECT-5.5.736-1.el5.x86_64
Marking INTERCONNECT-5.5.736/rpm_install_files/INTERCONNECT-5.5.736-1.el5.x86_64.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package INTERCONNECT.x86_64 0:5.5.736-1.el5 will be installed
--> Finished Dependency Resolution
Dependencies Resolved
============================================================================================================================
Package Arch Version Repository Size
============================================================================================================================
Installing:
INTERCONNECT x86_64 5.5.736-1.el5 /INTERCONNECT-5.5.736-1.el5.x86_64 431 M
Transaction Summary
============================================================================================================================
Install 1 Package
Total size: 431 M
Installed size: 431 M
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Installing : INTERCONNECT-5.5.736-1.el5.x86_64 1/1
Verifying : INTERCONNECT-5.5.736-1.el5.x86_64 1/1
Installed:
INTERCONNECT.x86_64 0:5.5.736-1.el5
Complete!
[root@localhost Downloads]# gunzip MODE_Solutions-7.7.736.tar.gz
[root@localhost Downloads]# tar -xvf MODE_Solutions-7.7.736.tar
./MODE_Solutions-7.7.736/
./MODE_Solutions-7.7.736/license.txt
./MODE_Solutions-7.7.736/rpm_install_files/
./MODE_Solutions-7.7.736/rpm_install_files/MODE-7.7.736-1.el5.x86_64.rpm
./MODE_Solutions-7.7.736/install.sh
[root@localhost Downloads]# yum install MODE_Solutions-7.7.736/rpm_install_files/MODE-7.7.736-1.el5.x86_64.rpm
Loaded plugins: fastestmirror, langpacks
Examining MODE_Solutions-7.7.736/rpm_install_files/MODE-7.7.736-1.el5.x86_64.rpm: MODE-7.7.736-1.el5.x86_64
Marking MODE_Solutions-7.7.736/rpm_install_files/MODE-7.7.736-1.el5.x86_64.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package MODE.x86_64 0:7.7.736-1.el5 will be installed
--> Finished Dependency Resolution
Dependencies Resolved
============================================================================================================================
Package Arch Version Repository Size
============================================================================================================================
Installing:
MODE x86_64 7.7.736-1.el5 /MODE-7.7.736-1.el5.x86_64 731 M
Transaction Summary
============================================================================================================================
Install 1 Package
Total size: 731 M
Installed size: 731 M
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Installing : MODE-7.7.736-1.el5.x86_64 1/1
Verifying : MODE-7.7.736-1.el5.x86_64 1/1
Installed:
MODE.x86_64 0:7.7.736-1.el5
Complete!
[root@localhost Downloads]# gunzip Lumerical_FlexLM-1.6.700.tar.gz
[root@localhost Downloads]# tar -xvf Lumerical_FlexLM-1.6.700.tar
Lumerical_FlexLM-1.6.700/
Lumerical_FlexLM-1.6.700/lumerical-flexlm-1.6.700-1.x86_64.rpm
Lumerical_FlexLM-1.6.700/aksusbd-2.2-1.i386.rpm
Lumerical_FlexLM-1.6.700/install.sh
[root@localhost Downloads]# yum install Lumerical_FlexLM-1.6.700/lumerical-flexlm-1.6.700-1.x86_64.rpm
Loaded plugins: fastestmirror, langpacks
Examining Lumerical_FlexLM-1.6.700/lumerical-flexlm-1.6.700-1.x86_64.rpm: lumerical-flexlm-1.6.700-1.x86_64
Marking Lumerical_FlexLM-1.6.700/lumerical-flexlm-1.6.700-1.x86_64.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package lumerical-flexlm.x86_64 0:1.6.700-1 will be installed
--> Finished Dependency Resolution
Dependencies Resolved
============================================================================================================================
Package Arch Version Repository Size
============================================================================================================================
Installing:
lumerical-flexlm x86_64 1.6.700-1 /lumerical-flexlm-1.6.700-1.x86_64 74 M
Transaction Summary
============================================================================================================================
Install 1 Package
2
Total size: 74 M
Installed size: 74 M
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Installing : lumerical-flexlm-1.6.700-1.x86_64 1/1
Installing licensing service from /opt/lumerical/lumerical-flexlm/FNPLicensingService to /usr/local/share/FNP/service64/11.12.1
Checking system for trusted storage area...
Configuring for Linux, Trusted Storage path /usr/local/share/macrovision/storage...
Creating /usr/local/share/macrovision/storage...
Setting permissions on /usr/local/share/macrovision/storage...
Permissions set...
Checking system for Replicated Anchor area...
Configuring Replicated Anchor area...
Replicated Anchor area already exists...
Setting permissions on Replicated Anchor area...
Replicated Anchor area permissions set...
Configuring Temporary area...
Temporary area already exists...
Setting permissions on Temporary area...
Temporary area permissions set...
Setting FUSE configuration
Configuration completed successfully.
Starting License Manager Daemon:
Verifying : lumerical-flexlm-1.6.700-1.x86_64 1/1
Installed:
lumerical-flexlm.x86_64 0:1.6.700-1
Complete!
[root@localhost Downloads]# rm /etc/init.d/lumlmadmin
rm: remove symbolic link ‘/etc/init.d/lumlmadmin’? y
[root@localhost Downloads]# cp /opt/lumerical/lumerical-flexlm/etc/lumlmadmin /etc/init.d/
[root@localhost Downloads]# chkconfig lumlmadmin on
[root@localhost Downloads]# /etc/init.d/lumlmadmin stop
Shutting down License Manager Daemon: [ OK ]
[root@localhost Downloads]# gunzip lumerical.2016a.build.736.linux.x64.patch.tar.gz
[root@localhost Downloads]# tar -xvf lumerical.2016a.build.736.linux.x64.patch.tar -C /
opt/lumerical/fdtd/bin/fdtd-engine-hpmpi-lcl
opt/lumerical/fdtd/bin/fdtd-engine-hpmpi-lcl.locale.xml
opt/lumerical/fdtd/bin/fdtd-engine-impi-lcl
opt/lumerical/fdtd/bin/fdtd-engine-impi-lcl.locale.xml
opt/lumerical/fdtd/bin/fdtd-engine-mpich2-lcl
opt/lumerical/fdtd/bin/fdtd-engine-mpich2-lcl.locale.xml
opt/lumerical/fdtd/bin/fdtd-engine-mpich2nem
opt/lumerical/fdtd/bin/fdtd-engine-mpich2nem.locale.xml
opt/lumerical/fdtd/bin/fdtd-engine-mpichgm
opt/lumerical/fdtd/bin/fdtd-engine-mpichgm.locale.xml
opt/lumerical/fdtd/bin/fdtd-engine-mpichp4
opt/lumerical/fdtd/bin/fdtd-engine-mpichp4-lcl
opt/lumerical/fdtd/bin/fdtd-engine-mpichp4-lcl.locale.xml
opt/lumerical/fdtd/bin/fdtd-engine-mpichp4.locale.xml
opt/lumerical/fdtd/bin/fdtd-engine-mpichshmem
opt/lumerical/fdtd/bin/fdtd-engine-mpichshmem.locale.xml
opt/lumerical/fdtd/bin/fdtd-engine-ompi-lcl
opt/lumerical/fdtd/bin/fdtd-engine-ompi-lcl.locale.xml
opt/lumerical/fdtd/bin/fdtd-solutions
opt/lumerical/fdtd/bin/fdtd-solutions.locale.xml
opt/lumerical/device/bin/device
opt/lumerical/device/bin/device.locale.xml
opt/lumerical/device/bin/device-engine-mpich2nem
opt/lumerical/device/bin/device-engine-mpich2nem.locale.xml
opt/lumerical/device/bin/thermal-engine-mpich2nem
opt/lumerical/device/bin/thermal-engine-mpich2nem.locale.xml
opt/lumerical/mode/bin/eme-engine
opt/lumerical/mode/bin/eme-engine.locale.xml
opt/lumerical/mode/bin/fd-engine
opt/lumerical/mode/bin/fd-engine.locale.xml
opt/lumerical/mode/bin/mode-solutions
opt/lumerical/mode/bin/mode-solutions.locale.xml
opt/lumerical/mode/bin/varfdtd-engine-hpmpi
opt/lumerical/mode/bin/varfdtd-engine-hpmpi.locale.xml
opt/lumerical/mode/bin/varfdtd-engine-impi
opt/lumerical/mode/bin/varfdtd-engine-impi.locale.xml
opt/lumerical/mode/bin/varfdtd-engine-mpich2nem
opt/lumerical/mode/bin/varfdtd-engine-mpich2nem.locale.xml
opt/lumerical/mode/bin/varfdtd-engine-mpichgm
opt/lumerical/mode/bin/varfdtd-engine-mpichgm.locale.xml
opt/lumerical/mode/bin/varfdtd-engine-mpichp4
opt/lumerical/mode/bin/varfdtd-engine-mpichp4.locale.xml
opt/lumerical/mode/bin/varfdtd-engine-mpichshmem
opt/lumerical/mode/bin/varfdtd-engine-mpichshmem.locale.xml
opt/lumerical/mode/bin/varfdtd-engine-ompi
opt/lumerical/mode/bin/varfdtd-engine-ompi.locale.xml
opt/lumerical/interconnect/bin/interconnect
opt/lumerical/interconnect/bin/interconnect.locale.xml
opt/lumerical/lumerical-flexlm/licenses/LUMERICL/start.lic
opt/lumerical/lumerical-flexlm/LUMERICL
[root@localhost Downloads]# /etc/init.d/lumlmadmin start
Starting License Manager Daemon:
[root@localhost Downloads]#
3
```
