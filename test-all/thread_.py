#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

## 多线程
## _thread (低级模块) / threading(高级模块 对_thread的封装)  平时使用threading 创建多线程

import threading, time
## 使用起来跟 java Thread 好象

def run_():
    print('thread %s is running.' %(threading.current_thread().name))

    for i in range(5):
        print('thread %s ===> %s ' %(threading.current_thread().name,i))
        time.sleep(i) ## 越来越慢


## 创建一个线程
t = threading.Thread(target=run_,name='Loop')
## 再创建一个线程
t1 = threading.Thread(target=run_,name='Loop1')
## 启动线程
# t.start()
## 启动另一个线程
# t1.start()
# t.join()
# t1.join()
print('main thread name is %s' %(threading.current_thread().name))

#  thread Loop is running.
# thread Loop ===> 0
# thread Loop ===> 1
# thread Loop ===> 2
# thread Loop ===> 3
# thread Loop ===> 4
#  main thread name is MainThread


## 共享资源在多线程 中的问题  和java一样 也会出现数据被篡改的问题

## 全局变量
sharer = 500

def add_(v):
    global sharer
    # time.sleep(3)
    sharer = sharer + v

def sub_(v):
    global sharer
    sharer = sharer - v

def run_thread(n):
    ## 这个值需要设置稍微打一点 否则可能看不出来
    for i in range(1000000):
        add_(n)

def run_thread_(n):
    for i in range(1000000):
        sub_(n)

## 这个线程负责存钱
t0 = threading.Thread(target=run_thread,name='T0',args=(50,))

## 这个线程负责取钱
t2 = threading.Thread(target=run_thread_,name='T2',args=(50,))

# t0.start()
# t2.start()
#
# t0.join()
# t2.join()

print('最终的值 %f ' %(sharer)) ## 最后这个值 不再是 500


## 通过threading.Lock() 获取线程锁 保护共享资源不被随意篡改


sx = 100

## 多个线程共用这个锁
lock = threading.Lock()

def change_add(n):
    global sx
    sx = sx + n

def change_sub(n):
    global sx
    sx = sx - n

def thread_add(v):
    for i in range(10000000):
        ## 先获取锁
        lock.acquire()
        try:
            change_add(v)
        finally:
            ## 释放锁  否则其他线程无法进入
            lock.release()

def thread_sub(v):
    for i in range(10000000):
        lock.acquire()
        try:
            change_sub(v)
        finally:
            lock.release()


##
t3 = threading.Thread(target=thread_add,name='add',args=(50,))
t4 = threading.Thread(target=thread_sub,name='sub',args=(50,))
# t3.start()
# t4.start()
# t3.join()
# t4.join()


print('---  sx %f' %(sx))


## ThreadLocal 对象 用来保证一个每个线程拥有自己的内部对象 而不需要我们去分配和管理


class Student(object):
    def __init__(self,name,gender):
        self._gender = gender
        self._name = name

##创建多线程共用的 对象管理对象ThreadLocal 实例
local_o = threading.local()

def getArg():
    t_name = local_o.tName
    print(t_name)
    print('当前线程 %s, 参数 %s --- > %s' %(threading.current_thread().name,t_name._name,t_name._gender))

def setArg(v):
    # print(v)
    ## 绑定需要给线程的参数
    local_o.tName = Student(v.get('name'),v.get('gender'))
    getArg()


th0 = threading.Thread(target=setArg,args=({'name':'palm','gender':'男'},),name='ThreadA')
th1 = threading.Thread(target=setArg,args=({'name':'张三','gender':'女'},),name='ThreadB')
th2 = threading.Thread(target=setArg,args=({'name':'李伟','gender':'男'},),name='ThreadC')
th3 = threading.Thread(target=setArg,args=({'name':'veer','gender':'女'},),name='ThreadD')


th0.start()
th1.start()
th2.start()
th3.start()

th0.join()
th1.join()
th2.join()
th3.join()

## 每个线程自己的属性 独有

## ThreadLocal 保证了每个线程拥有一个Student对象的一个副本 修改互不影响
