#! /usr/bin/python
# -*- coding: utf-8 -*-

x={'a':'aaa','b':'bbb','c':12}
print(x)
print(x['a'])
print(x['b'])
print(x['c'])

for key in x:
	print("Key is %s and value is %s" % (key,x[key]))

'''
	知识点
		*字典像Java中的Map
'''