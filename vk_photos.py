from datetime import datetime

from tqdm import tqdm
import requests

from settings import VK_TOKEN


class VkPhotos:
    """
    Класс работы с фотографиями профиля по переданному user_id
    """
    def __init__(self, user_id, count=5, version='5.131'):
        self.token = VK_TOKEN
        self.id = user_id
        self.photos = dict()
        self.version = version
        self.count = count
        self.params = {'access_token': self.token, 'v': self.version, 'count': count}

    def get_profile_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id,
                  'album_id': 'profile',
                  'photo_sizes': 1,
                  'extended': 1}
        print('Смотрим ваш профиль...')

        # Получили JSON ответа сервера с фотографиями профиля - фото - response['response']['items']
        response = requests.get(url, params={**self.params, **params}).json()

        #Собираем dict ссылок на фотографии с будущим названием в ключе
        self._make_photos_dict(response['response']['items'])

        return self.photos

    def _make_photos_dict(self, pictures):
        """
        Функция собирает словарь из ссылок на изображениями с новым названием в ключе, где название -
        количество лайков
        :param pictures: список фотографий, полученный get запросом
        :return: none
        """
        print('Обрабатываем полученные фотографии...')
        for image in tqdm(pictures, colour='GREEN'):
            if image['likes']['count'] in self.photos:
                date = datetime.utcfromtimestamp(image['date']).strftime('%Y-%m-%d')
                self.photos[image['likes']['count'] + date] = self._get_max_def_link(image)
            else:
                self.photos[image['likes']['count']] = self._get_max_def_link(image)

    def _get_max_def_link(self, picture):
        """
        Функция даёт ссылку на загрузку изображения в максимальном доступном качестве
        :param picture: фотография, полученная структурой dict из get запроса
        :return: ссылка на загрузку фотографии
        """
        sizes_dict = dict()
        for size in picture['sizes']:
            sizes_dict[size['type']] = size['url']

        # Размеры по возрастанию идут в алфавитном порядке, но выделяется самый большой - w
        if 'w' in sizes_dict:
            link = sizes_dict['w']
        else:
            link = sorted(sizes_dict.items())[-1][1]

        return link
