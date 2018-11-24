
# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4, 2]

#继承threading.Thread类的一个子类
class MyThread(threading.Thread):
    def __init__(self, func, args, name = ''):
        #调用父类的初始化函数
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    #重写run方法，使用start创建线程之后，会调用run方法
    def run(self):
        self.func(*self.args)

#线程方法
def loop(nloop, nsec):
    print 'start loop ', nloop, ' at ', ctime()
    sleep(nsec)
    print 'loop ', nloop, ' done at ', ctime()

def main():
    print 'starting at ', ctime()
    threads = []
    nloops = range(len(loops))

    #创建threading.Thread的子类的实例
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    #创建线程
    for i in nloops:
        threads[i].start()

    #主线程等待所有线程结束
    for i in nloops:
        threads[i].join()

    print 'all done at ', ctime()

if __name__ == '__main__':
    main()

