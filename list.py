#! /usr/bin/python
# -*- coding: utf-8 -*-

word=['a','b','c','d','e','f','g']

# 通过索引访问元组里的元素

a=word[0]
print ("a is " + a)

b=word[1:3]
print("b is " )
print(b)

c=word[:2]
print("c is ")
print(c)

d=word[0:]
print("d is ")
print(d)

#元组可以合并

e=word[:2]+word[2:]
print("e is ")
print(e)

f=word[-1]
print("f is ")
print(f)

g=word[-2:]
print("g is ")
print(g)

h=word[:-2]
print("h is ")
print(h)

l=len(word)
print("Length of word is : " + str(l))

word.append('h')
print(word)

#删除元素
del word[0]
print(word)
del word[1:3]
print word

'''
	知识点
		* 列表长度是动态的，可以任意添加删除元素
		* 用索引可以方便的访问元素，甚至返回一个子列表
'''













































