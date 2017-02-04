#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## 访问控制


class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def toString(self):
        print('我是%s,我%s岁了.' %(self.name,self.age))


p = Person('palm',25)

p.toString()  ## 我是palm,我25岁了.

## 可以随意修改 这个对象的属性值

p.name = '王八蛋'
p.age = 12345

p.toString()  ## 我是王八蛋,我12345岁了.
## 显然数据 被随意的破坏了

## 在python中,定义私有变量使用 __ [双下划线], 如

print('---------------- 对象属性私有化')


class PrivPerson(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def toString(self):
        print('我是%s,我%s岁了.' %(self.__name,self.__age))

pp = PrivPerson('palm','26')

pp.__name = '王八蛋'
pp.__age = 12345
pp.toString()  ## 我是palm,我26岁了.

print(pp.__name) ## 王八蛋
print(pp.__age)  ##12345

## 这里修改对象属性值没有成功

## 所以 对象属性私有化需要使用 双下划线 [__]作为属性变量名的前缀, 这样 __开头的属性只有对象内部可以访问,外部不可以访问

## 我发现,这样也只是保证了通过对象方法访问对象属性的时候是正确的,从外部直接访问依然是不正确的.所以在权限控制这块,依然没有java严谨.
## 这种机制只能防止君子
## 不过这已经算是一个保障了, 保障了对象内部的状态是正确的

## 同java一样 可以新增 get /set方法 来达到对象属性获取和修改正确, 如此也可以对象参数进行校验

## _x 和 __x 都是私有变量 只是后者约束性更强,前者只是约定,是可直接访问的

## 在python中,属性私有化 是把私有变量名称改变了,所以不能访问 所以我们从外面改变私有变量,其实只是动态的新增了属性 完全是幻觉

## _PrivPerson__name  == __name

## 我算是明白了,pytho中权限设置基本是摆设,你若要强上 谁也拦不住你, 所以全靠自觉, 难道pythoner自觉性真的很强?  能强忍住不上, 我服!
