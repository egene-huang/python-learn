#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

## 使用type() 判断一个对象的类型

class Hello():
    def hello():
        print('hello, python !')


h = Hello()



## main函数 入口函数
if __name__ == '__main__':
    print(type(h))  ## <class '__main__.Hello'>
    print(type(Hello))  ## <class 'type'>  是class类型
    print(h.hello)  ## <bound method Hello.hello of <__main__.Hello object at 0x7fa62caeda90>>


## type()还可以用来动态的创建一个类,而不用规范格式来定义一个类
def fn(self):
    print('hello type.')

Hellc = type('Hellc',(object,),dict(hello=fn))

Hellc().hello() ## hello type.


## python中的元类 metaClass有点理解不了 先放下 后根据需要再次肯理解一遍
