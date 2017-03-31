#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

## BytesIO 可以操作字节型数据 例如二进制数据
## StringIO 只能处理 str 数据

## BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes

from io import BytesIO

bi = BytesIO()
bi.write('中华人民...'.encode('utf-8'))

print(bi.getvalue())  ## b'\xe4\xb8\xad\xe5\x8d\x8e\xe4\xba\xba\xe6\xb0\x91...'

## 可以使用 BytesIO对象构造另一个 BytesIO, 然后读取


bio = BytesIO(b'\xe4\xb8\xad\xe5\x8d\x8e\xe4\xba\xba\xe6\xb0\x91...')
print(bio.read())


## StringIO 和BytesIO 是 file-like Object
