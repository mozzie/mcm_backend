from server.mcm import mcm_api



def get(search):
    url = "products/find"
    parameters = "?search=" + search
    return [{"id": c['idProduct'],
             "name": c['locName'],
             "set": c['expansionName']} for c in mcm_api.request(url, parameters)['product']]


