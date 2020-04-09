from mysql import connector
from os import path
ROOT = path.dirname(path.realpath(__file__))
import time


def db_connect():
#    con = sqlite3.connect(path.join(ROOT, "cards.db"))
    con = connector.connect(host='localhost',
                            database='db',
                            user='user',
                            password='pass')
    return con


def query(query, parameters={}):
    connection = db_connect()
    connection.cursor().execute(query, parameters)
    connection.commit()
    connection.close()


def fetch(query, parameters={}):
    connection = db_connect()
    connection.row_factory = to_dictionary
    connection.set_trace_callback(print)
    cur = connection.cursor()
    cur.execute(query, parameters)
    data = cur.fetchall()
    connection.close()
    return data


def get_cards(orderfield = "name", direction = "ASC"):
    if orderfield == 'trend_diff':
        orderfield = "(price - trend_price)"
    return fetch("SELECT * FROM CARDS ORDER BY {}".format(orderfield + " " + direction))

def get_not_updated_cards():
    timestamp = int(time.time()) - 60*60*24*7
    return fetch("SELECT * FROM CARDS WHERE updated IS null OR updated < :time",  {"time": timestamp})

def insert_card(card):
    query("INSERT INTO cards(id, product_id, name, card_set, price, language, cond, foil, signed, playset, altered, mcm_comment, amount) VALUES(:id, :product_id, :name, :card_set, :price, :language, :condition, :foil, :signed, :playset, :altered, :mcm_comment, :amount)",
          card)


def update_card(card_id, trend_price):
    query("UPDATE CARDS SET trend_price=:price, updated = :stamp WHERE id = :id",
          {"id": card_id, "price": trend_price, "stamp": int(time.time())})

def update_card_from_csv(card):
    card.update({"stamp":int(time.time())})
    query("UPDATE CARDS SET language=:language,cond=:condition,foil=:foil,signed=:signed,playset=:playset,altered=:altered,mcm_comment=:mcm_comment, amount=:amount, price=:price, updated = :stamp WHERE id = :id",
          card)


def delete_card(card_id):
    query("DELETE FROM CARDS WHERE id = :card_id", {"card_id": card_id})


def get_card(card_id):
    cards = fetch("SELECT * FROM CARDS WHERE id = :card_id", {"card_id": card_id})
    if cards and len(cards)>0:
        return cards[0]
    else:
        return None

def to_dictionary(cursor, row):
    return {col[0]: row[index] for index, col in enumerate(cursor.description)}
