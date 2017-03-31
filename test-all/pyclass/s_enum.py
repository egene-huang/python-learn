#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

## 在python中,提供了类似java的枚举类, Enum

from enum import Enum

Week = Enum('Week',('Sun','Mon','Tu','We','Th','Fr','Sa'))

print('获得了一个 Week类型的枚举类', Week.Sun)


for v in Week.__members__.items():
    print(v)

# ('Sun', <Week.Sun: 1>)
# ('Mon', <Week.Mon: 2>)
# ('Tu', <Week.Tu: 3>)
# ('We', <Week.We: 4>)
# ('Th', <Week.Th: 5>)
# ('Fr', <Week.Fr: 6>)
# ('Sa', <Week.Sa: 7>)


for k,v in Week.__members__.items():
    print('k -- ',k,' | v -- ',v.value)

# k --  Sun  | v --  1
# k --  Mon  | v --  2
# k --  Tu  | v --  3
# k --  We  | v --  4
# k --  Th  | v --  5
# k --  Fr  | v --  6
# k --  Sa  | v --  7

### 精确控制枚举类

from enum import Enum,unique

## @unique装饰器 可以保证只不会有重复值
@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

## 这样可以自定义每个成员的值

print(WeekDay.Sat.value)

for name, member in WeekDay.__members__.items():
    print('name ',name,' value ', member.value)


# name  Sun  value  0
# name  Mon  value  1
# name  Tue  value  2
# name  Wed  value  3
# name  Thu  value  4
# name  Fri  value  5
# name  Sat  value  6
