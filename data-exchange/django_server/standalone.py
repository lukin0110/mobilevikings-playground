#!/usr/bin/env python
import logging
import sys

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
sys.path.append('server')
from server import service

logger = logging.getLogger(__name__)


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/xmlrpc/',)


if __name__ == "__main__":
    # Logging to the console
    ch = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    logger.info("Starting RPC server")
    # Create server
    server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_instance(service.FooService())

    # Run the server's main loop
    server.serve_forever()
