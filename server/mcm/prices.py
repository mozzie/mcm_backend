from server.mcm import mcm_api


class Prices:

    def get(self, card_id, condition=None):
        url = "articles/" + str(card_id)
        parameters = "?idLanguage=1"
        if condition:
            parameters += "&minCondition=" + condition
        return mcm_api.request(url, parameters)['article']
