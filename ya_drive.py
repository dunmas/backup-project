import requests

from settings import YA_TOKEN

class YaDrive:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {YA_TOKEN}'}
        self.base_url = 'https://cloud-api.yandex.net/'


