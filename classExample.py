
class Base:
	def __init__(self):
		self.data=[]
	def add(self,x):
		self.data.append(x)
	def addtwice(self,x):
		self.add(x)
		self.add(x)

class Child(Base):
	def plus(self,a,b):
		return a+b


oChild = Child()
oChild.add("str1")
print(oChild.data)
oChild.addtwice("str2")
print(oChild.data)
s=oChild.plus(1,2)
print(s)

'''
	知识点：
		类成员必须以self作为第一个参数
		self类似java的this
'''