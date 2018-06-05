import sqlite3
from os import path
ROOT = path.dirname(path.realpath(__file__))


def db_connect():
    con = sqlite3.connect(path.join(ROOT, "cards.db"))
    return con


def query(query, parameters={}):
    connection = db_connect()
    connection.cursor().execute(query, parameters)
    connection.commit()
    connection.close()


def fetch(query, parameters={}):
    connection = db_connect()
    connection.row_factory = to_dictionary
    cur = connection.cursor()
    cur.execute(query, parameters)
    data = cur.fetchall()
    connection.close()
    return data


def get_cards():
    return fetch("SELECT * FROM CARDS")


def insert_card(card_id, card_amount, condition="NM"):
    query("INSERT INTO cards(card_id, amount) VALUES(:id, :amount)",
          {"id": str(card_id) + "-" + condition, "amount": card_amount})


def update_card(card_id, card_amount, condition="NM", price=0, name=""):
    query("UPDATE CARDS SET amount = :amount, current_price=:price, name=:name WHERE card_id = :id",
          {"id": str(card_id) + "-" + condition, "amount": card_amount, "price": price, "name": name})


def delete_card(card_id):
    query("DELETE FROM CARDS WHERE card_id = :card_id", {"card_id": card_id})


def get_card(card_id, condition):
    cards = fetch("SELECT * FROM CARDS WHERE card_id = :card_id", {"card_id": str(card_id) + "-" + condition})
    if cards and len(cards)>0:
        return cards[0]
    else:
        return None


def insert_price(card_id, condition, price):
    query("INSERT INTO prices(card_id, price) VALUES (:id, :price)",
          {"id": str(card_id) + "-" + condition, "price": price})


def to_dictionary(cursor, row):
    return {col[0]: row[index] for index, col in enumerate(cursor.description)}
