#!/usr/bin/env python3


## 迭代
## 在python中使用 for in 迭代可迭代对象
for str in 'ABC':
    print(str)


for var in list(range(10)):
    print(var)

## 在java中 任何对象只要实现 Iterable接口并提供一个返回Iterator对象的iterator方法，然后根据自己需求实现hasNext和next方法 如此就是一个可迭代对象了

## python中默认 for in迭代dict(字典)的key

for k in {'java':'hello','python':'world'}:
    print(k)

## 如果需要迭代dict中的value 则需要调用values函数获取全部值

dc = {'java':'static','python':'dynamic'}

for v in dc.values():
    print('=== values in ',v)

## 如果需要同时迭代 dict的key 和value则，使用两个变量接收迭代值就可以了
for k,v in dc.items():
    print('key is: ',k,'; vlaue is: ',v)


## 判断一个对象是否是可迭代对象,需要使用collections 模块的 Iterable

from collections import Iterable

print(isinstance(dc,Iterable))  ## True
print(isinstance('asd',Iterable)) ## True
print(isinstance('123',Iterable)) ## True
print(isinstance(123,Iterable))  ## False

print(isinstance([],Iterable)) ## True



## 在for循环中使用两个变量接收迭代值

for x,y in [(1,2),(3,4),('hello','world')]:
    print(x,y)

## 多个变量接收迭代值的时候，一定要注意匹配，否则会得到运行错误
## ValueError: not enough values to unpack (expected 2, got 1)
# for i,j in ['A','B','C','D','E','F','G']:
#     print('========',i,j)
