import requests

from settings import VK_TOKEN


class VkPhotos:
    """
    Класс работы с фотографиями профиля по переданному user_id
    """
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
