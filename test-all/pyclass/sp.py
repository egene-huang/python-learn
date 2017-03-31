#! /usr/bin/env python3

class Student(object):
    def __init__(self,name,gender,age):
        self._name = name
        self._gender = gender
        self._age = age

    def __str__(self):
        return 'Student(name: %s,gender: %s, age: %s)' %(self._name,self._gender,self._age)

    __repr__ = __str__


stu = Student('palm','M',25)

##自动调用了 class Student覆写的 __str__ 这个python特殊的函数 类似 java Object 对象上的 toString方法
print(stu)  ## Student(name: palm,gender: M, age: 25)

## 这样调用的是 __repr__ 函数而不是我们覆写的 __str__函数 所以 当我们没有覆写 __repr__函数的时候, 打印的依然是对象地址 除非 __str__()
print(stu.__str__)


## 当我们在类中定义了 __iter__函数则代表这个类的对象可以被迭代  可以用于for ... in ...上  就像一个list


## 需要实现 __iter__函数 和 __next__函数  这样这个对象就能使用 for in 循环了 for in 会一直调用 __next__ 函数 知道捕捉到 StopIteration异常
class Ilist(object):
    def __init__(self,count):
        self._cur = 0
        self._count = count

    def __iter__(self):
        return self

    def __next__(self):
        self._cur = self._cur + 1
        if self._cur > self._count:
            raise StopIteration() ## 超出范围抛出异常  StopIteration 异常  该异常能被for in循环捕获
        return self._cur

    def __getattr__(self,attr):
        if attr == 'age':
            return 25
        raise AttributeError('没有这个属性, 不要扯淡') ## 按例依然抛出异常


# for v in Ilist(100):
#     print(v)


## 总之 需要她像什么就实现这个鸭子的函数 就可以了


## 在python中 可以覆写 __getattr__函数来处理 动态增加属性出现可能混乱的局面, 因为当我们调用一个不存在的属性的时候 python会转而调用__getattr__函数 处理
## 这让我们对程序有更进一步的把控 ,不至于太混乱 可以适时调整

il = Ilist(100)
print(il.age) ## 25
# print(il.gender)
#
# Traceback (most recent call last):
#   File "sp.py", line 60, in <module>
#     print(il.gender)
#   File "sp.py", line 45, in __getattr__
#     raise AttributeError('没有这个属性, 不要扯淡')
# AttributeError: 没有这个属性, 不要扯淡



## 通过 __getattr__函数实现链式调用 真是太强大了 下面是廖大大的代码

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__



## 不得不说 利用 __getattr__实现这个特性真是太牛逼了  我不要膝盖了  ~@!!!!
print(Chain().user.palm.blog)  ## /user/palm/blog
