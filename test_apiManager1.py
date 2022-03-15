import requests
import unittest
#Please run unit test in order and have the api running

url = 'http://127.0.0.1:5000'
trans = '/transaction'
spend = '/spendpoints/'
balance = '/balance'

class Testapi(unittest.TestCase):
    
    def test_transaction_c(self):
        test1 = [
                { "payer": "DANNON", "amount": 1000, "timestamp": "2020-11-02T14:00:00Z" },
                { "payer": "UNILEVER", "amount": 200, "timestamp": "2020-10-31T11:00:00Z" },
                { "payer": "DANNON", "amount": -200, "timestamp": "2020-10-31T15:00:00Z" },
                { "payer": "MILLER COORS", "amount": 10000, "timestamp": "2020-11-01T14:00:00Z" },
                { "payer": "DANNON", "amount": 300, "timestamp": "2020-10-31T10:00:00Z" },
            ]
        result = '"transaction added"\n'
        for i in test1:
            self.assertEqual(requests.post(url+trans, data = i).text, result)

    def test_transaction_e(self):
        test1 = [
                { "payer": "DANNON", "timestamp": "2020-11-02T14:00:00Z" },
                { "payer": "UNILEVER"},
                { "payer": "DANNON", "amount": -200 },
                { "amount": 10000, "timestamp": "2020-11-01T14:00:00Z" },
                { "amount": 300 },
            ]
        result = '"transaction added"\n'
        for i in test1:
            self.assertNotEqual(requests.post(url+trans, data = i).text, result)
    

