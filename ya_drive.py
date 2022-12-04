import requests

from settings import YA_TOKEN

class YaDrive:
    def __init__(self, dir_name='VK_Profile_Backup'):
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {YA_TOKEN}'}
        self.base_url = 'https://cloud-api.yandex.net/'
        self.drive_dir = dir_name

    def _make_drive_dir(self):
        """
        Создаёт на Яндекс.Диске папку с названием из self.drive_dir
        :return:
        """
        pass

    def upload_by_url(self, url):
        """
        Загружает на диск фото по ссылке в папку из self.drive_dir
        :param url: Ссылка на загрузку фотографии
        :return:
        """
        pass
