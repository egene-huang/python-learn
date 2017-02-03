#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## 匿名函数在计算机变成语言中存在较多,例如 java javascript objective-c等

## 有些时候,我们只是临时用一下,所以没有必要显式的声明一个函数,引起不必要的麻烦和维护成本

## python中,和js一样,当将一个函数作为参数传递给另一个函数的时候,我们可以在使用的地方才开始定义这个函数, 这时候就需要匿名函数了

l = [1,2,3,4]

it = map(lambda x:x*x,l)

print(list(it))  ## [1, 4, 9, 16]

## 在python中匿名函数的支持很有限,相比js 和java来说简直弱爆了, 在pytyon中匿名函数只能是表达式, 但是在js中匿名函数/方法
## 除了没有名字以外,函数/方法体都是完整的,和普通函数/方法没有什么两样. 所以相比python来说这种就很强大了.处理逻辑灵活多变,更能胜任相比复杂的逻辑

# function f(func,args) {
#     var arr = [] ;
#     for(var i=0 ,len = args.length;i<len;i++) {
#         var t = args[i] ;
#         if(func(t)) {
#             arr.push(t) ;
#         }
#     }
#
#     return arr ;
# }
#
#
# console.log(f(function(e) {
#     return true ;
# },[1,2,3,4])) ;

## 返回全部元素

## 在调用f函数传递的匿名函数中,可以有任何普通函数拥有的东西[甚至也可以给匿名函数启一个名字,不过就不叫匿名函数了], 但是python的匿名函数lambda中不能有return  只能有简短的表达式


## 和其他语言的匿名函数一样,可以将来一个匿名函数赋值给一个变量

lamb = lambda x:x*x

print(lamb(5))

## 同样也可以将来这个lambda 作为结果返回,返回的同样是一个函数
