# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import thread
from time import sleep
import threading
from random import randrange
from atexit import register
from Queue import Queue

def writeQ(queue):
    for i in range(100):
        tmp = queue.get(True)
        queue.put(tmp + 1, True)

def readQ(queue):
    for i in range(100):
        tmp = queue.get(True)
        queue.put(tmp + 1, True)

def main():
    q = Queue(32)
    q.put(0, True)
    threading.Thread(target=writeQ, args = (q,)).start()
    threading.Thread(target=readQ, args = (q,)).start()
    sleep(2)
    print q.get(True)

if __name__ == '__main__':
    main()
