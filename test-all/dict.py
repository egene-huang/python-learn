map = {'k1':'v1','k2':'v2'}
print(map['k1'])
print(map['k2'])
map['k1'] = 'hello'
map['k2'] = 'world'
print(map)
print(map['k1'])
# 判断键值 key是否存在 两种方法
#python字典提供 get方法
print(map.get('key','null'))
## get 可以指定 没有找到的返回值 默认为 None
print(map.get('key'))

## 通过 in 查找是否存在 key键值
print(('key' in map))

#根据key删除一个键值对
map.pop('k1')
print(map)

## 使用pop删除不存在的key 会报错
# map.pop('key')


# set
slist = set([1,2,3,4,56,5,5,3])

slist.add('2')

#set自动过滤重复元素
slist.add(3)

#set内部元素是不保证顺序的

#set 使用remove移除元素
slist.remove('2')

print('slist',slist)


slist2 = set([1,2,3,4,900])

print('slist2',slist2)
# 作交集
clist = slist & slist2
print(clist)

#作并集
alist = slist | slist2
print(alist)



# tlist = [1,2,3,45]
# set 和字典一样 不能使用可变数据类型作为key 否则解释报错
    # tset = set([tlist,34])
# TypeError: unhashable type: 'list'
# set(tlist)  这里key 并不是一个list
# tset = set([tlist,34])
# tset = set([tlist])  这样才是把list当作key使用了  可能是set固定语法 为set([1,2,3])
# print('list to set',tset)

## 使用元组作为set 的key 因为元组是不可变对象
tup = (1,2,3)

t_set = set([tup,45])

print('t_set',t_set)
