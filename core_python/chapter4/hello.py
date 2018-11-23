#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
from time import sleep, ctime

loops = [4, 2]

class mythread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print 'start loop', nloop, 'at', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at', ctime()

def main():
    nloops = range(len(loops))
    threads = []

    for i in nloops:
        t = mythread(loop, (i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all done at', ctime()

if __name__ == '__main__':
    main()
