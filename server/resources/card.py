from flask_restful import Resource
from flask import request
from server.mcm import card_search
from server.db import db


class Card(Resource):

    def get(self):
        search_word = request.args['search']
        return card_search.get(search_word)

    def post(self):
        args = request.json
        card_id = args['id']
        amount = args['amount']
        condition = args['condition']
        card = db.get_card(card_id, condition)
        if card:
            new_amount = int(card['amount']) + int(amount)
            if new_amount < 1:
                db.delete_card(str(card_id) + "-" + condition)
            else:
                db.update_card(card_id, new_amount, condition, card['name'])
        else:
            db.insert_card(card_id, amount, condition)

