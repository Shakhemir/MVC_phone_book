from config import fields


def show_contacts(contacts_list):
    width = sum([f[1] for f in fields]) + len(fields)  # ширина записи контакта
    print('-' * width)
    size = len(str(len(contacts_list)))  # узнаем какого размера должен быть id контакта для выравнивания
    print(f'{"N".ljust(size)}  {"  ".join([f[0].ljust(f[1]) for f in fields])}')
    print('-' * width)
    for id, contact in enumerate(contacts_list):
        print(str(id).zfill(size), end='  ')
        for i, element in enumerate(fields):
            print(contact[i].ljust(element[1]), end='  ')
        print()
    print('-' * width)
