from server.db import db
from server.mcm.prices import Prices


def main():
    for c in db.get_cards():
        c_data = c['card_id'].split("-")
        update_card(c_data[0], c_data[1], c['amount'])


def update_card(card_id, condition, amount):
    prices = Prices()

    mcm_prices = prices.get(int(card_id, 10), condition=condition)
    pricesum = 0.0
    itemsum = 0
    for p in mcm_prices[:5]:
        pricesum += p['price']
        itemsum += p['count'] * 4 if p['isPlayset'] else 1
    new_price = int(100*pricesum/itemsum)
    db.update_card(card_id, amount, condition=condition, price=new_price, name=p['name'])
    db.insert_price(card_id, condition, new_price)


if __name__ == '__main__':
    main()