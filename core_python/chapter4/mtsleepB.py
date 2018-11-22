
# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print 'start loop ', nloop, ' at ', ctime()
    sleep(nsec)
    print 'loop ', nloop, ' done at ', ctime()
    lock.release

def main():
    print 'starting at ', ctime()
    locks = []
    nloops = range(len(loops))

    #给每个线程申请一个锁
    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    #创建线程，以元组的方式传参数
    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    #主进程检查所有线程的锁都被释放了之后，才退出
    for i in nloops:
        while locks[i].locked():
            #pass是一个占位符，相当于C中的TODO
            pass

    print 'all done at ', ctime()

if __name__ == '__main__':
    main()
