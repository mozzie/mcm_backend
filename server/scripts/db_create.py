from server.db.db import db_connect

def main():
    c = db_connect().cursor()
    c.execute("CREATE TABLE IF NOT EXISTS CARDS("
              "id INTEGER PRIMARY KEY, "
              "product_id INTEGER,"
              "name VARCHAR(255), "
              "card_set VARCHAR(10), "
              "language VARCHAR(10), "
              "cond VARCHAR(10), "
              "price INTEGER, "
              "foil INTEGER, "
              "signed INTEGER, "
              "playset INTEGER, "
              "altered INTEGER, "
              "updated INTEGER, "
              "trend_price INTEGER, "
              "edited_mcm INTEGER, "
              "amount INTEGER, "
              "mcm_comment VARCHAR(255), "
  	      "KEY `card_name` (`name`), "
              "KEY `card_price` (`price`), "
              "KEY `card_trend` (`trend_price`), "
              "KEY `card_comment` (`mcm_comment`))")

    c.execute("CREATE TABLE IF NOT EXISTS SOLD("
              "id INTEGER PRIMARY KEY, "
              "product_id INTEGER,"
              "name VARCHAR(255), "
              "card_set VARCHAR(30), "
              "language VARCHAR(10), "
              "cond VARCHAR(10), "
              "price INTEGER, "
              "foil INTEGER, "
              "signed INTEGER, "
              "playset INTEGER, "
              "altered INTEGER, "
              "amount INTEGER, "
              "mcm_comment VARCHAR(255), "
  	      "KEY `card_name` (`name`), "
              "KEY `card_price` (`price`), "
              "KEY `card_comment` (`mcm_comment`))")

    db_connect().commit()
    db_connect().close()

def delete():
    c = db_connect().cursor()
    c.execute("DROP TABLE cards")


if __name__ == '__main__':
    print("Swiping DB")
    main()
