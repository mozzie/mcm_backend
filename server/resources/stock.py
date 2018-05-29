from flask_restful import Resource
from server.db import db
import json


class Stock(Resource):

    def get(self):
        return [card for card in db.get_cards()]