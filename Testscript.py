import requests

#please make sure that the port is correct

url = 'http://127.0.0.1:5000'
trans = '/transaction'
spend = '/spendpoints/'
balance = '/balance'



test1 = [
        { "payer": "DANNON", "amount": 1000, "timestamp": "2020-11-02T14:00:00Z" },
        { "payer": "UNILEVER", "amount": 200, "timestamp": "2020-10-31T11:00:00Z" },
        { "payer": "DANNON", "amount": -200, "timestamp": "2020-10-31T15:00:00Z" },
        { "payer": "MILLER COORS", "amount": 10000, "timestamp": "2020-11-01T14:00:00Z" },
        { "payer": "DANNON", "amount": 300, "timestamp": "2020-10-31T10:00:00Z" },
        { "amount": 300, "timestamp": "2020-10-31T10:00:00Z" },
        { "payer": "DANNON", "timestamp": "2020-10-31T10:00:00Z" },
        { "payer": "DANNON", "amount": 300 }
    ]
for i in test1:
    print(requests.post(url+trans, data = i).text)

print(requests.get(url+balance).text)

test2 = [5000, 1, 2, 3, 4, 1, 10000, 500, 'a']

for i in test2:
    print(requests.put(url+spend+str(i)).text)
    
print(requests.get(url+balance).text)

