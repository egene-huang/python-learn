#! /usr/bin/env python3
class Student(object):
    age = 25
    pass


stu = Student()

stu.fullName = 'palm.strive'

## 给实例绑定属性
print('hello, %s' %stu.fullName)

## AttributeError: type object 'Student' has no attribute 'fullName'
## print('hello, %s' %Student.fullName)

## 类属性
print(Student.age)

## 给实例绑定一个方法

from types import MethodType

def fun(self,gender):
    self._gender = gender

## 这里需要使用 MethodType 来绑定 而不能像绑定属性那样
## 给实例绑定的属性或方法都是这个实例独有的 另一个实例不能拥有
stu.fun = MethodType(fun,stu)

## 给stu设置性别

stu.fun('男')
stu.fun('女')

print('hello, %s, 我是一个%s孩儿.' %(stu.fullName,stu._gender))


stu1 = Student() ;
# stu1.fullName = '另一个学生'
# stu1._gender = '女'

def toString(self):
    return self.fullName + ',' + self._gender

stu1.toString = MethodType(toString,stu1)

## AttributeError: 'Student' object has no attribute 'fullName'
## AttributeError: 'Student' object has no attribute '_gender'
# print(stu1.toString())


## 给类绑定函数 则所有实例都可以使用

def hello(self):
    return 'hello python.'

Student.hello = hello

st = Student()

print(' ---  ', st.hello())

## 在python中可以使用 __slots__来限制 对象属性添加 在定义python class的时候定义一个特殊的 __slots__的变量

class Limit(object):
    __slots__ = ('name','age','gender')  ## 使用tulpe来定义允许动态绑定的 属性名


li = Limit()
li.name = '绑定测试'

print(li.name) ## 绑定测试

## AttributeError: 'Limit' object has no attribute 'xx'
# li.xx = 'xx'

## __slots___ 不能限制子类对象 只能限制当前类
