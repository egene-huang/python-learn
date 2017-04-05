#!/usr/bin/env python3
# -*- encoding:utf-8 -*-


## python提供模块

## datetime

from datetime import datetime,timedelta

now = datetime.now()
print(now)  #2017-04-05 10:28:37.762380
print(type(now)) # <class 'datetime.datetime'>

## 和 java一样也有timestamp 表示时间的毫秒数  这个时间不会随着时区而变化是最准确的时间

stp = now.timestamp()
print(stp) ## 1491359551.487882

stb = datetime.fromtimestamp(stp) ## 根据本地时区转换
print(stb)  ## 2017-04-05 10:35:15.117943

sutc = datetime.utcfromtimestamp(stp) ## 根据格林威治 UTC时间转换 和当前北京时间相差8小时
print(sutc)  # 2017-04-05 02:36:13.176635


## python lib api (python api)[https://docs.python.org/3/library/]

## 格式化时间
svdate = datetime.strptime('2017-04-05 02:36:13','%Y-%m-%d %H:%M:%S') ## 有ValueError 错误
print(svdate)

## to str
strdate = now.strftime('%a,%b %d %H:%M')
print(strdate)  ## Wed,Apr 05 10:42 美国格式时间 星期 月 日 时间

## 使用 timedelta 加减时间
after = now + timedelta(days=1,hours=12)
print(after) ## 2017-04-06 22:47:28.512379
