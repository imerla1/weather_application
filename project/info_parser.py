class Info:
    def __init__(self):
        self.city = ''
        self.country = ''

    def get_personal_info(self):
        import requests
        import json

        
        url = 'http://ip-api.com/json/'
        req=requests.get(url)


        x = req.json()

        dict_mapping = {}

        for i in x:
            self.city = x['city']
            self.country = x['country']
            dict_mapping[i] = x[i]

        return dict_mapping
