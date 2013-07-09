#!/usr/bin/env python
 
import sys
sys.path.append('gen-py')

from foo import FooService
from foo.ttypes import *
 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
 
import socket
"""
service FooService {
    Portout portout(1: i32 msisdn),
    map<string, string> addcredit(1: i32 msisdn, 2: i32 amount),
}


"""


class FooServiceHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print "ping requested\n"
        return "Pong"

    def balance(self, msisdn):
        print "balance requested\n"
        return Balance(credit=15.0, currency='EUR')

    def portin(self, msisdn):
        print "portin requested\n"
        return {
            "status": "ok"
        }

    def portout(self, msisdn):
        print "portout request\n"
        return Portout(status="ok")

    def addcredit(self, msisdn, amount):
        print "addcredit requested\n"
        return {
            "status": "ok",
            "credit": str(amount),
            "msisdn": str(msisdn)
        }

handler = FooServiceHandler()
processor = FooService.Processor(handler)
transport = TSocket.TServerSocket('localhost', 30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
 
print "Starting python server..."
server.serve()
print "done!"