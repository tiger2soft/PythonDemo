# --*-- coding:utf-8 --*--
#函数的参数传递

#1.参数个数确定的情况
#定义函数f,并包含4个参数，其中参数d的默认值为10
def func1(a,b,c,d=10):
	return a+b+c+d

#按位置传递
print func1(1,2,3,4)
#按关键字传递
print func1(c=1,b=2,a=3,d=8)
#含默认值的可以不传递参数
print func1(1,2,3)



#2.参数个数不确定的情况，使用包裹传递
#(1).包裹位置传递
def func2(*args):
	print args
func2(1,2)
func2(1,2,3,4,5)

#(2).包裹关键字传递
def func3(**args):
	print args
func3(a=2,b=3,c=4,d=5)
#注意包裹传递的两种方式的区别



#3.解包裹，在参数调用的时候使用*或**称为解包裹
#(1).位置解包裹
def func4(a,b,c):
	print a,b,c
args=(1,2,3)
func4(*args)
#关键字解包裹
def func5(a,b,c):
	print a,b,c
args={'a':1,'b':2,'c':3}
func5(*args) #得到key值
func5(**args) #得到value值