from mysql import connector
from os import path
ROOT = path.dirname(path.realpath(__file__))
import time

con = None
def db_connect():
    global con
    if con is not None and con.is_connected():
        return con
    con = connector.connect(host='localhost',
                            database='db',
                            user='username',
                            password='passwd')
    return con
# TODO store DB credentials in config files

def query(query, parameters={}):
    connection = db_connect()
    connection.cursor().execute(query, parameters)
    connection.commit()
    connection.close()

def query_batch(query, parameters={}):
    connection = db_connect()
    connection.cursor().execute(query, parameters)

def close():
    connection = db_connect()
    connection.commit()
    connection.close()

def fetch(query, parameters={}):
    connection = db_connect()
    cur = connection.cursor(dictionary=True)
    cur.execute(query, parameters)
    data = cur.fetchall()
    connection.close()
    return data

def fetch_batch(query, parameters={}):
    connection = db_connect()
    cur = connection.cursor(dictionary=True)
    cur.execute(query, parameters)
    data = cur.fetchall()
    return data


def get_cards(orderfield = "name", direction = "ASC"):
    if orderfield == 'trend_diff':
        orderfield = "(price - trend_price)"
    return fetch("SELECT * FROM CARDS ORDER BY {}".format(orderfield + " " + direction))

def get_not_updated_cards():
    timestamp = int(time.time()) - 60*60*24*7
    return fetch("SELECT * FROM CARDS WHERE updated IS null OR updated < %(time)s limit 100",  {"time": timestamp})

def insert_card(card):
    query_batch("INSERT INTO CARDS(id, product_id, name, card_set, price, language, cond, foil, signed, playset, altered, mcm_comment, amount) VALUES(%(id)s, %(product_id)s, %(name)s, %(card_set)s, %(price)s, %(language)s, %(cond)s, %(foil)s, %(signed)s, %(playset)s, %(altered)s, %(mcm_comment)s, %(amount)s)",
          card)


def update_card(card_id, trend_price):
    query("UPDATE CARDS SET trend_price=%(price)s, updated = %(stamp)s WHERE id = %(id)s",
          {"id": card_id, "price": trend_price, "stamp": int(time.time())})

def update_card_from_csv(card):
    query_batch("UPDATE CARDS SET language=%(language)s,cond=%(cond)s,foil=%(foil)s,signed=%(signed)s,playset=%(playset)s,altered=%(altered)s,mcm_comment=%(mcm_comment)s, amount=%(amount)s, price=%(price)s WHERE id = %(id)s", card)


def delete_card(card_id):
    query_batch("DELETE FROM CARDS WHERE id = %(card_id)s", {"card_id": card_id})


def get_card(card_id):
    cards = fetch("SELECT * FROM CARDS WHERE id = %(card_id)s", {"card_id": card_id})
    if cards and len(cards)>0:
        return cards[0]
    else:
        return None


def insert_sold(sold):
    query_batch("INSERT INTO SOLD(id, product_id, name, card_set, price, language, cond, foil, signed, playset, altered, mcm_comment, amount, timestamp) VALUES(%(id)s, %(product_id)s, %(name)s, %(card_set)s, %(price)s, %(language)s, %(cond)s, %(foil)s, %(signed)s, %(playset)s, %(altered)s, %(mcm_comment)s, %(amount)s, %(timestamp)s)",
          sold)

def get_sold(card_id):
    cards = fetch_batch("SELECT * FROM SOLD WHERE id = %(card_id)s", {"card_id": card_id})
    if cards and len(cards)>0:
        for sold in cards:
            sold['timestamp'] = str(sold['timestamp'])
        return cards[0]
    else:
        return None

def get_all_sold(orderfield = "name", direction = "ASC"):
    cards = fetch("SELECT * FROM SOLD ORDER BY {}".format(orderfield + " " + direction))
    for sold in cards:
        sold['timestamp'] = str(sold['timestamp'])
    return cards
