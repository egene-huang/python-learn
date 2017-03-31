#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

## 读文件
try:
    f = open('util.py','r') ## r 表示 '读'文件
    print(f.read()) ## read一次读取全部文件到内存中
finally:
    if f:
        f.close() ## 调用close函数关闭 文件



## 使用 with .. as .. python自动帮我们关闭文件 ,不需要显式调用close()函数来关闭文件
with open('generator.py','r') as f1:
    print(f1.read())



## 使用  read(size) 读取规定容量的内容  readline一次读取一行数据  readlines 一次读取全部行, 并返回一个行list

with open('generator.py','r') as r:
    for l in r.readlines():
        print(':  ',l.strip())  ## strip 去除末尾的 \n
        # print('\n')


## 使用 rb 来读取二进制文件 如图像 视频等

j = open('/home/palm/Pictures/tomcat-container.png','rb')
print(j.read()) ## \xac\x88\x88\x88\xc8F\xf6\xff\x01D\x8f\xd5\xa3TN:Y\x00\x00\x00\x00IEND\xaeB`\x82'
j.close()


## 读取特定编码的文件 需要传递参数 encoding='gbk' errors 表示遇到错误的处理方式 'ignore'表示忽略  这样可以正常读取文件,但是 多半是乱码
try:
    with open('iter-util.py','r',encoding='utf-8',errors='ignore') as g:
        print(g.read()) ## 编码错误: UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 28: illegal multibyte sequence
except UnicodeDecodeError as e:
    print(' exception info : ',e)


## 写文件 参数 'r'变为 'w' 或'wb'

## 这种方式,如果文件不存在则 会自动创建, 如果目录不存在则会报错    FileNotFoundError: [Errno 2] No such file or directory: '/home/palm/xx/test.md'
with open('/home/palm/Pictures/test.md','w') as w:
    w.write('hello python io.  chanage\n')
    w.write('这是一行数据.\n')

## 使用with 操作文件 可以防止因为忘记关闭文件  f.close() 而导致资源一直占用, 或者是文件写入内容丢失,
## 同样使用open函数往文件中写入内容的时候 可以制定编码 encoding='utf-8' python帮我们转换编码 然后写入
