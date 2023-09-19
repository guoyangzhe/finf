======================================
Linux-删除目录下所有同名文件
======================================

* centos删除所有文件夹下的同一个名称的文件：

.. code-block:: sh
    :name: centos删除所有文件夹下的同一个名称的文件
    :emphasize-lines: 2
    :linenos:

    find ./ -type f -name "filename" -delete
    #filename为要删除的文件名
