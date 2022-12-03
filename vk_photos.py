import requests

from settings import VK_TOKEN


class VkPhotos:
    """
    Класс работы с фотографиями профиля по переданному user_id
    """
    def __init__(self, user_id, version='5.131'):
        self.token = VK_TOKEN
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_profile_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id,
                  'album_id': 'profile',
                  'photo_sizes': 1,
                  'extended': 1}

        # Получили JSON ответа сервера с фотографиями профиля
        response = requests.get(url, params={**self.params, **params}).json()

