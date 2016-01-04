# --*-- coding:utf-8 --*--
#引用first.py模块
import first
#import first as a	#也可以用这种形式

#引用模块包中的模块
import modules.second as sec

for i in range(10):
	first.showHello()

for i in range(10):
	sec.speak()