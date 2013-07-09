#!/usr/bin/env python
 
import sys
sys.path.append('gen-py')
 
from foo import FooService
from foo.ttypes import *
from foo.constants import *
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    # Make socket
    transport = TSocket.TSocket('localhost', 30303)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = FooService.Client(protocol)

    # Connect!
    transport.open()

    print "\nPinging ..."
    print client.ping()

    print "\nBalance ..."
    print client.balance(4545457)

    print "\nPortin ..."
    print client.portin(4545457)

    print "\nAdd credit ..."
    print client.addcredit(545454, 25)

    transport.close()
 
except Thrift.TException, tx:
    import traceback
    print traceback.format_exc()
    print "%s" % (tx.message)