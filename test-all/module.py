#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## 模块在很多地方都有用到,他可以形成一个小的作用域,有效避免命名空间的冲突 在Node.js中,或很多第三方的js框架中使用很多,在java中使用 包.类名来解决这些问题,其实也算是模块的概念


## 在ptyon中, 使用一个多级目录来达到模块的概念, 一个模块下需要有一个 __init__.py文件来标示这是一个模块而不是一个普通的目录

## 例如 com.cn.sys.util.py  com.cn.web.util.py


## 在py文件中, 任何第一行字符串都被解释为 文档注释

'test module doc'

## 注释文件创作者  和 @author一致
__author__ = 'palm.strive'

## 这之后才是真正的业务代码  这是python文件编写的一般规范

## 如果我们想使用一个模块,则需要先导入该模块,语法如下

## 导入python 内置模块 sys
import sys

def test():
    args = sys.argv
    # print(args)
    print('hello, module.')


## python module.py  //print  ['module.py']
## python module.py hello //print  ['module.py', 'hello']

# test()


## 在python交互环境中, 导入本模块,不会立即执行 test函数, 如果没有这个判断则会立即执行test函数
if __name__ == '__main__':
    test()


## 模块内作用域限制

## 在python中约定 _x __x 类似这种变量定义,是private的, 是不应该直接使用的  和java不一样的是,这种限制是约定的,不是完全不能访问,只是一种约定


## 可以设定 PYTHONPATH 环境变量 添加自己的python模块搜索路径
