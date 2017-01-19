#!/usr/bin/env pyhon3

## 递归调用

def fn(n):
    if n == 1:
        return 1
    else:
        return n * fn(n-1)

# print(fn(100))


## 尾递归优化
def fn1(n,accumulate):
    if n == 1:
        return accumulate
    else:
        return fn1(n-1,n*accumulate)

# call
print(fn1(100,1))
