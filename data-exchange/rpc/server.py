#!/usr/bin/env python
import datetime
import logging
import xmlrpclib

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

logger = logging.getLogger(__name__)


class FooService:
    """
    Definition of a RPC service, all these methods are exposed
    """
    def ping(self):
        logger.info("Ping requested")
        return "pong"

    def balance(self, msisdn):
        """
        Will fetch the balance of a sim card

        :param msisdn: msisdn number
        :return: dict with the balance
        """
        logger.info("Balance for %s", msisdn)

        # Do magic here ...

        valid_until = datetime.datetime.now() + datetime.timedelta(days=10)
        return {
            'credit': 10.56,
            'currency': 'EUR',
            'valid_until': xmlrpclib.DateTime(valid_until),
            'sms': 2645,
            'data': 2097152  # in bytes
        }

    def portin(self, msisdn):
        logger.info("Porting msisdn %s", msisdn)
        return {
            'status': 'processing'
        }

    def portout(self, msisdn):
        logger.info("Porting out msisn %s", msisdn)
        return "Porting out"

    def addcredit(self, msisdn, amount):
        logger.info('Add %s credit to %s', amount, msisdn)

        class Credit(object):
            def __init__(self, amount, status):
                self.amount = amount
                self.status = status

        return Credit(10, 'done')


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/foo',)


if __name__ == "__main__":
    # Logging to the console
    ch = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    logger.info("Starting RPC server")
    # Create server
    server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_instance(FooService())

    # Run the server's main loop
    server.serve_forever()
