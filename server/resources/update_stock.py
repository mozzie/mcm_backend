from flask_restful import Resource
from server.db import db
from scripts.db_create import delete
from server.mcm import stock_search
from server.mcm import product_search
import json


class UpdateStock(Resource):

    def get(self):
        stock = stock_search.get_stock()
        cards = {card['id'] : card for card in db.get_cards()}
        for card in stock:
            if(card['id'] in cards):
                db.update_card_from_csv(card)
                del cards[card['id']]
            else:
                db.insert_card(card)
        for card in cards:
            db.delete_card(card)
        not_updated_cards = db.get_not_updated_cards()
        for card in not_updated_cards:
            if card['price'] > 99:
                product = product_search.get_product(card['product_id'])
                prices = product['product']['priceGuide']
                db.update_card(card['id'], 100*prices['TRENDFOIL'] if card['foil']==1 else 100*prices['TREND'])
        return db.get_cards()
        #return [card for card in db.get_cards()]
