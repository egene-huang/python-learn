#!/usr/bin/env python3
# -*- coding:utf-8 -*-


## python 面向对象 类的定义  和java一样使用了 class关键字

class Student(object):
    ''' 这是注释: 构造方法 构造Student对象的时候调用'''
    def __init__(self,name,age):
        self.name = name
        self.age = age

        '''这是发送消息的方法 '''
    def print(self):
        print('我是%s, 我 %s 岁了!' %(self.name,self.age))


## 这里面定义使用了 self关键字, 我想和java中的 this概念差不多 只是在python中,需要明确声明,在java中不需要

## __init__ 是类似java的构造方法 用来构造 class Student这个类的实例的

## 获得 Student这个类的实例
stu = Student('palm',24)

## 调用对象上的方法打印信息 [发送消息]
stu.print() ## 我是palm, 我 24 岁了!


## 在定义类的时候,括号中放置的是父类,这是继承的表现形式, 和java类似 也是所有类都是object的子类[java中 首字母大写 Object]


## 凡是面向对象的语言都有 三大特性  封装 / 继承 / 多态
