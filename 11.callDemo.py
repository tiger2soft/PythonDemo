#--*-- coding:utf-8 --*--
#特殊方法
#特殊方法的前后都有__ ，如__init__()

#任何一个有__call__()特殊方法的对象都被当作是函数
class SampleMore(object):
	def __call__(self,a):
		return a+5
add=SampleMore()
print add(2)
print map(add,[2,3,4])