# -*- coding: UTF-8 -*-
__author__ = 'wz'
#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print 'start loop ', nloop, ' at ', ctime()
    sleep(nsec)
    print 'loop ', nloop, ' done at ', ctime()

def main():
    print 'starting at ', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        #threading模块创建线程的方法
        t = threading.Thread(target = loop, args = (i, loops[i]))
        threads.append(t)

    #启动线程
    for i in nloops:
        threads[i].start()

    #主进程等待所有线程结束
    for i in nloops:
        threads[i].join()

    print 'all done at ', ctime()

if __name__ == '__main__':
    main()
