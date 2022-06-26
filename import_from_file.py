from config import import_export_formats
import csv_io
import json_io
from user_interface import confirm_input, select_file_format


def import_format():
    from show_list import show_contacts
    file_format = select_file_format()
    file_name = input('Введите имя импортируемого файла: ')
    if '.' not in file_name:
        file_name += '.' + import_export_formats[file_format].lower()
    if file_format == 0:  # CSV
        imported_contacts = csv_io.import_from(file_name)
    else:
        imported_contacts = json_io.import_from(file_name)
    print(f'Контакты из импортируемого файла "{file_name}"')
    show_contacts(imported_contacts)
    confirm = confirm_input(f'Объединить с текущим справочником')
    if confirm:
        print(f'Загруженный файл добавлен в конец текущего справочника')
        return imported_contacts