
# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4, 2]

#使用类作为线程入口
class ThreadFunc(object):
    def __init__(self, func, args, name = ''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print 'start loop ', nloop, ' at ', ctime()
    sleep(nsec)
    print 'loop ', nloop, ' done at ', ctime()

def main():
    print 'starting at ', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        #传递对象作为线程参数
        t = threading.Thread(target = ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    #在这里才会调用每个对象，而不是创建线程的时候
    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all done at ', ctime()

if __name__ == '__main__':
    main()
