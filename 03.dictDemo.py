# --*-- coding:utf-8 --*--
#×Öµä
dic={'tom':11,'jack':23,'zhangsan':'28','wangwu':32}
for key in dic:
	print key,'->',dic[key]

print len(dic)
print dic.keys()
print dic.values()
print dic.items()

del dic['zhangsan']
print dic.items()

dic.clear()
print len(dic)