import requests
import json

class Service:
    def __init__(self, url):
        self.head = {
            'accept': 'application/json', 
            'Content-Type': 'application/json'
        }
        self.url = url

    def connect(self, url_auth, login, password) -> bool:
        payload = {
            "login": login,
            "password": password
        }
        data = json.dumps(payload) # преобразование словаря payload в json-формат

        response = requests.post(self.url + url_auth, headers = self.head, data = data)
        print(response.status_code)
        if response.status_code == 200:
            token = json.loads(response.text)
            if token["accessToken"] != None:
                self.head["Authorization"] = "Bearer " + token["accessToken"]
                print(token["accessToken"])
                return True
            else:
                return False
        else:
            return False
