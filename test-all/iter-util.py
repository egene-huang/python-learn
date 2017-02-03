#!/usr/bin/env python3

##　可以迭代的集合数据类型有:  list dict tuple set str generator  以及包含yield的函数  这些类型都可以直接使用for 迭代元素

## isinstance函数可以判断一个对象是否是一个类的事例　ex: isinstance('123',Iterable)

from collections import Iterable
from collections import Iterator

print(isinstance('123',Iterable))


## 类似java，　在python中，list set dict 虽然是Iterable子类，但是并不是Iterator子类　即不是Iterator实例，需要调用一个函数得到Iterator对象才可以进行迭代
## 类似java＃　iterator（）方法

l = [1,2,3,4,5]
itor = iter(l)

## 这样这个ｌｉｓｔ就变为流式数据了，　通常这节省了内存消耗  很多函数需要Iterator

print(itor)  ## <list_iterator object at 0x7f2f0fc397b8>

## 如此 这个list就可以使用next函数进行迭代了
print(next(itor))
print(next(itor))
print(next(itor))
print(next(itor))
print(next(itor))

# print(next(itor))
## Traceback (most recent call last):
  # File "iter-util.py", line 29, in <module>
    # print(next(itor))
# StopIteration
