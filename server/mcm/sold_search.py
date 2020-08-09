from server.mcm import mcm_api
import base64
import gzip
import csv

def get_sold(start):
    url = "orders/seller/received/{}".format(start)
    data = mcm_api.request(url, "")
    print(data)
    return {'data':data, "limit": data['limit']}
