#--*-- coding:utf-8 --*--
#ѭ������

#1.range(start,stop,step)
str='abcdefghijklmn'
for i in range(0,len(str),1):
	print str[i]

#2.enumerage()
#ͬʱ��ȡ���к�ֵ
for (index,value) in enumerate(str):
	print index,'->',value

#3.zip()
#ͬʱ����������У�������ͬλ�õ�Ԫ����ϳ�һ���µ�Ԫ�飻���������Ԫ�ص���Ŀ��һ�����Ը������ٵ��Ǹ�Ϊ׼������ֻ���������Ԫ��
ta=[1,2,3]
tb=[4,5]
tc=['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
	print (a,b,c)

#�ֽ�ۺϺ��Ԫ���б�
ta=[1,2,3]
tb=[4,5,6]
zipped=zip(ta,tb) #�ۺ�
print zipped
na,nb=zip(*zipped) #�ֽ�
print na,nb