import time

class payermanger:

    def __init__(self):
        self.payers = dict()
        self.transaction = list()
        self.wait = False
    
    def __updatePayers(self, payer, amount):
        if payer in self.payers:
            if self.payers[payer]['amount'] + amount < 0:
                amount = -1*self.payers[payer]['amount']
                self.payers[payer]['amount'] = 0
            else:
                self.payers[payer]['amount']+=amount
            return amount
        else:
            if amount < 0:
                self.payers[payer] = {'amount': 0}
                return 0
            else:
                self.payers[payer] = {'amount': amount}
                return amount
    
    
    def updateTransaction(self, payer, amount, timestamp):
        self.transaction.append({'payer': payer, 'amount': self.__updatePayers(payer, amount), 'timestamp': timestamp})
        return None
    
    def printPlayer(self):
        return self.payers 
    
    def spendPoints(self, amount):
        
        while self.wait:
            time.sleep(0.1)
        self.wait = True
        
        self.transaction.sort(key = lambda x: x['timestamp'])
        
        n=0
        limit = len(self.payers)
        visited = {}
        response = []
        count = 0
        
        for x in self.transaction:
            if x['payer'] in visited:
                visited[x['payer']] += x['amount']
            else:
                visited[x['payer']] = x['amount']
            n += x['amount']
            count+=1
            if n >= amount:
                temp = 0
                for i in visited:
                    temp = self.__updatePayers(i, (min(visited[i], amount)*-1))
                    response.append({'payer': i, "points":(temp)})
                    amount += temp
                del self.transaction[:count-1]
                self.transaction[0]['amount']+=temp
                self.wait = False
                return response
            if len(visited) == limit:
                break
        self.wait = False
        return "not enough points"

def main():
    test = payermanger()
    test1 = [
        { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" },
        { "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" },
        { "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" },
        { "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" },
        { "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }
    ]
    for i in test1:
        test.updateTransaction( i["payer"], i["points"], i["timestamp"])
    
    print(test.printPlayer())
    print(test.spendPoints(5000))
    print(test.printPlayer())
    print(test.spendPoints(5000))
    print(test.printPlayer())
    

if __name__ == "__main__":
    main()