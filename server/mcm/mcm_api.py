from requests_oauthlib import OAuth1Session
import json
import configparser
import os

configParser = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
configParser.read(configFilePath)

app_token = configParser.get('mcm', 'app_token')
app_secret = configParser.get('mcm', 'app_secret')
access_token = configParser.get('mcm', 'access_token')
access_token_secret = configParser.get('mcm', 'access_token_secret')

def request_base(base_url, parameters=""):
    full_url = "https://api.cardmarket.com/ws/v2.0/" + base_url
    auth = OAuth1Session(app_token,
                         client_secret=app_secret,
                         resource_owner_key=access_token,
                         resource_owner_secret=access_token_secret,
                         realm=full_url)
    r = auth.get(full_url + parameters)
    return r

def request(base_url, parameters=""):
    full_url = "https://api.cardmarket.com/ws/v2.0/output.json/" + base_url
    auth = OAuth1Session(app_token,
                         client_secret=app_secret,
                         resource_owner_key=access_token,
                         resource_owner_secret=access_token_secret,
                         realm=full_url)
    r = auth.get(full_url + parameters)
    print(r)
    return json.loads(r.content.decode("utf-8"))
