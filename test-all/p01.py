#!/usr/bin/env python3

# result = 100 + 200
# print('hello, python! result: ' + str(result))
#
# print('hello,python ! other result: ',result)
#
#
# # accpet = input('input some string please:')
# # print('input content : ',accpet)
#
#
# print('1024*168=',1024*168)
#
# print(12//8)
#
#
# v =((85-72)/72) * 100
# print('%.1f%%' %v)



# list = ['A','B','C']
# print(list)
# list.pop(1)
# print(list)
# list.insert(6,'F') ;
# print(list)
# print(len(list))
# list.append('K') ;
# print(list,len(list))



# list example

# list = [] ;
# list.append('A') ;
# list.append('B') ;
# list.append('C') ;
# list.append('D') ;
# print(len(list),'\n',list) ;
# list[0] = 'a' ;
# print(list) ;
#
# list.insert(0,'A') ;
# print(list,'\n',len(list)) ;
#
#
# list.insert(9,'E') ;
# print(list) ;

# if example
# age = 20 ;
# if age == 18:
#     print(' miss ..') ;
# elif age == 20:
#     print('hello you\'re 20.') ;
# else :
#     print('right!') ;



# list = ['A'] ;
# list.pop() ;
# if list:
#     print('this is not empty list') ;
# else:
#     print('this is empty list') ;


## a case
# h = 1.75
# w = 80.5
#
# bmi = w / (h * h)
#
# print(bmi)
#
# if bmi < 18.5:
#     print('过轻')
# elif bmi < 25 and bmi >= 18.5:
#     print('正常')
# elif bmi >= 25 and bmi < 28:
#     print('过重')
# elif bmi >= 28 and bmi <32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# while case
#
# list = ['A','B','C','D']
# for str in list:
#     print(str)

#
# sum = 0
# for i in list(range(11)):
#     sum += i
#
# print(sum)

# sum = 0
# v = 100
# while v > 0:
#     sum += v
#     v-=1
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
#
# for v in L:
#     print('Hello,',v,'!')

#
# sum = 100
# count = 0
# while sum > 0:
#     count += 1
#     if sum == 50:
#         break
#     sum -=1
# print('循环了',count,'次')


list = [1,2,3,4,5,6]

clist = []

for v in list:
    if v == 4:
        continue
    clist.append(v)

print(clist)
