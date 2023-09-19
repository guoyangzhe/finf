===================================
ImageJ批量转化raw文件为bmp文件
===================================

1. 用 ``ImageJ`` 打开 ``raw`` 文件

    * ``File`` -> ``Import`` -> ``Raw...``
    * 选择一个文件然后点击 ``Open`` ，弹出 ``Raw Options`` 对话框，设置参数:
    * ``Image Type`` :  ``16-bit Signed``
    * ``Width`` :  ``160``
    * ``Height`` : ``160``
    * ``Offset to first image`` : ``14``
    * ``Number of images`` : ``1``
    * ``Gap between images`` : ``0``
    * ``White is zero`` : 选中
    * ``Little-endian byte order`` : 选中
    * ``Open all files in folder`` : 选中
    * ``Use virtual stack`` : 选中
    * 然后点击 ``OK`` 。

2. 转化为 ``bmp`` 文件

    * ``File`` -> ``Save As`` -> ``Image Sequence...``
    * 弹出 ``Save as Image Sequence`` 对话框，设置参数:
    * ``Dir`` : 选择保存的目录
    * ``Format`` : 选择 ``BMP`` 
    * ``Name`` : 选择文件名(文件名的头部，如 ``test`` ，则保存的文件名为 ``test0001.bmp`` )
    * ``Start At`` : ``1``
    * ``Digits(1-8)`` : ``4``
    * ``Use slice label as file names`` : 选中
    * 然后点击 ``OK`` 。
