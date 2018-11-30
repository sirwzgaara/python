
# -*- coding: UTF-8 -*-
#!/usr/env/bin python

from socket import *
from time import ctime

HOST = ''               #可以使用任何可用的地址
PORT = 21567            #一个随机的端口号
BUFSIZ = 1024           #缓冲区大小1KB
ADDR = (HOST, PORT)

#建立socket，绑定，监听
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    #默认accept是阻塞的，注意接受连接返回的是一个新的套接字
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        #将client发来的data加上时间发回去
        tcpCliSock.send('[%s] %s' % (ctime(), data))

    tcpCliSock.close()

#关闭socket，永远不会执行
tcpSerSock.close()

