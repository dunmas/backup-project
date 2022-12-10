import requests

from tqdm import tqdm
from settings import YA_TOKEN


class YaDrive:
    def __init__(self, dir_name='VK_Profile_Backup'):
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {YA_TOKEN}'}
        self.base_url = 'https://cloud-api.yandex.net'
        self._make_drive_dir(dir_name)

    def upload_photos(self, photos_dict):
        """
        Загружает на диск все переданные фотографии в базовую директорию
        :param photos_dict: Словарь фотографий по типу 'название': 'ссылка на фото'
        :return:
        """
        print('Загружаем ваши фото на диск...')
        for photo in tqdm(photos_dict, colour='GREEN'):
            self._upload_photo_by_url(photos_dict[photo], photo)

        print("Готово! Бэкап сделан.\n"
              "Лог файл 'backup_log.txt' лежит в директории проекта.")

    def _make_drive_dir(self, dir_name):
        """
        Создаёт на Яндекс.Диске папку с названием dir_name, если такая есть - удаляет существующую и пишет
        новую
        :param dir_name: Имя создаваемой на диске директории
        :return:
        """
        self.drive_dir = '/' + dir_name
        uri = '/v1/disk/resources'
        request_url = self.base_url + uri
        test_params = {'path': self.drive_dir}

        response_code = requests.get(request_url, params=test_params, headers=self.headers).status_code

        if response_code == 404:
            response_code = requests.put(request_url, params=test_params, headers=self.headers).status_code

            if response_code == 201:
                print(f"\rДиректория '{self.drive_dir[1:]}' создана!")
        elif response_code == 200:
            counter = 1
            print('Директория с заданным именем уже существует. Пробуем создать новую...')

            while (response_code == 200):
                # addon необходим для решения случая, если бэкап-папка с таким названием уже есть
                addon = f'_{counter}'
                test_params['path'] = self.drive_dir + addon
                response_code = requests.get(request_url, params=test_params,
                                             headers=self.headers).status_code
                counter += 1

            response_code = requests.put(request_url, params=test_params, headers=self.headers).status_code

            if response_code == 201:
                print(f"\rНовая директория бэкапа - '{self.drive_dir + addon}'")
            else:
                print(f'Возникла ошибка обращения к серверу. Её код: {response_code}')
            self.drive_dir += addon
        else:
            print(f'Возникла ошибка обращения к серверу. Её код: {response_code}')
            exit()

    def _upload_photo_by_url(self, url, name):
        """
        Загружает на диск фото по ссылке в папку из self.drive_dir
        :param url: Ссылка на загрузку фотографии
        :return:
        """
        uri = '/v1/disk/resources/upload'
        request_url = self.base_url + uri
        params = {'url': url, 'path': self.drive_dir + '/' + str(name)}
        response = requests.post(request_url, params=params, headers=self.headers)

        if response.status_code == 201:
            print('Готово!')
