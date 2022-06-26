def import_from(file_name: str):
    contacts_list = []
    with open(file_name, 'r') as file:
        for contact_line in file.readlines():
            contact = contact_line.strip().split(';')
            contacts_list.append(contact)
    return contacts_list


def export_to(file_name: str, contacts_list: list):
    with open(file_name, 'w') as file:
        for contact in contacts_list:
            print(';'.join(contact), file=file)
