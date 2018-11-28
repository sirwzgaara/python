
# -*- coding: UTF-8 -*-
#!/usr/env/bin python

from twisted.internet import protocol, reactor

HOST = '10.1.108.52'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = naw_input('> ')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()

class TSClntFacotry(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
            lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()

