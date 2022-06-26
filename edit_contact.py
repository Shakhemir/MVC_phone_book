from show_list import show_contacts
from config import fields
from user_interface import max_limit_input


def edit_contact(contacts_list):
    show_contacts(contacts_list)
    max_id = len(contacts_list) - 1
    edit_id = '?'
    while not edit_id.isdigit() or int(edit_id) not in range(max_id + 1):
        edit_id = input('Выберите N контакта для редактирования (пустая строка - отмена): ')
        if edit_id == '':
            return contacts_list
    edit_id = int(edit_id)
    print(f'Введите новые значение для контакта (пустая строка, чтобы оставить как есть):')
    for i, edit_field in enumerate(contacts_list[edit_id]):
        print(f'{fields[i][0]} ({edit_field}):')
        new_field = max_limit_input(fields[i][1])
        if new_field != '':
            contacts_list[edit_id][i] = new_field
    return contacts_list
