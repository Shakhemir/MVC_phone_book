import user_interface as ui


def delete(contacts_list):
    del_id = ui.select_contact(contacts_list, 'для удаления')
    if del_id:
        confirm = ui.confirm_input(f'Вы точно хотите удалить контакт N {del_id} "{" ".join(contacts_list[del_id][:2])}"')
        if confirm:
            deleted_contact = contacts_list.pop(del_id)
            print(f'Контакт N {del_id} "{" ".join(deleted_contact[:2])}" удален!')
    return contacts_list
