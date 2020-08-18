from flask_restful import Resource
from flask import request
from server.db import db
from scripts import db_create
from server.mcm import sold_search
import json


class SoldItems(Resource):

    def get(self):
        orderfield = request.args.get('sort', default="name")
        sortorder = request.args.get('order', default="ASC")
        if(orderfield not in ['name', 'price', 'mcm_comment', 'timestamp']):
            orderfield = 'name'
        if(sortorder not in ['ASC', 'DESC']):
            sortorder = 'ASC'
        return db.get_all_sold(orderfield, sortorder)
