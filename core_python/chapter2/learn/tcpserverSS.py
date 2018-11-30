
# -*- coding: UTF-8 -*-
#!/usr/env/bin python

from SocketServer import (TCPServer as TCP,
        StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    #在基类中，这个方法没有任何行为，需要根据用途重写
    def handle(self):
        print '...connected from:', self.client_address
        #数据是用文件的方式
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()

