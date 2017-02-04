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
## 在实例化 Student 对象的时候和java不同的是 没有使用 new关键字 而是像调用一个方法名首字母大写的普通的方法一样
## 其实在 java中构造方法也是一个特殊的方法

## 凡是面向对象的语言都有 三大特性  封装 / 继承 / 多态

## python是一动态语言,所以可随时给一个对象绑定属性, 如:
stu.score = 234
print(stu.score)  ## 234
## 动态绑定/删除属性 这应该是动态语言的通性

## 在构造clss实例的时候, 我们只需要传递构造方法中需要绑定的属性值就可以了, self 不需要传递,python解释器帮我们传递进去, 这个参数需要在第一个参数位置声明,
## 所以我猜想,__init__方法 和java中的构造方法一样, 构造方法的调用是对象构造完成的最后一步 ,在调用 __init__方法的时候类实例已经构造出来了,只是属性还没有初始化完成


##在类中定义方法, 有一个特点是,第一个参数永远是实例本身变量 self 否则无法使用 self


class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def fun(p):
        print('这是一个普通方法,%s' %p.name)
    # def pstu(stu):
    #     print(stu.score)   ## TypeError: pstu() takes 1 positional argument but 2 were given
    def pstu(self,stu):
        print(' Student对象,属性值,',stu.score)

    def fun_(self):
        print('在类中定义的方法必须包含self参数')


p = Person('palm',24)

## 如果类中包含一个不包含 self参数的普通方法,会报错, python解释器永远会自动帮我们传递一个实例进去
# p.fun() ##  TypeError: fun() takes 0 positional arguments but 1 was given

p.fun_()
p.fun()
p.pstu(stu)

## 所以在python 类上定义的方法第一个参数永远是实例本身 self 我觉得这也是封装的需要 ,
# 获取数据都需要通过方法, 不直接获取对象绑定数据也是为了进一步的解耦合,方便代码维护,也不用暴露实现细节

## 由于动态语言和静态语言在数据类型约束上有所不同, 动态语言不需要类型声明,一个变量在任何时候可以容纳任何类型的数据, 所以在类中存储的数据不需要像java那样需要将数据类型首先声明

## 在js中也是类似的

# function Person(name,age) {
#     this.name = name ;
#     this.age = age ;
# }

## 在获取Person实例的时候, var p = new Person('palm',23) ; 直接调用了函数 Person python则专门提供了一个构造方法, 我想这比js仓库设计在后续的扩展和灵活性上应该更胜一筹
