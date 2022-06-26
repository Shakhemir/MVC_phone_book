from show_list import show_contacts
from funcs import confirm_input


def delete(contacts_list):
    show_contacts(contacts_list)
    max_id = len(contacts_list) - 1
    del_id = '?'
    while not del_id.isdigit() or int(del_id) not in range(max_id + 1):
        del_id = input('Выберите N контакта для удаления: ')
    del_id = int(del_id)
    confirm = confirm_input(f'Вы точно хотите удалить контакт N {del_id} {contacts_list[del_id][0]}')
    if confirm:
        deleted_contact = contacts_list.pop(del_id)
        print(f'Контакт N {del_id} {deleted_contact[0]} удален!')
    return contacts_list
