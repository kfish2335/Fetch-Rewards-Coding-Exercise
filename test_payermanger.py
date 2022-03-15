import unittest
from payermanger import payermanger

class Testpayment(unittest.TestCase):
    
    def test_payermanger(self):
        i = payermanger()
        test1 = [
        { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" },
        { "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" },
        { "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" },
        { "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" },
        { "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }
    ]
        result = {'DANNON': {'amount': 1100}, 'UNILEVER': {'amount': 200}, 'MILLER COORS': {'amount': 10000}}
        for t in test1:
            i.updateTransaction( t["payer"], t["points"], t["timestamp"])
        
        val = i.printPlayer()
        self.assertEqual(val, result)
        
        result = [{'payer': 'DANNON', 'points': -100}, {'payer': 'UNILEVER', 'points': -200}, {'payer': 'MILLER COORS', 'points': -4700}]
        val = i.spendPoints(5000)
        self.assertEqual(val, result)
        
        result = {'DANNON': {'amount': 1000}, 'UNILEVER': {'amount': 0}, 'MILLER COORS': {'amount': 5300}}
        val = i.printPlayer()
        self.assertEqual(val, result)
        
        result = [{'payer': 'MILLER COORS', 'points': -5000}]
        val = i.spendPoints(5000)
        self.assertEqual(val, result)
        
        result = "not enough points"
        val = i.spendPoints(5000)
        self.assertEqual(val, result)