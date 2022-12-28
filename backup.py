import json


def make_backup_log(backup_path, json_list):
    """
    Записывает в backup_path файл JSON-лог в заданном формате
    :param backup_path: файл, в который будет произведена запись JSON-лога
    :param json_list: Словарь словарей формата {"file_name": наименование_файла, "size": размер_файла}
    """
    with open(backup_path, 'w') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=2)
