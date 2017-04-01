#!/usr/bin/env python3
# -*- encoding:utf-8 -*-


## python os模块提供了对系统文件和目录的操作
import os

## 获取操作系统的详细信息
print(os.uname())  ## 这个函数只有类linux unix 才有 win没有
# posix.uname_result(sysname='Linux', nodename='arch', release='4.10.6-1-ARCH', version='#1 SMP PREEMPT Mon Mar 27 08:28:22 CEST 2017', machine='x86_64')


## 获取系统环境变量
print(os.environ)

## 获取某一个环境变量的值
print('\n',os.environ.get('JRE_HOME'))  # /home/palm/myapps/java/jdk-7u79-linux-x64/jdk1.7.0_79/jre


##查看当前目录的绝对路径
print('\n',os.path.abspath('.')) #/home/palm/myapps/python-learn/test-all


## 在某一个路径下创建一个目录
## 首先获取新目录的全路径
apath = os.path.join('.','testdir')
## 然后创建这个目录
## 如果存在则会报错
# os.mkdir(apath)  ## FileExistsError: [Errno 17] File exists: './testdir'

## 删掉一个目录 如果不存在则会报错   FileNotFoundError: [Errno 2] No such file or directory: './testdir'
# os.rmdir(apath)

## os.path.join函数可以针对各个操作系统不同的目录分隔符进行处理 避免我们手动处理的麻烦 降低出错率

print(apath)  ## ./testdir

## 当需要对某一个目录进行拆分的时候, 不要自己去判断 \(windows) 或/ 使用 os.path.split函数

print(os.path.split(apath))   ## ('.', 'testdir')  第二部分为最后一层目录或文件

## 使用 os.path.splitext函数可以直接获得文件扩展名
print(os.path.splitext(apath))  ## ('./testdir', '')  如果不是文件或没有获取到则 返回空字符串

print(os.path.splitext('filter.py'))  ## ('filter', '.py')

print(os.path.splitext('~/mirrorlist'))  ## ('~/mirrorlist', '')


## os.rename函数对文件重命名
## 如果目标文件不存在则报错  即第一个参数
# os.rename('test.md','t.md')  ## FileNotFoundError: [Errno 2] No such file or directory: 'test.md' -> 't.md'
#
# with open('test.md','w') as f:
#     f.write('hello os of python')

# os.rename('test.md','tr.md')

## 删除文件  目标不存在 则报错 FileNotFoundError: [Errno 2] No such file or directory: 'test.md'
# os.remove('test.md')


print('-===========================----------')

## 列出当前目录下的全部目录
for x in os.listdir('.'):
    ## 判断是否目录
    if os.path.isdir(x):
        print(x)


## 列出当前目录下的所有.py文件
for d in os.listdir('.'):
    ## 判断是文件 而且 扩展名为 .py  os.path.splitext函数返回一个数组 两部分构成, 前面为目录到文件名 第二部分为扩展名
    if os.path.isfile(d) and (os.path.splitext(d)[1] == '.py'):
        print(d)


## 总体上文件和目录操作 分布在两个模块  os 和 os.path
