#!/usr/bin/env python3

## 和javascript类似，python中函数 也可以赋给一个变量
def fun():
    print('hello function.')

f = fun
f()  ## hello function.

## 在javascript中，经常利用这个特性来扩展和定制js引擎提供api


## 当一个函数可以赋给一个变量的时候, 同时就可以将一个函数作为一个参数传递给另一个函数,在另一个函数中,使用一个变量来接受传进来的这个函数

def fu():
    print('fu funciont')



def ff(ft):
    ft()


# fu funciont
ff(fu)

# hello function.
ff(fun)


## 和在javascript中类似, 在函数中调用函数可以直接使用()调用
