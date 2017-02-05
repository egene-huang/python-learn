#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## 在python class中 直接存在的属性称为类属性,类属性可以直接通过类访问，而且这些类属性，其实例都可以访问

class Person(object):
    name = '这是类属性'
    def __init__(self,age):
        self._age = age



p = Person(24)
print(Person.name) ##  这是类属性
print(p.name) ## 这是类属性

# print(Person._age)  ## 这是实例属性 类不能访问  AttributeError: type object 'Person' has no attribute '_age


print('--------------- 分割线-----------------------')
p1 = Person(14)
p1.name = '我是p1'

print(Person.name) ## 这是类属性
print(p.name) ## 这是类属性

## 类实例只能访问类属性， 而不能改变类属性  当实例绑定了和类同名的属性时，则该类属性会被实例覆盖
## 这有点像javascript 的原型链

print(p1.name) ## 我是p1

## 删除实例属性

del p1.name
print(p1.name) ## 这是类属性

## 删除实例属性后，实例访问name得到的值就是类属性的值  优先从实例上查找

del Person.name ## 删除类属性
print(Person.name) ## 类属性被删除了  AttributeError: type object 'Person' has no attribute 'name'
