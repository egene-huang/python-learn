#!/usr/bin/env python3



## list 生成式
## list comprehensions python内置工具
l = [x*x for x in range(1,11)]
## [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l)

## ['1_1', '2_2', '3_3', '4_4', '5_5', '6_6', '7_7', '8_8', '9_9', '10_10']
l = [str(i) + '_' + str(i) for i in range(1,11)]
print(l)


## 类似迭代器
##  ['A=a', 'B=b', 'C=c']
di = {'A':'a','B':'b','C':'c'}

print([key + '=' + value for key,value in di.items()])
