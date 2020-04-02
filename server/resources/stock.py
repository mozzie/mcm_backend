from flask_restful import Resource
from flask import request
from server.db import db
from scripts import db_create
from server.mcm import stock_search
import json


class Stock(Resource):

    def get(self):
#        delete()
        orderfield = request.args.get('sort', default="name")
        sortorder = request.args.get('order', default="ASC")
        if(orderfield not in ['name', 'price', 'trend_price', 'trend_diff']):
            orderfield = 'name'
        if(sortorder not in ['ASC', 'DESC']):
            sortorder = 'ASC'
        db_create.main()
        #return stock_search.get()
        return db.get_cards(orderfield, sortorder)
