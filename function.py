#! /usr/bin/python
# -*- coding: utf-8 -*-

def sum(a,b):
	return a+b


func = sum
r=func(5,6)
print(r)

#提供默认值
def add(a,b=2):
	return a+b

r=add(1)
print(r)

r=add(1,4)
print(r)

print("-"*20)
#一个比较好的函数
a=range(1,10)
for i in a:
	print(i)

print("=="*20)
a=range(-2,-11,-3)
for i in a:
	print(i)