#--*-- coding:utf-8 --*--

#1.使用lambda创建函数对象
func=lambda x,y:x+y
print func(1,2)
#以上代码等同于：
#def func(x,y):
#	return x+y


#2.将函数对象作为参数传递
def test(f,a,b):
	print '调用func的结果:',f(a,b)
test(func,2,3)
#test((lambda x,y:x+y),3,4)


#3.map()函数，将函数对象依次作用于表的每一个元素
re=map((lambda x:x**2),[2,3])
print re
#多个参数，多个列表的元素个数必须一样
re=map((lambda x,y:x+y),[1,2,3],[4,5,6])
print re


#4.filter()函数，将作为参数的函数对象作用于多个元素，如果函数对象返回True,则将该次传入的元素存储于返回的列表中
def func(a):
	if a > 10:
		return True
	else:
		return False
result = filter(func,[3,11,7,15,18])
print result


#5.reduce()函数，累进的将函数作用于给个参数
print reduce((lambda x,y:x+y),[1,2,3,4,5])
#执行过程相当于(((1+2)+5)+7)+9