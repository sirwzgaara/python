
# -*- coding: UTF-8 -*-
#!/usr/env/bin python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
#UDP不需要监听，但是仍然要绑定端口
udpSerSock.bind(ADDR)

while (True):
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    #udp没有连接，需要指定地址
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print '---received from and returned to', addr

udpSerSock.close()

