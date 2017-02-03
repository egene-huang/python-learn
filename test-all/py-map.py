#!/usr/bin/env python3


from functools import reduce
## 在python中,对高阶函数的支持使得很多有规律性的功能被高度的抽象出来,就像javascipt中数组提供搞基函数map一样, python中也有类似的实现


## map返回一个新的Iterator
# 在ptyon中map一共有两个形式参数,第一个是自定义功能函数,第二个是Iterable对象 如list dict 等

def fun(x):
    return str(x) + '-' + str(x)


print(map(fun,[1,2,3,4,5,6]))  ## <map object at 0x7f38396e14a8>

## 使用list函数将一个iterator变为一个 list
print(list(map(fun,[1,2,3,4,5,6])))  ## ['1-1', '2-2', '3-3', '4-4', '5-5', '6-6']


## 如果我们需要将下面一个 int类型元素的list  变为string list然后使用 ;分隔,则可以使用map

def tr(il=None):
    if il == None:
        return ''
    else:
        return ';'.join(list(map(str,il)))

print(tr([11,22,33,44,55,66,77])) ## 11;22;33;44;55;66;77

print(tr())

def upcastr(st):
    return str.capitalize(st)

print(list(map(upcastr,['adam', 'LISA', 'barT'])))


## python 提供的高阶函数 reduce累积作用在所有元素上, 比如累加,累积等 调用和map相似

def sum(x,y):
    return x * y


def osum(x,y):
    return x + y

print(reduce(sum,[1,2,3,4,5,6])) ## 720
print(reduce(osum,[1,2,3,4,5,6])) ## 21
