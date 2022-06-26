from os.path import exists
import csv_io
import user_interface as ui
from config import *
import show_list
import add_contact, delete_contact, edit_contact
import import_from_file
import export_to_file

contacts_list = []
contacts_file = ''


def init(file):
    global contacts_list, contacts_file
    contacts_file = file if file else default_contacts_file
    print(f'Телефонный справочник из файла "{contacts_file}"')
    if exists(contacts_file):
        contacts_list = csv_io.import_from(contacts_file)


def main_polling():
    command = '?'
    while command != '':
        ui.show_menu()
        command = ui.select_command()
        if command.isdigit():
            execute_command(int(command))
    csv_io.export_to(contacts_file, contacts_list)
    print(f'Файл "{contacts_file}" сохранен.')


def execute_command(command):
    global contacts_list
    if command == 1:  # Показать список контактов
        show_list.show_contacts(contacts_list)
    elif command == 2:  # Добавить контакт
        contacts_list = add_contact.add_contact(contacts_list)
    elif command == 3:  # Редактировать контакт
        contacts_list = edit_contact.edit_contact(contacts_list)
    elif command == 4:  # Удаление контакта
        contacts_list = delete_contact.delete(contacts_list)
    elif command == 5:  # Импорт из файла
        imported_contacts = import_from_file.import_format()
        if imported_contacts is not None:
            contacts_list += imported_contacts
    elif command == 6:  # Экспорт в файл
        export_to_file.export_format(contacts_list)
    else:
        print("Введите верную команду")


def run_app(contacts_file):
    init(contacts_file)
    main_polling()
