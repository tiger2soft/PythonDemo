#--*-- coding:utf-8 --*--

#1.循环对象
#如下，open()方法返回的就是一个循环对象，循环对象包含next()方法
for line in open('record.txt','r'):
	print line


#2.生成器，用于构建用户自定义循环对象
#定义生成器和定义函数类似，只是把return换成了yield。第一次调用生成器时返回第一个yield后面的值，第二次返回第二个yield后面的值，...依次类推。
def gen():
	a=100
	yield a
	a=a*8
	yield a
	yield 1000
#print gen().next()
#循环获取gen()中的三个yield值
for item in gen():
	print item


#3.表推导，用于快速生成表
L=[]
for x in range(10):
	L.append(x**2)
#可以简写成如下形式
#L=[x**2 for x in range(10)]
print L

#案例：
xl=[1,3,5]
yl=[9,12,13]
L=[x**2 for (x,y) in zip(xl,yl) if y > 10]
print L