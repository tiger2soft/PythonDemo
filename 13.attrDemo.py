#-*- coding:utf-8 -*-

#1.���������
#��������Դ����__dict__�ֵ��У���ֵ�������Ե�����
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



#2.����
#ʹ��property�ؼ����Զ�������
#property()�����Լ����ĸ�������ǰ��������Ϊ�������ֱ����ڴ����ѯ���ԡ��޸����ԡ�ɾ�����ԡ����һ������Ϊ���Ե��ĵ�������Ϊһ���ַ�������˵�����á�
class Bird(object):
	fether = True
class Chicken(Bird):
	fly=False
	def __init__(self,age):
		self.age = age
	def getAdult(self):
		if(self.age > 1.0): return True
		else : return False
	adult  = property(getAdult)	#��������
summer = Chicken(0.5)
print summer.adult
summer.age = 1.2
print summer.adult

#���԰�����
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



#3.__getattr__(self,name) ���������ڲ�ѯ��ʱ���ɵ�����
#__getattr__ֻ��������ѯ����__dict__ϵͳ�е�����
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

#�������Ե���������
#__getattribute__���ⷽ�������ڲ�ѯ��������
#__setattr__(self, name, value)��__delattr__(self, name)�������޸ĺ�ɾ������