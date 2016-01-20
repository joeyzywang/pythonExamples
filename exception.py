#! /usr/bin/python
# -*- coding: utf-8 -*-

s=input("Input your name: ")
if s=="":
	raise Exception("Input must not be empty.")

try:
	i=int(s)
except Exception as err:
	print("Get exception when int()")
	print(err)
finally:
	print("Goodbye!")