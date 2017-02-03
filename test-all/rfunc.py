#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## 高阶函数中,可以将一个函数作为参数传递,也可以将一个函数作为结果返回 这在javascript中闭包比较常见


## 通常将一个函数作为结果返回,是为了不让函数立即执行.


def outf(x):
    def inf():
        return x * x
    return inf

print(outf(3)) ## 返回内部函数地址  <function outf.<locals>.inf at 0x7f9e8f3551e0>
print(outf(3)())  ## 返回内部函数并执行返回计算结果值  9

## 这和js看起来是没有什么区别的

# function(x){
#     return function(){
#         return x * x ;
#     } ;
# }


## 每次调用 outf函数的时候返回的函数都是一个新的函数并不是上次返回的函数

f1 = outf(2)
f2 = outf(2)

print(f1 == f2)  ## False


## 其实一个函数返回另一个函数的这种行为就是一个闭包, 其返回的内部函数一般都引用了外部函数的局部变量,所以当外部函数调用结束的时候,其局部变量生命周期还没有结束,
# 所以 在js中存在的一些闭包问题在这里依然存在, 例如 常见的返回函数组问题

# function arrf(arr){
#     var fs = []
#     for(var i = 0, len = arr.length; i < len; i++) {
#         var t = arr[i] ;
#         fs.push(function(){
#             return t * t ;
#         }) ;
#     }
#
#     return fs ;
# }
#
# var funcs = arrf([1,2,3]) ;
# console.log(funcs[0](),funcs[1](),funcs[2]()) ;

## 这个调用结果并不是我们预想的 1 4 9  而是 9 9 9 这是闭包比较常见的坑 解决这个问题的办法一般都是将循环变量缓存起来,不要被循环值给覆盖

# function arrf(arr){
#     var fs = []
#     for(var i = 0, len = arr.length; i < len; i++) {
#         var t = arr[i] ;
#         fs.push(function(e_){
#             return function(){
#                 return e_ * e_ ;
#             }
#         }(t)) ;
#     }
#
#     return fs ;
# }
#
# var funcs = arrf([1,2,3]) ;
# console.log(funcs[0](),funcs[1](),funcs[2]()) ;

## 1 4 9
# 这样结果就对了

# 所以在python中也存在上述问题, 解决办法也和上面方法一致,使用另一个内部函数包裹一层,达到变量缓存的目的,使外部循环变量不会影响到结果计算使用变量


## 所以在一个函数返回另一个函数的时候,被返回函数一定不要直接引用外部函数运行时可变的变量
