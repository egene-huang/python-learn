#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## 在学习面向对象的时候， 我自做聪明误认为 __init__就是python class的构造方法， 其实不是

## 查阅资料得知， 在执行 p = Person('测试',23)这行代码的时候， 首先调用的是 __new__这个类方法
## __init__这个是实例方法，是在实例构造完成后 使用来处理实例属性值等类似工作的 地一个参数self 就是__new__构造出来的实例


# __ new__(cls, *args, **kwargs) 创建对象时调用，返回当前对象的一个实例;注意：这里的第一个参数是cls即class本身
#
# __ init__(self, *args, **kwargs) 创建完对象后调用，对当前对象的实例的一些初始化，无返回值,即在调用__new__之后，根据返回的实例初始化；
# 注意，这里的第一个参数是self即对象本身


class Person(object):
    def __new__(cls,name,age):
        print('实例化Person 调用 __new__')
        print('属性值',name,age)
        ## 注意，这里调用的是父类的 __new__构造方法， object是没有我们自定义的属性的，所以，这里 不能 object.__new__(cls,name,age) 这是错误的
        return object.__new__(cls)

    def __init__(self,name,age):
        print('调用 __init__')
        self._name = name
        self._age = age

    def __str__(self):
        print('我是%s,我%s岁了' %(self._name,self._age))

p = Person('小张',24)

## 打印日志如下:
# 实例化Person 调用 __new__
# 属性值 小张 24
# 调用 __init__

## 所以 在实例化一个对象的时候 有限调用的是 __new__  然后接着调用 __init__ 如果 我们覆盖了 __new__ 但是没有返回值 则 __init__ 不会被调用。
## 在 覆盖 __new__ 方法的时候注意不能形成系循环  比如 在Person#__new__中， return Person.__new__(cls) 或者 子类.__new__(cls) 因为子类实例化一定会先实例化父类的 形成死循环

## 当然也可以在 __new__方法中返回其他类的实例， 那么之后不会调用自己的__init__ 而是调用__new__返回实例的__iniit方法

p.__str__()



print('----------------我是分割线----------------------------------')


class Dog(object):
    def __init__(self,name):
        print('Dog __init__被调用')
        self._name = name
    def __str__(self):
        print('我是%s' %self._name)


class Student(object):
    '''重新定义构造方法'''
    def __new__(cls,name):
        print('调用 Student __new__')
        return Dog(name) ## 返回 Dog实例
        # return Dog.__new__(cls) ## 这样依然返回 Student实例

    def __init__(self,name):
        print('Student __init__被调用')
        self._name = name
    def __str__(self):
        print('我是%s' %self._name)


stu = Student('学生')
print()
