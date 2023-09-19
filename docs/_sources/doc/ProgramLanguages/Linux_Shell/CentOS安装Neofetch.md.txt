# CentOS-7 安装 Neofetch
## 1. 安装 epel-release
`yum install epel-release`
## 2. 添加第三方软件源
`curl -o /etc/yum.repos.d/konimex-neofetch-epel-7.repo https://copr.fedorainfracloud.org/coprs/konimex/neofetch/repo/epel-7/konimex-neofetch-epel-7.repo`
## 3. 安装 neofetch
`yum install neofetch`
## 4. 运行 neofetch
`neofetch`
## 5. 设置 neofetch 开机自启
`echo "neofetch" >> /etc/profile`
## 6. 重启系统
`reboot`
```
## 7. 效果图

```bash
                 ..                    root@node01
               .PLTJ.                  -----------
              <><><><>                 OS: CentOS Linux 7 (Core) x86_64
     KKSSV' 4KKK LJ KKKL.'VSSKK        Host: Super Server 0123456789
     KKV' 4KKKKK LJ KKKKAL 'VKK        Kernel: 3.10.0-1127.el7.x86_64
     V' ' 'VKKKK LJ KKKKV' ' 'V        Uptime: 2 days, 35 mins
     .4MA.' 'VKK LJ KKV' '.4Mb.        Packages: 2468 (rpm)
   . KKKKKA.' 'V LJ V' '.4KKKKK .      Shell: bash 4.2.46
 .4D KKKKKKKA.'' LJ ''.4KKKKKKK FA.    Resolution: 1920x1080
<QDD ++++++++++++  ++++++++++++ GFD>   Theme: Adwaita [GTK2/3]
 'VD KKKKKKKK'.. LJ ..'KKKKKKKK FV     Icons: Adwaita [GTK2/3]
   ' VKKKKK'. .4 LJ K. .'KKKKKV '      CPU: AMD EPYC 7H12 64- (128) @ 2.600GHz
      'VK'. .4KK LJ KKA. .'KV'         GPU: NVIDIA 21:00.0 NVIDIA Corporation Device 1fb2
     A. . .4KKKK LJ KKKKA. . .4        Memory: 176641MiB / 515723MiB
     KKA. 'KKKKK LJ KKKKK' .4KK
     KKSSA. VKKK LJ KKKV .4SSKK
              <><><><>
               'MKKM'
                 ''
```

