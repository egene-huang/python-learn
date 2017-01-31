#!/usr/bin/env python3

### 生成器 generator


##创建一个生成器
## 注意非字符串不能使用 + 需要使用str将int转换为string
g = (str(i) + ' * ' + str(i) for i in range(11))


## 这和列表生成式很类似  列表生成式 使用[]括起来， 而生成器使用()括起来
## 列表生成式 是一个list 生成器是一个generator

#<generator object <genexpr> at 0x7fe69f4dd2b0>
print(g)


## 使用next可以获得生成器下一个元素

print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 0 * 0
# 1 * 1
# 2 * 2
# 3 * 3

## 每当调用next函数的时候计算下一个元素值 在没有下一个元素的时候调用next函数 则抛出 StopIteration错误


## 如果循环取出全部元素则使用for循环  for循环会自动帮我们计算是否还有元素  类似 java #Iterator #hasNext

for e in g:
    print(e)
