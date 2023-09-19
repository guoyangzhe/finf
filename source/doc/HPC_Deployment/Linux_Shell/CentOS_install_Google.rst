====================================================
CentOS-7 Google-Chrome 安装
====================================================

* 谷歌浏览器是一款开源好用的浏览器，在CentOS桌面版上使用，可以增强用户体验。打开控制台，输入如下命令：

``cd /``

``cd etc/yum.repos.d``

``sudo vim google-chrome.repo``

编辑输入如下内容：

``[google-chrome]``

``name=google-chrome``

``baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch``

``enabled=1``

``gpgcheck=1``

``gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub``


然后 ``:wq`` 保存。最后安装，输入如下bash。

``sudo yum -y install google-chrome-stable --nogpgcheck``