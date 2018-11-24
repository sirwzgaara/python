# -*- coding: UTF-8 -*-
#!/usr/bin/python

#和注册顺序相反
import threading
from time import sleep, ctime
import atexit

def atexitFunc_1():
    print 'I am atexitFunc_1'

def atexitFunc_2(name, age):
    print ('I am atexitFunc_2, %s is %d years old' % (name, age))

print 'I am the first output'

atexit.register(atexitFunc_1)
atexit.register(atexitFunc_2, 'Katherine', 20)

@atexit.register
def atexitFunc_3():
    print 'I am atexitFunc_3'
