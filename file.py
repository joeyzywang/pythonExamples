#! /usr/bin/python
# -*- coding: utf-8 -*-
def readFile(path):
	print("=="*10 + " fileContent " + "=="*10)
	f=open(spath,'r')
	for line in f:
		print("Each line is: %s" % line)
	f.close()

spath="./baa.txt"
f=open(spath,'w')
f.write("First line 1. \n")
f.writelines("First line2.\n")
f.close()
print("Write file done!")

readFile(spath)

f=open(spath,'a')
f.write("Add a new line there")
f.close()
print("Append done !")

readFile(spath)

'''
	知识点：
		*打开后记得关闭
		*open用于打开一个文件，r读，w写，a打开并附加内容
'''