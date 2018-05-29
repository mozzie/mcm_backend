from flask_restful import Resource
from flask import request
from server.mcm.card_search import CardSearch
from server.db import db


class Card(Resource):

    def get(self):
        search_word = request.args['search']
        return CardSearch.get(search_word)

    def put(self):
        args = request.json
        card_id = args['id']
        amount = args['amount']
        condition = args['condition']
        db.insert_card(card_id, amount, condition)

    def post(self):
        args = request.json
        card_id = args['id']
        amount = args['amount']
        condition = args['condition']
        db.update_card(card_id, amount, condition)
