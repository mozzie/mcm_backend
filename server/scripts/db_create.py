from server.db.db import db_connect


def main():
    c = db_connect().cursor()
    c.execute("CREATE TABLE IF NOT EXISTS cards("
              "card_id TEXT PRIMARY KEY, name TEXT,"
              "amount INTEGER, "
              "current_price INTEGER)")

    c.execute("CREATE TABLE IF NOT EXISTS prices("
              "id INTEGER PRIMARY KEY AUTOINCREMENT,"
              "card_id TEXT NOT NULL,"
              "price INTEGER NOT NULL,"
              "timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,"
              "FOREIGN KEY(card_id) REFERENCES cards(card_id))")


def delete():
    c = db_connect().cursor()
    c.execute("DROP TABLE prices")
    c.execute("DROP TABLE cards")


if __name__ == '__main__':
  #  delete()
    main()
