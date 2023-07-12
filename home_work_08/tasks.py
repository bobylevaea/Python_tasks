# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления 
# данных. Пользователь также может ввести имя или фамилию, и Вы должны 
# реализовать функционал для изменения и удаления данных.

phone_book = {}
path: str = 'phones.txt'


def open_file():
    phone_book.clear()
    try:
        file = open(path, 'r+', encoding='UTF-8')
    except FileNotFoundError:
        file = open(path, 'w+', encoding='UTF-8')
    data = file.readlines()
    file.close()

    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}

    print('\nТелефонная книга успешно загружена!')


def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        for i, contact in phone_book.items():
            contact_data = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
            file.write(contact_data + '\n')
    print('\nТелефонная книга успешно сохранена!')


def show_contacts(book: dict[int, dict]):
    if not book:
        print('\nТелефонная книга пуста.')
    else:
        print('\n' + '=' * 20)
        for i, cnt in book.items():
            print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
        print('=' * 20 + '\n')


def add_contact():
    if not phone_book:
        uid = 1
    else:
        uid = max(list(phone_book.keys())) + 1

    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}

    print(f'\nКонтакт {name} успешно добавлен в телефонную книгу!')


def search():
    if not phone_book:
        print('\nТелефонная книга пуста.')
        return {}

    result = {}
    word = input('Введите слово, по которому будем искать: ')
    for i, contact in phone_book.items():
        if word.lower() in ''.join(list(contact.values())).lower():
            result[i] = contact
    return result


def change_file():
    if not phone_book:
        print('\nТелефонная книга пуста.')
        return

    result = search()
    show_contacts(result)
    index = int(input('Введите индекс контакта, который необходимо изменить: '))

    if index not in phone_book:
        print('Некорректный индекс контакта.')
        return

    contact = phone_book[index]
    name = input('Введите новое имя контакта (оставьте пустым, чтобы оставить прежнее имя): ')
    phone = input('Введите новый телефон контакта (оставьте пустым, чтобы оставить прежний телефон): ')
    comment = input('Введите новый комментарий к контакту (оставьте пустым, чтобы оставить прежний комментарий): ')

    if not name:
        name = contact.get("name")
    if not phone:
        phone = contact.get("phone")
    if not comment:
        comment = contact.get("comment")

    phone_book[index] = {'name': name, 'phone': phone, 'comment': comment}

    print(f'\nКонтакт {name} успешно изменен в телефонной книге!')


def remove():
    if not phone_book:
        print('\nТелефонная книга пуста.')
        return

    result = search()
    show_contacts(result)
    index = int(input('Введите индекс контакта, который необходимо удалить: '))

    if index not in phone_book:
        print('Некорректный индекс контакта.')
        return

    del_cnt = phone_book.pop(index)
    del_name = del_cnt.get("name")
    print(f'\nКонтакт {del_name} успешно удален из телефонной книги!')

    updated_phone_book = {}
    new_index = 1
    for contact in phone_book.values():
        updated_phone_book[new_index] = contact
        new_index += 1
    phone_book.clear()
    phone_book.update(updated_phone_book)


def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('\nОшибка ввода, введите число от 1 до 8!')


print('Добро пожаловать в телефонный справочник!')
while True:
    select = menu()
    if select == 1:
        open_file()
    elif select == 2:
        save_file()
    elif select == 3:
        show_contacts(phone_book)
    elif select == 4:
        add_contact()
    elif select == 5:
        result = search()
        show_contacts(result)
    elif select == 6:
        change_file()
    elif select == 7:
        remove()
    elif select == 8:
        print('До свидания!')
        break
