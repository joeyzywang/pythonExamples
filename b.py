#! /usr/bin/python
# -*- coding: utf-8 -*-

from a import add_func

print("Import add_func from module a")
print("Result of 1 plus 2 is: ")
print(add_func(1,2))

'''
	python可以定义module在包里面，但是定义的方式有点奇怪。
	假设我们有一个parent，知道这个文件层次结构，该文件夹有一个child子文件夹，child中有一个module a.py，如何
	让python知道这个文件夹层次结构呢？每个目录里都要放一个名为__init_.py的文件。该文件可以为空。

	Python如何找到包：
		在标准包sys中，path属性记录了Python的包路径，你可以将之打印出来：
'''

import sys
print(sys.path)

'''
	通常我们将module的包路径放到PYTHONPATH中，该环境变量会自动添加到sys.path的属性。另一种方法是编程中直接指定我们的module
	到sys.path中
'''

import os
sys.path.append(os.getcwd()+'/c.py')
sys.path.append(os.getcwd()+'/parent/child')

from c import minus
print(sys.path)
print(minus(10,2))