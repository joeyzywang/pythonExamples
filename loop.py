#! /usr/bin/python
# -*- coding: utf-8 -*-
x=int(input("Please enter an integer: "))
if x<0:
	x=0
	print("Negative changed to zero")
elif x==0:
	print("Zero")
else:
	print("More")


# Loop list
a=['cat','window','defenestrate']
for x in a :
	print(x,len(x))