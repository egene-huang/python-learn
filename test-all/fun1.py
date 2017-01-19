#!/usr/bin/env python3


#指定函数参数默认值
def p(x,n):
    sum = 1
    while(n > 0):
        sum *= x
        n-=1
    return sum

## call
print(p(2,3))

#也可以不用传递第二个参数值,可以默认为计算某一个数的平方
#不指定默认值,则调用为强制参数,为必传参数
def p_(x,n=2):
    sum = 1
    while(n > 0):
        sum *= x
        n-=1
    return sum


# test
print(p_(2))

## python和javascript采用了类似参数站位的方式,
## 这种在参数声明的时候指定值,在java这种静态语言就没有这种灵活性了,但解释起来确实也会费力一点

## 和javascript 一样 或者java的可变长参数一样, 可选参数都需要在必选残水之后,这点在javascript和python中尤其重要
## 因为后两者都是占位的方式, 在python中,可选参数放在必选参数之后,python解释器报错

# def test(n=2,x):
#     return n,x

# test
#SyntaxError: non-default argument follows default argument
# print(test(4))


## 当一个函数同时有两个以上的可选参数的时候,调用时,又只想传递可选参数中的某一个,可以使用键值对的方式指定传递哪一个可选参数

def arg(name,age=20,city='北京',gender='男'):
    return name,age,city,gender


## 假如 需要传递 'palm' 20 陕西 男

## ('palm', 20, '陕西', '男')  这样就不会导致位置不匹配 参数值获取错误的情况了
print(arg('palm',city='陕西'))
## 这样也可以不用按照参数顺序给值了


def lists(L=[]):
    L.append('END')
    return L

print(lists())
print(lists())  ## 第二次调用会出现  ['END', 'END']  之前的L被记住了
 # 定义默认参数要牢记一点：默认参数必须指向不变对象！


## python 格式相当严格  刚刚函数定义钱有空格就出现了  IndentationError: unexpected indent错误
def lists_(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print('========================')
print(lists_())
print(lists_())
## 这样使用　None这种不变的类型来作为初始参数值，就好了

## 因为这样L 永远都指向的一个不可变的对象None

## 可变长参数定义
def cfun(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        sum += num

    return sum

print(cfun(1,2,3,4,5,6,7,8,9,10))
print(cfun())

## 在java中定义可变长参数是这样的,　方法内部接受到的是一个指定类型的数组

# public void fun(String ... args) {
#
#     System.out.println(args) ;
# }

## 在python中函数内部接受到的是一个tuple

## 在python中如果手持一个list调用一个可变参数的函数可以这样

l = [1,2,3,4,5,5,6,7]
## 在l钱加上*就可以把一个list 或者tuple当做一个可变参数传递
print(cfun(*l))


## 关键字参数　**kw

def kfun(name,age,**kw):
    print(name,age,kw)


## call
kfun('palm',23,city='Beijing')
 ##这和可选参数无序调用类似,　这和在javascript中使用{}传递多个参数和扩展参数方法差不多　

 ## 和可变参数一样　如果手里已经有一个字典变量则可以使用　［**变量名］ 直接将这个字典对象传递给函数

## 关键字参数不能定义和必选参数相同的变量名否则报错
## TypeError: kfun() got multiple values for argument 'age'
d = {'ais':'pre2','gender':'F','city':'Beijing'}

kfun('palm',23,**d)
## 在函数内部检查是否存在关键字参数的某一个参数，可以使用 in　　因为实际上函数接受到的是一个字典变量

def kfun2(name,**kw):
    print(name,kw)
    if 'city' in kw:
        print(kw['city'])
    if 'gender' in kw:
        print(kw['gender'])

kfun2('pre2',**d)


## 在python中使用*隔离的办法限制关键字参数的名字

def kfun3(name,age,*,city,job):
    print(name,age,city,job)

## 传入不被允许关键字参数则会报错
# kfun3('veer',24,**d)
## TypeError: kfun3() got an unexpected keyword argument 'ais'


dc = {'city':'Beijing','job':'java'}
kfun3('vver',24,**dc)

## * 之后的参数都是命名关键字参数,意味着关键字参数的名字叫什么，这之外的关键字参数都不被认可
## 命名关键字参数同样可以指定一个默认值,这样就可以不用传递这个参数了

def kfun4(name,*,city='Beijing',job):
    print(name,city,job)

## 这里不用传递city参数　默认为Beijing
kfun4('p2',job='java Dev')


## python支持　参数类型如下
## 必选参数／位置参数
## 默认参数(参数默认值)
## 可变参数　　*args
## 关键字参数  **kw
## 命名关键字参数  name,*,city,job  使用 * 分隔

### 以上五中参数类型可以组合使用，但是要遵从　必选参数　默认参数　可变参数　命名关键字参数 关键字参数的顺序声明　，不能混乱


def fun5(name,gender='男',*args,**kw):
    print(name,gender,args,kw)

lis = ['hello','world']

dics = {'city':'Beijing','test':'测试'}

ds = {'job':'java'}

fun5('palm650',lis,**dics)


## ＊args 可变参数　函数接受的是一个元组 tuple
##　**kw 关键字参数　函数接受的是一个字典 dict

## 将一个list或tuple传入可变参数函数需要使用　＊args方式转换  或*(1,2,3) 　一般都是分散传递如：　fn(1,2,3,4)
## 将一个字典 dict传入关键字函数需要使用　**kw方式转换 也可以使用指定键值对传递 如: fn(city='Beijing',job='java')
