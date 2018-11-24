#!/usr/bin/env python
import thread
from time import sleep
import threading

def func():
    print threading.stack_size()

def main():
    lock = thread.allocate_lock()
    lock.acquire()
    if lock.locked():
        print 1
    else:
        print 2
    lock.release()
    if lock.locked():
        print 1
    else:
        print 2
    print threading.activeCount()
    print threading.currentThread()
    print threading.enumerate()
    print threading.stack_size()
    t = threading.Thread(target=func, args=())
    t.start()
    t.join()

if __name__ == '__main__':
    main()
