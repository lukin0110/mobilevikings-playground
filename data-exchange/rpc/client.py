#!/usr/bin/env python
from datetime import datetime
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000/xmlrpc/')

print "\nAvailable method:"
print s.system.listMethods()

print "\nInfo about balance:"
print s.system.methodHelp('balance')

balance = s.balance(34435345)
converted = datetime.strptime(balance['valid_until'].value, "%Y%m%dT%H:%M:%S")
print "\nValid until: ", type(converted), converted

print "\nPing:"
print s.ping()

print "\nCredit:"
print s.addcredit(34435345, 15)
