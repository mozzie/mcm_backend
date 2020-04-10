from server.mcm import mcm_api
import base64
import gzip
import csv

def get_stock():
    url = "stock/file"
    data = mcm_api.request(url, "")
    zip = base64.b64decode(data['data']['stock'])
    csv_data = gzip.decompress(zip).decode("utf-8")
    reader = csv.DictReader(csv_data.splitlines(), delimiter=";")
    reader.fieldnames = "id", "product_id", "name", "local_name", "card_set", "full_set", "price", "language", "cond", "foil", "signed", "playset","altered","mcm_comment","amount","onsale"
    next(reader, None)  # skip the headers
    cards = [row for row in reader]
    for card in cards:
        card['price'] = int(float(card['price'])*100)
        card['language'] = "ENG" if card['language'] == '1' else "foreign"
        for i in ['amount','id','product_id']:
            card[i] = int(card[i])
        for b in ['foil','signed','playset','altered']:
            card[b] = 1 if card[b] == 'X' else 0
    return {'data':cards, "limit": data['limit']}
