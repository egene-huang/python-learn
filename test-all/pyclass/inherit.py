#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## python继承

## 定义基类
class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def toString(self):
        print('我是 %s, 我%s岁了' %(self.__name,self.__age))


## 继承基类 Person
class Student(Person):
    def __init__(self,name,age,school):
        self.__name = name
        self.__age = age
        self.__school = school

    ''' 覆写父类 toString()方法'''
    def toString(self):
        print('我是%s,我%s岁了,在%s上学.' %(self.__name,self.__age,self.__school))


class XiaoMing(Student):
    def __init__(self,name,age,school):
        self.__name = name
        self.__age = age
        self.__school = school

    # def toString(self):
    #     print('我是%s,我%s岁了,在%s上学.' %(self.__name,self.__age,self.__school))


''' 接受Person任何子类对象'''
def fun(person):
    person.toString()


stu = Student('palm',24,'清华')

fun(stu)  ## 我是palm,我24岁了,在清华上学.

p = Person('palm pre',25)
fun(p) ## 我是 palm pre, 我25岁了

xm = XiaoMing('小明',25,'北大')
fun(xm) ## 我是小明,我25岁了,在北大上学.

## 当 XiaoMing对象没有覆写 toString()函数则,报错 找不到属性
## AttributeError: 'XiaoMing' object has no attribute '_Student__name'  所以在这里这个多态基本是没什么用

## 这也是python解释器改变了私有变量名称导致的. 然后在继承体系中没有动态的将私有变量翻译回来
