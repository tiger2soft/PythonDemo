#--*-- coding:utf-8 --*--
#循环处理

#1.range(start,stop,step)
str='abcdefghijklmn'
for i in range(0,len(str),1):
	print str[i]

#2.enumerage()
#同时获取所有和值
for (index,value) in enumerate(str):
	print index,'->',value

#3.zip()
#同时遍历多个序列，并把相同位置的元素组合成一个新的元组；如果序列中元素的数目不一样，以个数最少的那个为准，如下只会输出两个元组
ta=[1,2,3]
tb=[4,5]
tc=['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
	print (a,b,c)

#分解聚合后的元组列表
ta=[1,2,3]
tb=[4,5,6]
zipped=zip(ta,tb) #聚合
print zipped
na,nb=zip(*zipped) #分解
print na,nb