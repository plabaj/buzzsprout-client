import requests

class BuzzsproutClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.buzzsprout.com/api"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Token {self.api_key}",
            "Accept": "application/json"
        })
