
# -*- coding: UTF-8 -*-
#!/usr/env/bin python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    #有客户端连接，调用此方法
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from:', clnt
    #收到客户端发来的数据，调用此方法
    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()

