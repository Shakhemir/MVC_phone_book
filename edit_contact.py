from config import fields
import user_interface as ui


def edit_contact(contacts_list):
    edit_id = ui.select_contact(contacts_list, 'для изменения')
    if edit_id:
        print(f'Введите новые значение для контакта (пустая строка, чтобы оставить как есть):')
        for i, edit_field in enumerate(contacts_list[edit_id]):
            print(f'{fields[i][0]} ({edit_field}):')
            new_field = ui.max_limit_input(fields[i][1])
            if new_field != '':
                contacts_list[edit_id][i] = new_field
    return contacts_list
