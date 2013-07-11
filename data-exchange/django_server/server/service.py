import datetime
import logging
import xmlrpclib

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
            # 'valid_until': xmlrpclib.DateTime(valid_until),
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

    def addcredit(self, msisdn, amount=10):
        logger.info('Add %s credit to %s', amount, msisdn)

        class Credit(object):
            def __init__(self, amount, msisdn, status):
                self.amount = amount
                self.msisdn = msisdn
                self.status = status

        return Credit(amount, msisdn, 'done')
