#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

## python 错误/异常处理机制

try:
    v = 10/0
    print('v -- ',v)
except ZeroDivisionError as ze:
    print('除数不能为0')
finally:
    print('调用结束')

print('代码执行完毕.')

## 代码执行顺序 和java的try .. catch .. finally.. 是相同的

# 除数不能为0
# 调用结束
# 代码执行完毕.


def fn():
    try:
        rs = 10/0
    except Exception as e:
        return 12
    finally:
        return 30


print(fn())  # 30


def fnt():
    try:
        return 10/2
    except Exception as e:
        print(e)
    finally:
        return 50

print(fnt()) ## 50


## 通过继承可以自定义错误类型
class MyException(Exception):
    pass


## 使用自定义异常
def test(n):
    raise MyException('自定义异常测试')

# test(1)

## raise 语句如果不给参数 则表示将当前错误原样抛出  同样可以像java 异常一样 将一个异常包装为另一个异常抛出  和构造一个实例一样的方式


## 可以使用断言 aseer来调试程序

def fs(n):
    assert n == 0,' 参数不正确'
    return 'ar'

print(fs(0))


## logging 打印日志

import logging

## 配置 logging  这样才会打印 info级别的日志

## debug，info，warning，error
logging.basicConfig(level=logging.INFO)
def fi(i):
    logging.info(' 参数值 %s' %i)


fi(8)  # INFO:root: 参数值 8

## 通过pdb 调试程序  单步调试

## 廖大婶的科普 http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000

## doctest
