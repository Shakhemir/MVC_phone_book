from config import fields
from user_interface import max_limit_input


def add_contact(contacts_list):
    new_contact = []
    for i, field in enumerate(fields):
        new_field = max_limit_input(field[1], f'{field[0]}: ')
        new_contact.append(new_field)
    contacts_list.append(new_contact)
    return contacts_list
