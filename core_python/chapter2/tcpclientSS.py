
# -*- coding: UTF-8 -*-
#!/usr/env/bin python

from socket import *
HOST = '10.1.108.52'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

#SocketServer默认是短连接，每次都新建连接，最后断开
while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()

