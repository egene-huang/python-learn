#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 排序函数同样是一个高阶函数,他们都把可变的规则抽象为一个规则函数我们自己来定义,这样,就可以实现自定义规则排序了,同时也达到了函数复用的目的


## sorted()函数 一般根据 key 函数来排序,例如:

l = [0,1,-2,-23,34,23,45,-98]

## 根据每个元素的绝对值大小来排序
print(sorted(l,key=abs)) ## [0, 1, -2, -23, 23, 34, 45, -98]

## 还支持根据 key函数的规则反向排序, 设置sorted函数的第三个参数值为 reverse=True

print(sorted(l,key=abs,reverse=True))  ## [-98, 45, 34, -23, 23, -2, 1, 0]




L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

## 按照姓名排序
def by_name(t):
    return t[0]


print(sorted(L,key=by_name))
print(sorted(L,key=by_name,reverse=True))


## 按照成绩排序
def by_score(t):
    return t[1]

print(sorted(L,key=by_score))
