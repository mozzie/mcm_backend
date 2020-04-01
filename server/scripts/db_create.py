from server.db.db import db_connect


def main():
    c = db_connect().cursor()
    c.execute("CREATE TABLE IF NOT EXISTS cards("
              "id INTEGER PRIMARY KEY, "
              "product_id INTEGER,"
              "name TEXT, "
              "card_set TEXT, "
              "language TEXT, "
              "condition TEXT, "
              "price INTEGER, "
              "foil INTEGER, "
              "signed INTEGER, "
              "playset INTEGER, "
              "altered INTEGER, "
              "updated INTEGER, "
              "trend_price INTEGER, "
              "edited_mcm INTEGER, "
              "amount INTEGER, "
              "mcm_comment TEXT)")



def delete():
    c = db_connect().cursor()
    c.execute("DROP TABLE cards")


if __name__ == '__main__':
    print("Swiping DB")
    main()
