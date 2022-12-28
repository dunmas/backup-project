from datetime import datetime

from tqdm import tqdm
import requests
import json

from settings import VK_TOKEN
from backup import make_backup_log


class VkPhotos:
    """
    Класс работы с фотографиями профиля по переданному user_id
    """
    def __init__(self, user_id, screen_name='', count=5, backup_path='./backup_log.txt', version='5.131'):
        self.token = VK_TOKEN
        self.photos = dict()
        self.version = version
        self.count = count
        self.params = {'access_token': self.token, 'v': self.version, 'count': count}
        self.json_list = list()
        self.backup_path = backup_path

        if screen_name != '':
            self.id = self._get_user_id()
        else:
            self.id = user_id

    def _get_user_id(self):
        result = ''
        return result

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
        try:
            self._make_photos_dict(response['response']['items'])
        except KeyError:
            print('Возникла ошибка при обращении к серверам VK. Проверьте введённые данные или повторите '
                  'позднее.')
            exit()

        make_backup_log(self.backup_path, self.json_list)
        self.count = len(self.photos)

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
            if str(image['likes']['count']) + '.jpg' in self.photos:
                date = datetime.utcfromtimestamp(image['date']).strftime('%Y-%m-%d')
                name = str(image['likes']['count']) + "_" + str(date) + ".jpg"
                image_params = self._get_max_def_link(image)

                self.photos[name] = image_params[0]
            else:
                name = str(image['likes']['count']) + ".jpg"
                image_params = self._get_max_def_link(image)

                self.photos[name] = image_params[0]

            self.json_list.append({"file_name": name, "size": image_params[1]})

    def _get_max_def_link(self, picture):
        """
        Функция даёт ссылку на загрузку изображения в максимальном доступном качестве
        :param picture: фотография, полученная структурой dict из get запроса
        :return: список, где первый элемент - ссылка на загрузку фотографии, второй - её размер
        """
        sizes_dict = dict()
        for size in picture['sizes']:
            sizes_dict[size['type']] = size['url']

        # Размеры по возрастанию идут в алфавитном порядке, но выделяется самый большой - w
        if 'w' in sizes_dict:
            link = sizes_dict['w']
            mark = 'w'
        else:
            params = sorted(sizes_dict.items())[-1]
            link = params[1]
            mark = params[0]

        return [link, mark]
