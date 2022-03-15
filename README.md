# Fetch-Rewards-Coding-Exercise

Please write a web service that accepts HTTP requests and returns responses based on the conditions outlined in the next section. You can use any language and frameworks you choose. We must be able to run your web service; provide any documentation necessary to accomplish this as part of the repository you submit. Please assume the reviewer has not executed an application in your language/framework before when developing your documentation.

## Background

Our users have points in their accounts. Users only see a single balance in their accounts. But for reporting purposes we actually track their points per payer/partner. In our system, each transaction record contains: payer (string), points (integer), timestamp (date). For earning points it is easy to assign a payer, we know which actions earned the points. And thus which partner should be paying for the points. When a user spends points, they don't know or care which payer the points come from. But, our accounting team does care how the points are spent. There are two rules for determining what points to "spend" first.

⋅⋅ We want the oldest points to be spent first (oldest based on transaction timestamp, not the order they’re received) 
⋅⋅ We don’t want any payer's points to go negative.

We expect your web service to provide routes that: 

⋅⋅ Add transactions for a specific payer and date. 
⋅⋅ Spend points using the rules above and return a list of { "payer": , "points": } for each call. 
⋅⋅ Return all payer point balances.

## Directions:

This application was written in Python and uses flask as the framework for the api.

To start the server:

Open the command line and move to the Fetch Reward dir.

⋅⋅* Start the virtual environment by entering & env/Scripts/Activate.ps1 into the command line
⋅⋅* Start the program apiManger.py (the port number of your server may be different from the examples, please change the port number before using routes. )
⋅⋅* To stop the server, use the command CTRL+C to shut down the server.

Three routes are provide for use:

### Route: http://127.0.0.1:5000/transaction

This route is for adding payer transactions. Users need to send a POST request in json format with the following argument: payer (string), amount(int), and timestamp(string) in a dictionary. Each transaction is saved by the program. If all these variables are not proved, the api will return an error. If an amount is provided that would set the account below zero, then that amount is set to zero. 

Example:
```
{
    "payer": "DANNON", 
    "amount": 300, 
    "timestamp": "2020-10-31T10:00:00Z"
}
```

### Route: http://127.0.0.1:5000/spendpoints/<int:points>

This route is for spending points using the rules above and returns a list of points sent. Users need to send a PUT request to the above route changing <int:points> to the deserved amount of points to be spent. If there aren't enough points, the api will return a dictionary of the accounts changed and how many points were taken. Points are only spent if there is enough in the accounts. 

Example:

```
http://127.0.0.1:5000/spendpoints/5000
```
### Route: http://127.0.0.1:5000/balance

This route is for getting the balances of all accounts currently recorded by the api. Users need to send a Get request to the above route. It will return a dictionary of account names and current balances in Json format. 

Example:
```
{
    "DANNON": {
    "amount": 1000
  },
  "MILLER COORS": {
    "amount": 4795
  },
  "UNILEVER": {
    "amount": 0
  }
 }
```
