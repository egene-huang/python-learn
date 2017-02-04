#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import types


## 通过type()函数可以获取对象信息
print(type(123)) ## <class 'int'>


class Student(object):
    def __init__(self,name,age):
        self.___name = name
        self.__age  = age

    def toString(self):
        print('我是%s, 我%s岁了．' %(self.__name,self.__age))

class XiaoMing(Student):
    pass

def fun(stu):
    stu.toString()


# xm = XiaoMing('小明',23)
# fun(xm)

stu = Student('学生1',24)


print(type(stu)) ## <class '__main__.Student'>

## 判断是否是函数 可以使用 types模块 各种类型的常亮

print(type(fun)) ## <class 'function'>
print(types.FunctionType) ## <class 'function'>


##通常使用这个常量来判断对象是否函数类型
print(type(fun) == types.FunctionType)  ## True

## 判断是否是某一类型的实例, 使用isinstance()函数

print(isinstance(stu,Student))  ## True

## 基本类型大豆使用 type()函数来判断  自定义类型可以使用  isinstance()函数来判断

## 使用dir()函数可以获得对象的所有信息, 包括 __x__这种特殊方法和属性 , 并返回字符串 list

print(dir(stu))
## print
r = ['_Student___name', '_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'toString']


## 对象方法, 例如setattr

setattr(stu,'school','清华')

## 是否有指定属性
print(hasattr(stu,'school'))  ## True

## 获取属性值
print(getattr(stu,'school')) ## 清华

## 如果获取一个不存在的属性变量,则报错

# print(getattr(stu,'aaa'))  ## AttributeError: 'Student' object has no attribute 'aaa'

##　可以提供一个默认值，当获取不到的时候 类似map的get　方法

map = {'k1':123}
print(map.get('k2','null')) ## null 默认返回None

##　指定默认返回值
print(getattr(stu,'aaa','null')) ## null 字符串

## getattr函数不仅仅可以获取属性，　也可以获取对象方法

##在使用　getattr的时候应该首先使用　hasattr判断获取的属性或方法是否存在
