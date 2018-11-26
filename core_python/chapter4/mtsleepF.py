
# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime

#继承set的子类，重写打印的__str__方法
class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
#两次随机，第一次随机个数，然后每个都是一个随机数，得到的loops是一个生成器
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    #加锁，锁set和I/O
    lock.acquire()
    remaining.add(myname)
    print '[%s] Started %s' % (ctime(), myname)
    #睡眠之前要释放锁
    lock.release()
    sleep(nsec)
    #再次加锁，锁set和I/O，使用with lock的方式，2.5以上版本支持
    with lock:
        remaining.remove(myname)
        print '[%s] completed %s(%d secs)' % (ctime(), myname, nsec)
        print '     (remaining: %s)' % (remaining or 'NONE')

def main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
