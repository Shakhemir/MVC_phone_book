from config import command_list


def show_menu():
    menu = ' | '.join(command_list)
    print()
    print('=' * len(menu))
    print(menu)
    print('=' * len(menu))
    print()


def select_command():
    return input('Выберите номер команды (для выхода пустая строка): ')


def confirm_input(text=''):
    answer = input(f'{text} (для подтверждения введите "да"/"yes"/"y")?')
    return answer.lower() in ('да', 'yes', 'y')


def max_limit_input(max_limit: int, text=''):
    txt_len = max_limit + 1
    input_text = ''
    while txt_len > max_limit:
        input_text = input(text)
        txt_len = len(input_text)
        if txt_len > max_limit:
            print(f'Введите не больше {max_limit} символов')
    return input_text


def select_file_format():
    from config import import_export_formats
    print('Из файла какого формата импортировать справочник?')
    print(', '.join(f'{i + 1} {file_format}' for i, file_format in enumerate(import_export_formats)))
    max_count = len(import_export_formats)
    selected_format = '?'
    while not selected_format.isdigit() or selected_format in range(1, max_count + 1):
        selected_format = input()
    return int(selected_format) - 1


def select_contact(contacts_list, for_what=''):
    from show_list import show_contacts
    show_contacts(contacts_list)
    max_id = len(contacts_list)
    select_contact_id = '?'
    while not select_contact_id.isdigit() or int(select_contact_id) not in range(max_id):
        select_contact_id = input(f'Выберите N контакта {for_what} (пустая строка - отмена): ')
        if select_contact_id == '':
            return False
    return int(select_contact_id)
