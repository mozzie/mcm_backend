from flask_restful import Resource
from flask import request
from server.db import db
from scripts import db_create
from server.mcm import sold_search
import json


class SoldItems(Resource):

    def get(self):
        return db.get_all_sold()
