# -*- coding: UTF-8 -*-
#!usr/local/env python

import thread
from time import sleep, ctime

def loop0():
    print 'start loop0 at ', ctime()
    sleep(4)
    print 'loop0 done at ', ctime()

def loop1():
    print 'start loop1 at ', ctime()
    sleep(2)
    print 'loop1 done at ', ctime()

def main():
    print 'start at ', ctime()
    #thread模块核心函数，传入函数或者对象，参数使用元组，这里没有参数
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all done at ', ctime()

if __name__ == '__main__':
    main()
