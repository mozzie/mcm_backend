from server.mcm import mcm_api
import base64
import gzip
import csv

def get_product(product_id):
    url = "products/" + str(product_id)
    data = mcm_api.request(url, "")
    return data
