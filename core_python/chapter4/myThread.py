
# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    
    #这样很巧妙，若func有返回值的话，可以调用此函数获取
    def getResult(self):
        return self.res

    def run(self):
        print 'starting', self.name, 'at', ctime()
        self.res = self.func(*self.args)
        print self.name, 'finished at', ctime()

