
# -*- coding: UTF-8 -*-
#!/usr/env/bin python

from twisted.internet import protocol, reactor

HOST = '10.1.108.52'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    #私有方法，建立连接后调用此函数发送数据
    def sendData(self):
        data = raw_input('> ')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()
    #重写此方法，建立连接后调用
    def connectionMade(self):
        self.sendData()
    #重写此方法，接收数据后调用
    def dataReceived(self, data):
        print data
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
            lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()

