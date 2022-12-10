from vk_photos import VkPhotos
from ya_drive import YaDrive

if __name__ == '__main__':
    id = input(f"Это программа для резервного копирования фотографий профиля VK.\n"
               f"Не забудьте указать ваш токен Яндекс.Диска в файле 'settings.py'!\n"
               f"Введите ID необходимого профиля: ")
    print('-----------------------------------------------------------')
    count = input(f"Введите желаемое количество фотографий для создания бэкапа\n(чтобы выбрать количество "
                  f"по умолчанию - нажмите <Enter>: ")
    print('-----------------------------------------------------------')
    dir_name = input(f"Введите желаемое имя директории\n(чтобы выбрать имя по умолчанию - нажмите "
                     f"<Enter>): ")
    print('-----------------------------------------------------------')

    vk_params = [id]
    if count != '':
        vk_params.append(count)

    #Работаем с VK API
    album = VkPhotos(*vk_params)
    pics = album.get_profile_photos()

    #Работаем с Ya.Disk API
    if dir_name != '':
        drive = YaDrive(dir_name)
    else:
        drive = YaDrive()
    drive.upload_photos(pics)
