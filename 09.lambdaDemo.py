#--*-- coding:utf-8 --*--

#1.ʹ��lambda������������
func=lambda x,y:x+y
print func(1,2)
#���ϴ����ͬ�ڣ�
#def func(x,y):
#	return x+y


#2.������������Ϊ��������
def test(f,a,b):
	print '����func�Ľ��:',f(a,b)
test(func,2,3)
#test((lambda x,y:x+y),3,4)


#3.map()�������������������������ڱ��ÿһ��Ԫ��
re=map((lambda x:x**2),[2,3])
print re
#�������������б��Ԫ�ظ�������һ��
re=map((lambda x,y:x+y),[1,2,3],[4,5,6])
print re


#4.filter()����������Ϊ�����ĺ������������ڶ��Ԫ�أ�����������󷵻�True,�򽫸ôδ����Ԫ�ش洢�ڷ��ص��б���
def func(a):
	if a > 10:
		return True
	else:
		return False
result = filter(func,[3,11,7,15,18])
print result


#5.reduce()�������۽��Ľ����������ڸ�������
print reduce((lambda x,y:x+y),[1,2,3,4,5])
#ִ�й����൱��(((1+2)+5)+7)+9