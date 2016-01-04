# --*-- coding:utf-8 --*--
#读写文本文件

#打开文件
f=open('record.txt','r')
#读取n个字节
content = f.read(3)
print content
#读取一行
content = f.readline()
print content
#读取所有行
content=f.readlines()
for line in content:
	print line
#关闭文件
f.close()

f=open('record.txt','w')
#写入文件
f.write('Hello Python!')
f.close()