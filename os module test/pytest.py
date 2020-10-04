"""
功能: 目录拷贝（递归实现）
如果目录1的文件目录2已经有了，就不覆盖
"""

import os, shutil

# 获取 输入 src 和 des（des如果不存在则创建）

def copydir(src, des):
    if not os.path.exists(des):  # 如不存在目标目录则创建
        os.makedirs(des)
    files = os.listdir(src)  # 获取文件夹中文件和目录列表
    for f in files:
        if os.path.isdir(src + '/' + f):  # 判断是否是文件夹
            copydir(src + '/' + f, des + '/' + f)  # 递归调用本函数
        else:
            shutil.copy(src + '/' + f, des + '/' + f)  # 拷贝文件

if __name__ == '__main__':
    src = "E:\Program File\py test\os module test\dir1"
    des = "E:\Program File\py test\os module test\dir2"
    copydir(src, des)
