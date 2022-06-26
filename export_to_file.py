from config import import_export_formats
import csv_io
import json_io
from user_interface import select_file_format


def export_format(contacts_list):
    file_format = select_file_format()
    file_name = input('Введите имя файла для экспорта: ')
    if '.' not in file_name:
        file_name += '.' + import_export_formats[file_format].lower()
    if file_format == 0:  # CSV
        csv_io.export_to(file_name, contacts_list)
    else:
        json_io.export_to(file_name, contacts_list)
    print(f'Текущий справочник импортирован в файл "{file_name}"')