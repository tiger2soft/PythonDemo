#coding:utf-8
#��һ���������ñ��룬������ʱ�����Ļ��޷�����

#��ֵ����
def change_integer(a):
	a=a+1
	return a
a=1
print change_integer(a)
print a

#�����ô���
def change_list(b):
	b[0]=b[0]+1
	return b
b=[1,2,3]
print change_list(b) 
print b