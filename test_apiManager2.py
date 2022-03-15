import requests
import unittest
#Please run unit test in order and have the api running

url = 'http://127.0.0.1:5000'
trans = '/transaction'
spend = '/spendpoints/'
balance = '/balance'

class Testapi(unittest.TestCase):
    
    def test_spend_amount_c(self):
        result = [{'payer': 'DANNON', 'points': -100}, {'payer': 'UNILEVER', 'points': -200}, {'payer': 'MILLER COORS', 'points': -4700}]
        self.assertEqual(requests.put(url+spend+str(5000)).json(), result)
        result = {'DANNON': {'amount': 1000}, 'UNILEVER': {'amount': 0}, 'MILLER COORS': {'amount': 5300}}
        self.assertEqual(requests.get(url+balance).json(), result)