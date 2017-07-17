#!/usr/bin/env python3

import os
import shutil

def fun():
	cdir = os.path.abspath('.')
	print('cpath',cdir)
	pdst = os.path.join(cdir,'group')
	if os.path.isdir(pdst):
		print('该脚本已经运行过了,如果的确需要再次运行,可以删除目录',pdst,',然后再次运行此脚本.')
		return
	
	os.mkdir(pdst)
	psrc = os.path.join(cdir,'audio4')
	flist = os.listdir(psrc)
	le = len(flist)
	c = 0 
	PAIR = 80
	l = []
	index = 0
	for str_ in flist:
		t = c + PAIR
		if t <= le :
			l = flist[c:t]
			group(l,psrc,os.path.join(pdst,str(index)))
			print('group', index)
			index += 1 
			l = []
			c = t
		else : 
			l = flist[c: le]
			group(l,psrc,os.path.join(pdst,str(index)))
			print('group', index)
			break
	#print(flist)


def group(flist,src,dst):
	print('path ', src,dst)
	os.mkdir(dst)
	for f in flist:
		np = shutil.copy(os.path.join(src,f),dst)
#		print('copied into ', np)



## exec
fun()
