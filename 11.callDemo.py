#--*-- coding:utf-8 --*--
#���ⷽ��
#���ⷽ����ǰ����__ ����__init__()

#�κ�һ����__call__()���ⷽ���Ķ��󶼱������Ǻ���
class SampleMore(object):
	def __call__(self,a):
		return a+5
add=SampleMore()
print add(2)
print map(add,[2,3,4])