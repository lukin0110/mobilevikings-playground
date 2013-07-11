#!/usr/bin/env python
import requests
import json


class Client(object):
    url = "http://localhost:8000/rest"

    def __getattr__(self, item):
        def inner(*args, **kwargs):
            payload = json.dumps(kwargs)
            headers = {'content-type': 'application/json'}

            # Some butserij
            response = requests.get(self.url + "/" + item, data=payload, headers=headers)

            if response.status_code == 405:
                response = requests.post(self.url + "/" + item, data=payload, headers=headers)

            return json.loads(response.content)

        return inner


client = Client()

print "\nPing:"
print client.ping()

print "\nBalance:"
print client.balance(msisdn=45454254)

print "\nPortin:"
print client.portin(msisdn=45454254)

print "\nPortout:"
print client.portout(msisdn=45454254)

print "\nAdd credit:"
print client.addcredit(msisdn=99954254, amount=50)
