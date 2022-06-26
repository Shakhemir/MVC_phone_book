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
