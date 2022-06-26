"Конфигурация приложения"

default_contacts_file = 'contacts.csv'  # В этом файле будет храниться по умолчанию список контактов
fields = ('Имя', 15), ('Фамилия', 15), ('Телефон', 12), ('Описание', 35)  # Поля и их максимальный размер"
json_field_names = 'Name', 'Last name', 'Phone number', 'Comment'

command_list = '01. Показать список', '02. Добавить контакт', '03. Редактировать контакт', '04. Удалить контакт', \
               '05. Импортировать из файла', '06. Экспортировать в файл'

import_export_formats = 'CSV', 'JSON'
