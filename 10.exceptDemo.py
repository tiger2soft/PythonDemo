#--*-- coding:utf-8 --*--
#�쳣����

#1.�����쳣
#����1��
re = iter(range(5))
try:
    for i in range(100):
        print re.next()
except StopIteration:
    print 'here is end ',i
print 'HaHaHaHa'


#����2��
try:
    print a*2
except TypeError:
    print "TypeError"
except NameError:
	print "NameError"
except:
    print "OtherError"


#����3��
f=open('record.txt','w')
try:
	print f.read(5)
except:
	print '���ļ��쳣'
finally:
	f.close()



#2.�׳��쳣
print 'aaaaaaaaaa'
raise ZeroDivisionError
print 'bbbbbbbbbb'

