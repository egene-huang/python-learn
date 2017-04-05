#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

## 正则 像byte数据表示一样  python 使用 r表示正则字符 如此 我们不需要担心字符转义的问题  如: r'\d{3}'

import re

inp = 'Python'

rs = re.match(r'(P|p)ython',inp)
## match 函数判断是否匹配, 匹配成功则返回 Match对象  否则返回 None
if rs:
    print('right !')
else:
    print('wrong !')


## 日常经常用到的 字符串切分

s = 'a b c d e f'

rs = re.split(r'\s+',s)
print(rs)  ## ['a', 'b','c','d', 'e', 'f']

## 和java类似 python中的 Match对象不仅有match函数还有 group和groups函数  返回想要的匹配组 group(0)返回原始字符

## 使用group自取字串  注意匹配失败的时候  不能使用group函数
print(re.match(r'^(\d{3}-(\d{3,8})$)','010-10234562').group(0))
print(re.match(r'(\d{3}-(\d{3,8}))','010-10234562').group(1))
print(re.match(r'(\d{3}-(\d{3,8}))','010-10234562').groups())


e = 'palm.strive@gmail.com'

## 不会写
# reg = re.match(r'^[\w\d\.\w]+@(\w+)\.(com|cn|net|org)$',e)
#
# if reg:
#     print(reg.groups())
# else:
#     print('error mail addr of %s' %e)
