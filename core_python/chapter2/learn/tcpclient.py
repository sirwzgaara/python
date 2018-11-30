
# -*- coding: UTF-8 -*-
#!/usr/env/bin python

from socket import *

HOST = '10.1.108.52'        #服务器地址
PORT = 21567                #服务器端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    #用户没有输入，也就是直接敲enter的时候，退出客户端
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()

