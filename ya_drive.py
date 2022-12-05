import requests

from settings import YA_TOKEN

class YaDrive:
    def __init__(self, dir_name='VK_Profile_Backup'):
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {YA_TOKEN}'}
        self.base_url = 'https://cloud-api.yandex.net/'
        self._make_drive_dir(dir_name)

    def upload_photos(self, photos_dict):
        """
        Загружает на диск все переданные фотографии в базовую директорию
        :param photos_dict: Словарь фотографий по типу 'название': 'ссылка на фото'
        :return:
        """
        for photo in photos_dict:
            self._upload_photo_by_url(photos_dict[photo], photo)

        print('Готово! Бэкап сделан.')


    def _make_drive_dir(self, dir_name):
        """
        Создаёт на Яндекс.Диске папку с названием dir_name, если такая есть - удаляет существующую и пишет
        новую
        :param dir_name: Имя создаваемой на диске директории
        :return:
        """
        self.drive_dir = dir_name

    def _upload_photo_by_url(self, url, name):
        """
        Загружает на диск фото по ссылке в папку из self.drive_dir
        :param url: Ссылка на загрузку фотографии
        :return:
        """
        uri = '/v1/disk/resources/upload'
        request_url = self.base_url + uri
        params = {'url': url, 'path': self.drive_dir + name}
        response = requests.post(request_url, params=params, headers=self.headers)

        if response.status_code == 201:
            print('Готово!')
