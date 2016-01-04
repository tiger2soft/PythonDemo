#--*-- coding:utf-8 --*--
#上下文对象
#用于规定某个对象的使用范围。一旦进入或者离开该使用范围，会有特殊操作被调用 (比如为对象分配或者释放内存)。它的语法形式是with...as...

#如下，读取文件后会自动关闭文件，不需要显式的调用f.close()方法：
with open('record.txt','w') as f:
	print f.closed
	f.write('Hello World!!!')
print f.closed



#2.自定义上下文对象
#任何定义了__enter__()和__exit__()方法的对象都可以用于上下文管理器
#案例：
class MyClass(object):
	def __init__(self,name):
		self.content=name
	def __enter__(self):
		self.content= 'Welcome ' + self.content
		return self
	def __exit__(self,exc_type,exc_value,traceback): # exc_type,exc_value,traceback 这三个参数用于描述异常，如果运行正常都为None
		self.content = 'Goodbye!'
with MyClass('张三') as m:
	print m.content
print m.content
