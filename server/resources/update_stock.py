from flask_restful import Resource
from server.db import db
from scripts.db_create import delete
from server.mcm import stock_search
import json


class UpdateStock(Resource):

    def get(self):
        stock = stock_search.get_stock()
        cards = {card['id'] : card for card in db.get_cards()}
        for card in stock['data']:
            if(card['id'] in cards):
                db.update_card_from_csv(card)
                del cards[card['id']]
            else:
                db.insert_card(card)
        for card in cards:
            db.delete_card(card)
        db.close()
        return {'data': db.get_cards(), 'limit': stock['limit']}
