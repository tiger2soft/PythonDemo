#--*-- coding:utf-8 --*--
#异常处理

#1.捕获异常
#案例1：
re = iter(range(5))
try:
    for i in range(100):
        print re.next()
except StopIteration:
    print 'here is end ',i
print 'HaHaHaHa'


#案例2：
try:
    print a*2
except TypeError:
    print "TypeError"
except NameError:
	print "NameError"
except:
    print "OtherError"


#案例3：
f=open('record.txt','w')
try:
	print f.read(5)
except:
	print '读文件异常'
finally:
	f.close()



#2.抛出异常
print 'aaaaaaaaaa'
raise ZeroDivisionError
print 'bbbbbbbbbb'

