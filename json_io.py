import json
from config import json_field_names


def import_from(file_name: str):
    with open(file_name, 'r') as file:
        jdata = file.read().strip()
    jdata = json.loads(jdata)
    contacts_list = []
    for d in jdata:
        contact = []
        for value in d.values():
            contact.append(value)
        contacts_list.append(contact)
    return contacts_list


def export_to(file_name: str, contacts_list: list):
    contacts_dict_list = []
    for contact in contacts_list:
        contact_dict = dict()
        for i, field in enumerate(contact):
            contact_dict[json_field_names[i]] = field
        contacts_dict_list.append(contact_dict)
    with open(file_name, 'w') as file:
        json.dump(contacts_dict_list, file, indent=4, ensure_ascii=False)
