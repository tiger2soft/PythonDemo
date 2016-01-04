# --*-- coding:utf-8 --*--
#面向对象的基本概念

#自定义Person类，继承自object类
class Person(object):
	#构造函数，创建对象时自动调用
	def __init__(self):
		print '构造函数被调用'
		self.myAttr='这是在初始函数中新添加的属性'
	#类中的属性name和age
	name='张三'
	age=24
	#类中定义方法，第一个参数self是必须的.
	def move(self,dx,dy):
		position=[0,0]
		position[0]=position[0]+dx
		position[1]=position[1]+dy
		return position
	def eat(self):
		print self.name,'is eatting...'
#创建类的实例
p=Person()
#调用类属性和方法
print p.myAttr
print p.name,p.age,'岁'
print 'after move:',p.move(5,8)
print p.eat()


#类的继承
class WoMan(Person):
	sex="男"
wm=WoMan()
print wm.sex
