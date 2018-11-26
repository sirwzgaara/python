
# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

#使用锁和信号量，锁用来锁I/O
lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

#释放信号量，表示新增一个糖果
def refill():
    lock.acquire()
    print 'Refilling candy...',
    try:
        candytray.release()
    except ValueError:
        print 'full, skipping'
    else:
        print 'OK'
    lock.release()

#获取信号量，表示消耗一个糖果
def buy():
    lock.acquire()
    print 'Buying candy...',
    if candytray.acquire(False):#非阻塞标记False
        print 'OK'
    else:
        print 'empty, skipping'
    lock.release()

#生产者
def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))

#消费者
def consumer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))

def main():
    print 'starting at:', ctime()
    nloops = randrange(2, 6)
    print 'THE CANDY MACHINE (full with %d bars)' % MAX
    Thread(target=consumer, args=(randrange(nloops, nloops + MAX + 2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print 'all DNOE at:', ctime()

if __name__ == '__main__':
    main()
