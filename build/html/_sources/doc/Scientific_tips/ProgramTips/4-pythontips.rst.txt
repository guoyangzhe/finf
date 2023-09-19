===============
Python tips
===============

.. note:: 
    1. 用 ``with`` 来打开文件，而不是用 ``open`` ，因为 ``with`` 可以自动关闭文件
    2. 用 ``enumerate`` 来遍历一个 ``list`` ，而不是用 ``range(len(list))`` 
    3. 用 ``isinstance`` 来判断变量的类型，而不是用 ``type`` ，因为 ``isinstance`` 可以判断子类
    4. 用 ``__init__`` 来初始化类的属性，而不是在类的外面初始化
    5. 用 ``__repr__`` 来代替 ``__str__`` ，因为 ``__str__`` 会在 ``print`` 的时候调用，而 ``__repr__`` 会在交互式环境下调用
    6. 用 ``__slots__`` 来限制类的属性，可以节省内存，提高速度
    7. 用 ``is`` 来判断两个变量是否是同一个对象，而不是用 ``==`` ，因为 ``==`` 会调用 ``__eq__`` 方法，而 ``is`` 不会
    8. 用 ``numpy`` 的 ``array`` 来存储数据，而不是 ``list`` 

.. note::
    1. VS Code中，用 ``ctrl+shift+p`` 打开命令面板，输入 ``python:select interpreter`` 来选择python解释器
    2. VS Code 中多行缩进快捷键： ``ctrl+[`和`ctrl+]``
    3. VS Code 中多行注释快捷键： ``ctrl+k ctrl+c`和`ctrl+k ctrl+u``

