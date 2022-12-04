import requests

from settings import YA_TOKEN

class YaDrive:
    def __init__(self, dir_name='VK_Profile_Backup'):
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {YA_TOKEN}'}
        self.base_url = 'https://cloud-api.yandex.net/'
        self._make_drive_dir(dir_name)


    def _make_drive_dir(self, dir_name):
        """
        Создаёт на Яндекс.Диске папку с названием dir_name, если такая есть - удаляет существующую и пишет
        новую
        :param dir_name: Имя создаваемой на диске директории
        :return:
        """
        self.drive_dir = dir_name

    def upload_by_url(self, url):
        """
        Загружает на диск фото по ссылке в папку из self.drive_dir
        :param url: Ссылка на загрузку фотографии
        :return:
        """
        uri = '/v1/disk/resources/upload'
        request_url = self.base_url + uri
        params = {'url': url, 'path': self.drive_dir}
        response = requests.post(request_url, params=params, headers=self.headers)

        if response.status_code == 201:
            print('Готово!')
