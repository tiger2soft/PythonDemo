#--*-- coding:utf-8 --*--

#1.ѭ������
#���£�open()�������صľ���һ��ѭ������ѭ���������next()����
for line in open('record.txt','r'):
	print line


#2.�����������ڹ����û��Զ���ѭ������
#�����������Ͷ��庯�����ƣ�ֻ�ǰ�return������yield����һ�ε���������ʱ���ص�һ��yield�����ֵ���ڶ��η��صڶ���yield�����ֵ��...�������ơ�
def gen():
	a=100
	yield a
	a=a*8
	yield a
	yield 1000
#print gen().next()
#ѭ����ȡgen()�е�����yieldֵ
for item in gen():
	print item


#3.���Ƶ������ڿ������ɱ�
L=[]
for x in range(10):
	L.append(x**2)
#���Լ�д��������ʽ
#L=[x**2 for x in range(10)]
print L

#������
xl=[1,3,5]
yl=[9,12,13]
L=[x**2 for (x,y) in zip(xl,yl) if y > 10]
print L