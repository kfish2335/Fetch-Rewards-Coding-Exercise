from payermanger import payermanger
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

test = payermanger()
inputArgs = reqparse.RequestParser()
inputArgs.add_argument("payer", type=str, help = "Invalid argument! Expected: payer of type str", required=True)
inputArgs.add_argument("amount", type=int, help = "Invalid argument! Expected: amount of type int",required=True )
inputArgs.add_argument("timestamp", type=str, help = "Invalid argument! Expected: timestamp of type str", required=True)

def check_if_int(x):
    if type(x) is not int:
        abort("This not an int value!")

class transactions(Resource):
    def post(self):
        args = inputArgs.parse_args()
        test.updateTransaction( args["payer"], args["amount"], args["timestamp"])
        return 'transaction added', 201

class payerBalance(Resource):
    def get(self):
        return jsonify(test.printPlayer())

class spendPoints(Resource):
    def put(self, points):
        check_if_int(points)
        return jsonify(test.spendPoints(points))
        


api.add_resource(transactions, '/transaction')
api.add_resource(payerBalance, '/balance')
api.add_resource(spendPoints, '/spendpoints/<int:points>')

if __name__ == '__main__':
    app.run(debug = True)