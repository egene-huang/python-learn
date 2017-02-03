#!/usr/bin/env python3
# -*- coding:utf-8 -*-


## 这是一个过滤器, 根据规则过滤掉符合规则的元素, 这都是高阶函数的产物

## 同样接受两个参数,第一个为规则函数,第二为一个序列, 然后根据规则函数返回值来判断是否保留该元素 ,该规则函数一次作用到序列每个元素上

## 注意: 提供的规则函数是含有一个参数的  否则会提示参数个数不匹配, 定义为0个参数,但是filter却传递了一个参数给fun
# TypeError: fun() takes 0 positional arguments but 1 was given
def fun(n):
    # return True  ## 保留全部元素
    return False  ## 舍弃全部元素

l = [1,2,3,4,5,6]

# print(filter(fun,l))  ## <filter object at 0x7f27969a14a8>

print(list(filter(fun,l))) ## 同样 filter返回也是一个iterator 需要使用list将全部元素取出来
