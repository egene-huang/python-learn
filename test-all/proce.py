#!/usr/bin/env python3
# -*-encoding:utf-8 -*-

import os
## 使用os 模块的 fork 创建一个子进程
# os.fork()
os.getpid() ## 获取进程id
os.getppid()  ## 获取子进程id

## windows  没有fork接口函数
## 一个进程 监听某一个端口  如果接到一个请求后 可以使用fork函数创建一个子进程 处理业务

## multiprocessing 模块处理 python 跨平台中多进程

from multiprocessing import Process

def run_proc(name):
    print('进程名 %s, 进程id %s' %(name,os.getpid()))


# if __name__ == '__main__':
#     print('main 进程 id ', os.getpid())
#     p = Process(target=run_proc,args=('palm',)) ## 注意这里 参数是一个tumple 单个元组写法 使用 ',' 逗号
#     p.start()
#     p.join()  ## join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。




## 进程池 Pool

from multiprocessing import Pool
import time,random

def fun(name):
    print('name ',name, '--- ', os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('%s cost time %0.2f ' %(name,(end - start)))


if __name__ == '__main__':
    print('main pid ', os.getpid())
    ## 如果不传递参数 则默认为当前cpu 的核心数  但是不知道这个核心指的是什么核心  我现在的T430 是i7双核  但是默认可以同时运行4个进程
    p = Pool(5) ## 一次创建5个  代表可以并发最多5个进程  从console 日志可以看出 当循环到5 6的时候 函数 fun不会立即执行而是等到前面5个进程执行完毕释放资源后才有进程让给5 6
    for i in range(7):
        p.apply_async(fun,args=(i,))

    print(' ---- end ---')
    p.close()
    p.join()


## 子进程 subprocess 模块启动子进程 然后控制输入和输出

import subprocess

sr = subprocess.call(['nslookup','www.archlinux.org'])

# Server:		202.106.0.20
# Address:	202.106.0.20#53
#
# Non-authoritative answer:
# www.archlinux.org	canonical name = apollo.archlinux.org.
# Name:	apollo.archlinux.org
# Address: 138.201.81.199
# Name:	apollo.archlinux.org
# Address: 2a01:4f8:172:1d86::1
#
# exit code:  0

print('exit code: ',sr)

## 通过 subprocess 模块可以模拟 命令行执行

# 进程间通信是通过Queue、Pipes等实现的
