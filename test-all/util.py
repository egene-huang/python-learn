#!/usr/bin/env python3


## 切片工具

l = [1,2,3,4,5]


## 不包含　结束位置，这里和java　的substring类似
print(l[0:3])

## 默认为从索引０开始截取
print(l[:3])

## 从最后一个元素开始取
print(l[-1])
print(l[-3])



print('=-=================================================================')



l1 = list(range(101))
print(l1)
##　获取前50个元素  0-49
print(l1[:50])

## 获取后５1个元素 50 -100
print('========================获取后５1个元素=======================')
print(l1[-51:])
print(len(l1[-51:]))


## 获取前10个数，每间隔两个取一次
print(l1[:10:2])

print('获取全部数据，每间隔１０个取一次-===========================')
print(l1[::10])

print('=========复制一个list=============')
print(l1[:])

print('tuple操作')

##元组切片操作后结果还是元组
t = (1,2,3,4,5)

print(t[:3])

print('字符串切片操作仍然是字符串=========================')

str = 'hello,world'

print(str[:5])
