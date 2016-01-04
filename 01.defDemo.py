#coding:utf-8
#第一句用来设置编码，不设置时有中文会无法运行

#按值传递
def change_integer(a):
	a=a+1
	return a
a=1
print change_integer(a)
print a

#按引用传递
def change_list(b):
	b[0]=b[0]+1
	return b
b=[1,2,3]
print change_list(b) 
print b