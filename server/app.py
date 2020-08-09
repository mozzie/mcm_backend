from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from server.resources.stock import Stock
from scripts import db_create
from server.resources.update_stock import UpdateStock
from server.resources.update_trends import UpdateTrends
from server.resources.sold_items import SoldItems
from server.resources.update_sold import UpdateSold
app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Stock, "/stock")
api.add_resource(UpdateStock, "/update")
api.add_resource(UpdateTrends, "/trends")
api.add_resource(SoldItems, "/sold")
api.add_resource(UpdateSold, "/updatesold")

if __name__ == '__main__':
    db_create.main()
    app.run(host='0.0.0.0', port='5002', debug=True)
