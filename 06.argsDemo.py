# --*-- coding:utf-8 --*--
#�����Ĳ�������

#1.��������ȷ�������
#���庯��f,������4�����������в���d��Ĭ��ֵΪ10
def func1(a,b,c,d=10):
	return a+b+c+d

#��λ�ô���
print func1(1,2,3,4)
#���ؼ��ִ���
print func1(c=1,b=2,a=3,d=8)
#��Ĭ��ֵ�Ŀ��Բ����ݲ���
print func1(1,2,3)



#2.����������ȷ���������ʹ�ð�������
#(1).����λ�ô���
def func2(*args):
	print args
func2(1,2)
func2(1,2,3,4,5)

#(2).�����ؼ��ִ���
def func3(**args):
	print args
func3(a=2,b=3,c=4,d=5)
#ע��������ݵ����ַ�ʽ������



#3.��������ڲ������õ�ʱ��ʹ��*��**��Ϊ�����
#(1).λ�ý����
def func4(a,b,c):
	print a,b,c
args=(1,2,3)
func4(*args)
#�ؼ��ֽ����
def func5(a,b,c):
	print a,b,c
args={'a':1,'b':2,'c':3}
func5(*args) #�õ�keyֵ
func5(**args) #�õ�valueֵ