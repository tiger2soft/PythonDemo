#--*-- coding:utf-8 --*--
#�����Ķ���
#���ڹ涨ĳ�������ʹ�÷�Χ��һ����������뿪��ʹ�÷�Χ������������������� (����Ϊ�����������ͷ��ڴ�)�������﷨��ʽ��with...as...

#���£���ȡ�ļ�����Զ��ر��ļ�������Ҫ��ʽ�ĵ���f.close()������
with open('record.txt','w') as f:
	print f.closed
	f.write('Hello World!!!')
print f.closed



#2.�Զ��������Ķ���
#�κζ�����__enter__()��__exit__()�����Ķ��󶼿������������Ĺ�����
#������
class MyClass(object):
	def __init__(self,name):
		self.content=name
	def __enter__(self):
		self.content= 'Welcome ' + self.content
		return self
	def __exit__(self,exc_type,exc_value,traceback): # exc_type,exc_value,traceback �������������������쳣���������������ΪNone
		self.content = 'Goodbye!'
with MyClass('����') as m:
	print m.content
print m.content
