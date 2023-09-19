============================================
CentOS-7 集群上创建用户
============================================
.. tip::
    1. ``useradd  host``
    2. ``passwd host``
    3. ``su host``
    4. ``ssh-keygen``
    5. ``cd  /home/host/.ssh/``
    6. ``cat  id_rsa.pub > authorized_keys``
    7. ``chmod 600 authorized_keys`` 
    8. ``su root``
    9. ``cd  /var/yp/``
    10. ``make``  