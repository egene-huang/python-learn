#!/usr/bin/env python3
## 复习定一个完整的python 类 --class


class Student(object):
    ## 相当于java中的构造方法 每次实例化对象会首先调用 __new__() 然后调用 __init__()方法 ;
    ## 因为python动态语言的缘故， 所以我们也可以返回别的实例给调用者
    def __new__(cls,name,age):
        print('调用 __new__方法',name,age)
        return object.__new__(cls)

    def __init__(self,name,age):
        print('初始化属性 name & age')
        self._name = name
        self._age = age

    def say(self):
        print('hello, my name is',self._name)

    def getName(self):
        return self._name
    def setName(self,name):
        self._name = name
    def getAge(self):
        return self._age
    def setAge(self,age):
        self._age = age


## 实例化对象  语法中没有 new 这种特殊构造符
stu = Student('palm',23)

print(stu.getName())
stu.say()


class GStu(Student):
    # def __init(self,name,age):
    #     self._name = name
    #     self._age = age
    def say(self):
        print('hello, my name is',self.getName(), ', 我',self.getAge(),'岁了.')

gstu = GStu('张三',23)
gstu.say()
