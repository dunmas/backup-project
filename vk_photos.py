import requests

from settings import VK_TOKEN


class VkPhotos:
    """
    Класс работы с фотографиями профиля по переданному user_id
    """
    def __init__(self, user_id, version='5.131'):
        self.token = VK_TOKEN
        self.id = user_id
        self.photos = dict()
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def _make_photos_dict(self, pictures):
        """
        Функция собирает словарь из ссылок на изображениями с новым названием в ключе, где название -
        количество лайков
        :param pictures: список фотографий, полученный get запросом
        :return: none
        """
        pass

    def _get_max_def_link(self, picture):
        """
        Функция даёт ссылку на загрузку изображения в максимальном доступном качестве
        :param picture: фотография, полученная структурой dict из get запроса
        :return: ссылка на загрузку фотографии
        """
        link = ''

        return link

    def get_profile_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id,
                  'album_id': 'profile',
                  'photo_sizes': 1,
                  'extended': 1}

        # Получили JSON ответа сервера с фотографиями профиля - фото - response['response']['items']
        response = requests.get(url, params={**self.params, **params}).json()

        #Собираем dict ссылок на фотографии с будущим названием в ключе
        self._make_photos_dict(response['response']['items'])


