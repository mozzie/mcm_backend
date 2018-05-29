from server.db import db
from server.mcm.prices import Prices


def main():
    prices = Prices()
    for c in db.get_cards():
        c_data = c['card_id'].split("-")
        mcm_prices = prices.get(int(c_data[0], 10), condition=c_data[1])
        pricesum = 0.0
        itemsum = 0
        for p in mcm_prices[:5]:
            pricesum += p['price']
            itemsum += p['count'] * 4 if p['isPlayset'] else 1
        new_price = int(100*pricesum/itemsum)
        db.update_card(c_data[0], c['amount'], condition=c_data[1], price=new_price)
        db.insert_price(c_data[0], c_data[1], new_price)


if __name__ == '__main__':
    main()