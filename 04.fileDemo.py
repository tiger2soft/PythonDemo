# --*-- coding:utf-8 --*--
#��д�ı��ļ�

#���ļ�
f=open('record.txt','r')
#��ȡn���ֽ�
content = f.read(3)
print content
#��ȡһ��
content = f.readline()
print content
#��ȡ������
content=f.readlines()
for line in content:
	print line
#�ر��ļ�
f.close()

f=open('record.txt','w')
#д���ļ�
f.write('Hello Python!')
f.close()