from vk_photos import VkPhotos
from ya_drive import YaDrive

if __name__ == '__main__':
    id = ''
    screen_name = ''

    while True:
        response = input(f"Это программа для резервного копирования фотографий профиля VK.\n"
                   f"Не забудьте указать ваш токен Яндекс.Диска в файле 'settings.py'!\n"
                   f"Выберите вариант доступа к аккаунту:\n"
                   f"1. По ID\n"
                   f"2. По screen_name (никнейм/короткое имя)\n")

        if response == '1':
            id = input("Введите ID необходимого профиля: ")
            break
        elif response == '2':
            screen_name = input("Введите screen_name необходимого профиля: ")
            break

    print('-----------------------------------------------------------')
    count = input(f"Введите желаемое количество фотографий для создания бэкапа\n(чтобы выбрать количество "
                  f"по умолчанию - нажмите <Enter>: ")
    print('-----------------------------------------------------------')
    dir_name = input(f"Введите желаемое имя директории\n(чтобы выбрать имя по умолчанию - нажмите "
                     f"<Enter>): ")
    print('-----------------------------------------------------------')

    vk_params = [id, screen_name]
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
