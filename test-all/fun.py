#!/usr/bin/env python3

import math

print(abs(-123))

#error one arguments
# print(abs(-1234,123))


print(int('12345'))

#error
# print(int('sd'))


#给函数取别名 和js中函数一样可以将函数赋值给一个变量 这在java中是不可以的
_abs = abs
print(_abs(-234))


#hex 将一个正数转换为16进制字符
print(hex(123))

#只能是数字   TypeError: 'str' object cannot be interpreted as an integer
# print(hex('123'))

#只能是integer类型 不能是其他类型 如float
#'float' object cannot be interpreted as an integer
# print(hex(12.3))

#定义一个函数
def fun(x,y):
    if x > y:
        return x
    else:
        return y


print(' --- ',fun(1,2))
print(';;;;;;;;;', fun(3,4))

#如果函数没有明确的返回某一个值,则函数默认函数None
#如果函数明确返回,但没有指定返回值,则返回None  这类似 java 中的void 如

# public void fun(boolean b) {
#     return ;
# }

# 在python 中 return 和return None含义是一致的
def func(x,y):
    if x > y:
        return None
    else:
        return

## 空语句pass 定义一个控函数 还是用pass 否则函数不能运行
def f_():
    ## SyntaxError: unexpected EOF while parsing
    # pass
    pass


#错误参数类型检查
# isinstance

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


    # raise TypeError('bad operand type')
# TypeError: bad operand type
# print(my_abs('12'))
print(my_abs(-123))



#函数可以返回多个值
def mur(x,y):
    if x > y:
        return x
    else:
        return x,y

print(mur(1,2))   #(1, 2)

#使用一个变量接受函数返回的多个值,则使用了元组(tuple)来包装返回
#虽然实际上函数只返回了一个值,但是可以支持返回散列的多个值这种语法,在java 中是不可以的,
#在python中 可以用多个变量来接收一个tuple元素,只要位置对应正确,就可以接收到正确的值

a,b = mur(3,4)
print(a,b)  #3 4



# 根据给定参数求解方程ax2 + bx + c = 0的根
#(-b +-)/2a
def quadratic(a,b,c):

    dt = b*b - 4*a*c
    if dt < 0:
        return '该方程没有根'
    else:
        x1 = (-b + math.sqrt(dt))/(2*a)
        x2 = (-b - math.sqrt(dt))/(2*a)
        rs = set([x1,x2])
        return rs



print(quadratic(1,4,4))
