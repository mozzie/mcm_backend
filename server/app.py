from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from server.resources.stock import Stock
from server.resources.update_stock import UpdateStock
app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Stock, "/stock")
api.add_resource(UpdateStock, "/update")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002', debug=True)
