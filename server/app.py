from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from server.resources.card import Card
from server.resources.stock import Stock

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Card, "/cards")
api.add_resource(Stock, "/stock")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002', debug=True)
