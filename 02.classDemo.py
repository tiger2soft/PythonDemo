# --*-- coding:utf-8 --*--
#�������Ļ�������

#�Զ���Person�࣬�̳���object��
class Person(object):
	#���캯������������ʱ�Զ�����
	def __init__(self):
		print '���캯��������'
		self.myAttr='�����ڳ�ʼ����������ӵ�����'
	#���е�����name��age
	name='����'
	age=24
	#���ж��巽������һ������self�Ǳ����.
	def move(self,dx,dy):
		position=[0,0]
		position[0]=position[0]+dx
		position[1]=position[1]+dy
		return position
	def eat(self):
		print self.name,'is eatting...'
#�������ʵ��
p=Person()
#���������Ժͷ���
print p.myAttr
print p.name,p.age,'��'
print 'after move:',p.move(5,8)
print p.eat()


#��ļ̳�
class WoMan(Person):
	sex="��"
wm=WoMan()
print wm.sex
