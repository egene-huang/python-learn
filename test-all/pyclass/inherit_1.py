#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def toString(self):
        print(self)
        print('hello,%s,%s' %(self._name, self._age))


class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)


def fun(p):
    p.toString()


stu = Student('学生1',23)
fun(stu)


## 经过测试 __x 这种私有属性表现形式，因为python解释器会修改变量名,所以不能被子类继承， 所以不要使用双下划线来声明私有属性， 使用单下划线声明就好了，
# 反正在python中也没有真正的权限限制，全靠约定
