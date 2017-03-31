#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

## python 提供StringIO 来缓存数据到内存中, 对用户来说 可以把StringIO对象当作真是存在的 文件使用

from io import StringIO

si = StringIO()
si.write('写入StringIo内容')

## 使用getValue()函数获取已经写入到StringIO对象的字符

print(si.getvalue())
si.write('add content.')

print(si.getvalue())

## 也可以像读取文件一样 读

ss = StringIO('Hello!\nHi!\nBye~\n')

while True:
    s = ss.readline()
    if s == '':
        break
    print(s.strip()) ## 去\n
