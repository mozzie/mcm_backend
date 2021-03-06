from flask_restful import Resource
from server.db import db
from scripts.db_create import delete
from server.mcm import product_search
import json


class UpdateTrends(Resource):

    def get(self):
        limit = None
        not_updated_cards = db.get_not_updated_cards()
        for card in not_updated_cards:
            product = product_search.get_product(card['product_id'])
            limit = product['limit']
            prices = product['data']['product']['priceGuide']
            price = 100*prices['TRENDFOIL'] if card['foil'] == 1 else 100 * prices['TREND']
            if card['playset'] == 1:
                price = price * 4
            db.update_card(card['id'], price)
        return {"data": db.get_cards(), "limit": limit}
