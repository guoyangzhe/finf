# Linux 选择性文件复制

## 1. 问题描述

在Linux系统中，有时候需要将某个目录下的所有文件复制到另一个目录，但是又不想复制某些文件，比如不想复制隐藏文件，或者不想复制某些特定后缀的文件，这时候就需要用到Linux的选择性文件复制功能。

## 2. 解决方案

### 2.1. 复制所有文件，但不包括隐藏文件

```shell
cp -r /source/* /target
```

### 2.2. 复制所有文件，但不包括隐藏文件和指定后缀的文件

```shell
cp -r /source/*!(.txt|.doc) /target
```

### 2.3. 复制所有文件，但不包括隐藏文件和指定文件

```shell
cp -r /source/*!(.txt|file1) /target
```

### 2.4. 复制所有文件，但不包括隐藏文件和指定文件夹

```shell
cp -r /source/*!(.txt|dir1) /target
```

### 2.5. 复制所有文件，但不包括隐藏文件和指定文件夹下的所有文件

```shell
cp -r /source/*!(.txt|dir1/*) /target
```

### 2.6. 复制所有文件，但不包括隐藏文件和指定文件夹下的所有文件夹

```shell
cp -r /source/*!(.txt|dir1/*/) /target
```

### 2.7. 复制所有文件，但不包括隐藏文件和指定文件夹下的所有文件和文件夹

```shell
cp -r /source/*!(.txt|dir1/*|dir1/*/) /target
```

## 3. 复制文件夹下所有文件并排除特定大小的文件

```shell
find /source -type f -size +100M -exec cp {} /target \;
# 例如：
find ./ -type f -size -500M -exec cp -rf --parents {} /mnt/hybrid/ \;
# 该命令是找到小于500MB的文件，并强制复制到目标目录，复制时创建原文件的层级关系（保留文件夹的复制，若不加--parents会导致没有文件目录）
```
