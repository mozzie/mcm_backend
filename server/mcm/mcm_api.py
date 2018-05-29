from requests_oauthlib import OAuth1Session
import json
import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'mcm_config.ini'
configParser.read(configFilePath)

app_token = configParser.get('mcm', 'app_token')
app_secret = configParser.get('mcm', 'app_secret')
access_token = configParser.get('mcm', 'access_token')
access_token_secret = configParser.get('mcm', 'access_token_secret')


def request(base_url, parameters=""):
    full_url = "https://api.cardmarket.com/ws/v2.0/output.json/" + base_url
    auth = OAuth1Session(app_token,
                         client_secret=app_secret,
                         resource_owner_key=access_token,
                         resource_owner_secret=access_token_secret,
                         realm=full_url)
    r = auth.get(full_url + parameters)
    return json.loads(r.content.decode("utf-8"))