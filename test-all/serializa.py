#!/usr/bin/env pyathon3
# -*- encoding:utf-8 -*-

## 对象序列化模块 pickle

import pickle

d = dict(name='palm',gender='M',age=25)

# p = pickle.dumps(d)
# print(p) ## 结果为字节  类似b'\xxxx'

## 将对象序列化到文件中
## 这个地方 需要使用wb 因为写入的是字节数据   TypeError: write() argument must be str, not bytes
# with open('palm.md','wb') as f:
#     ## 使用dump序列化对象
#     pickle.dump(d,f)


## 使用 pickle.load 反序列化对象 pickle.loads

## 这里同样需要使用 open之前序列化对象所在的文件  因为序列化的时候写入的是字节 所以读取也需要按照字节来读取

# with open('palm.md','rb') as f:
#     o = pickle.load(f)
#     print(o)  ## {'name': 'palm', 'gender': 'M', 'age': 25}  直接获取到 dict 对象
#     print(o.get('name'))
#     print(o.get('gender'))
#     print(o.get('age'))


## python内置json模块能够 将对象序列化为 一个Json对象    方便信息交换

import json

sn = json.dumps(d)
print(sn)  # {"name": "palm", "gender": "M", "age": 25}


##写入文件
# with open('palm.json','w') as f:
#     json.dump(d,f)  ## 将对象以json格式写入文件 palm.json {"name": "palm", "gender": "M", "age": 25}

## json.loads json.load函数反序列化

print(json.loads(sn))

#
# with open('palm.json','r') as f:
#     o = json.load(f)
#     print(o) ## 返回一个标准的python对象   {'name': 'palm', 'gender': 'M', 'age': 25}


## 序列化一个自定义类

class Student(object):
    def __init__(self,name,gender,age):
        self._name = name
        self._gender = gender
        self._age = age


stu = Student('palm','男',25)
# json.dumps(stu)
## 出现错误
# Traceback (most recent call last):
#   File "serializa.py", line 64, in <module>
#     json.dumps(stu)
#   File "/usr/lib/python3.6/json/__init__.py", line 231, in dumps
#     return _default_encoder.encode(obj)
#   File "/usr/lib/python3.6/json/encoder.py", line 199, in encode
#     chunks = self.iterencode(o, _one_shot=True)
#   File "/usr/lib/python3.6/json/encoder.py", line 257, in iterencode
#     return _iterencode(o, 0)
#   File "/usr/lib/python3.6/json/encoder.py", line 180, in default
#     o.__class__.__name__)
# TypeError: Object of type 'Student' is not JSON serializable

## 使用 pickle 正常
# p = pickle.dumps(stu)
# print(pickle.loads(p)._name)


## 廖大大说 使用json模块序列化自定义类的时候需要 我们制定序列化方式 否则这个对象不可以被json序列化
## 定义这个类实例 序列化方式 类似 java writeObject 和 readobject 方法来定制序列化操作
## 再次使用json序列化独享 stu

def writeObject(stu):
    return {
        'name': stu._name,
        'gender': stu._gender,
        'age': stu._age
    }

## 中文是字节表示 需要使用关键字参数
stujson = json.dumps(stu,default=writeObject)
print(stujson)
print(json.loads(stujson))  ## 获取python对象
