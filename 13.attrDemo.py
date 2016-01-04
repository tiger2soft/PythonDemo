#-*- coding:utf-8 -*-

#1.对象的属性
#对象的属性存放在__dict__字典中，键值就是属性的名称
class Bird(object):
	fether = True

class Chicken(Bird):
	fly=False
	def __init__(self,age):
		self.age = age

summer = Chicken(12)
print Bird.__dict__
print Chicken.__dict__
print summer.__dict__



#2.特性
#使用property关键字自定义特性
#property()最多可以加载四个参数，前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。最后一个参数为特性的文档，可以为一个字符串，起说明作用。
class Bird(object):
	fether = True
class Chicken(Bird):
	fly=False
	def __init__(self,age):
		self.age = age
	def getAdult(self):
		if(self.age > 1.0): return True
		else : return False
	adult  = property(getAdult)	#定义特性
summer = Chicken(0.5)
print summer.adult
summer.age = 1.2
print summer.adult

#特性案例：
class num(object):
	def __init__(self,value):
		self.value = value
	def getNeg(self):
		return self.value ** 2
	def setNeg(self,value):
		self.value=value
	def delNeg(self):
		print "value was deleted"
		del self.value
	neg = property(getNeg,setNeg,delNeg,"custom property")
n=num(1)
print n.neg
n.neg=3
print n.value
print n.neg
print n.neg.__doc__
del n.neg



#3.__getattr__(self,name) 函数，用于查询即时生成的属性
#__getattr__只能用来查询不在__dict__系统中的属性
class bird(object):
	fether=False
class chicken(bird):
	fly=True
	def __init__(self,age):
		self.age = age
	def __getattr__(self,name):
		if name == 'adult':
			if(self.age>1.0): return True
			else: return False
		else: raise AttributeError(name)
summer=chicken(1.5)
print summer.adult
summer.age=0.5
print summer.adult

#关于属性的其他函数
#__getattribute__特殊方法，用于查询任意属性
#__setattr__(self, name, value)和__delattr__(self, name)可用于修改和删除属性