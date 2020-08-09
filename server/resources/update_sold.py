from flask_restful import Resource
from server.db import db
from scripts.db_create import delete
from server.mcm import sold_search
import json


class UpdateSold(Resource):

    def get(self):
        start = 1
        l = []
        for start in range(1,10000000, 100):
            stock = sold_search.get_sold(start)
            orders = stock['data']['data']['order']
            for order in orders:
                for article in order['article']:
                    item = self.get_card(article)
                    print(item)
                    if db.get_sold(item['id']) is None:
                        db.insert_sold(item)
                    else:
                        db.close()
                        return db.get_sold()
            print(len(orders))
            if len(orders) < 100:
                db.close()
                return db.get_all_sold()

    def get_card(self, obj):
        return {
            "id": obj['idArticle'],
            "product_id": obj['idProduct'],
            "name": obj['product']['enName'],
            "card_set": obj['product'].get('expansion', "n/a"),
            "language": obj['language']['languageName'],
            "cond": obj.get('condition', "n/a"),
            "price": obj['price'],
            "foil": obj.get('isFoil', 0),
            "signed": obj.get('isSigned', 0),
            "playset": obj.get('isPlayset', 0),
            "altered": obj.get('isAltered', 0),
            "amount": obj['count'],
            "mcm_comment": obj['comments']
        }
