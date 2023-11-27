import json

def load_data():
    try:
        with open('phone_book.txt', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('phone_book.txt', 'w') as file:
        json.dump(data, file, indent=2)

def display_data(data):
    if not data:
        print("Телефонный справочник пуст.")
    else:
        print("Телефонный справочник:")
        for contact_id, contact in data.items():
            print(f"{contact_id}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Номер телефона']}")

def search_record(data, key, value):
    found_records = [contact_id for contact_id, contact in data.items() if contact[key] == value]
    return found_records

def add_record(data, surname, name, patronymic, phone_number):
    contact_id = str(len(data) + 1)
    data[contact_id] = {
        'Фамилия': surname,
        'Имя': name,
        'Отчество': patronymic,
        'Номер телефона': phone_number
    }
    print("Запись успешно добавлена.")

def update_record(data, contact_id, key, value):
    data[contact_id][key] = value
    print("Запись успешно обновлена.")

def delete_record(data, contact_id):
    del data[contact_id]
    print("Запись успешно удалена.")

def main():
    phone_book = load_data()

    while True:
        print("\nВыберите действие:")
        print("1. Вывести данные")
        print("2. Сохранить данные")
        print("3. Импорт данных")
        print("4. Поиск записи")
        print("5. Добавить запись")
        print("6. Изменить запись")
        print("7. Удалить запись")
        print("8. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            display_data(phone_book)
        elif choice == '2':
            save_data(phone_book)
            print("Данные сохранены.")
        elif choice == '3':
            import_file = input("Введите имя файла для импорта: ")
            try:
                with open(import_file, 'r') as file:
                    imported_data = json.load(file)
                    phone_book.update(imported_data)
                print("Данные успешно импортированы.")
            except FileNotFoundError:
                print("Файл не найден.")
            except json.JSONDecodeError:
                print("Ошибка при чтении файла.")
        elif choice == '4':
            search_key = input("Введите характеристику для поиска (Фамилия, Имя, Отчество, Номер телефона): ").capitalize()
            search_value = input(f"Введите значение {search_key}: ")
            found_records = search_record(phone_book, search_key, search_value)
            if found_records:
                print("Найденные записи:")
                for record_id in found_records:
                    print(f"{record_id}. {phone_book[record_id]['Фамилия']} {phone_book[record_id]['Имя']} {phone_book[record_id]['Отчество']}: {phone_book[record_id]['Номер телефона']}")
            else:
                print(f"Записи по {search_key} '{search_value}' не найдены.")
        elif choice == '5':
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            add_record(phone_book, surname, name, patronymic, phone_number)
        elif choice == '6':
            record_id = input("Введите номер записи для изменения: ")
            if record_id in phone_book:
                update_key = input("Введите характеристику для изменения (Фамилия, Имя, Отчество, Номер телефона): ").capitalize()
                update_value = input(f"Введите новое значение {update_key}: ")
                update_record(phone_book, record_id, update_key, update_value)
            else:
                print("Запись с указанным номером не найдена.")
        elif choice == '7':
            record_id = input("Введите номер записи для удаления: ")
            if record_id in phone_book:
                delete_record(phone_book, record_id)
            else:
                print("Запись с указанным номером не найдена.")
        elif choice == '8':
            save_data(phone_book)
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите корректный номер действия.")

if __name__ == "__main__":
    main()