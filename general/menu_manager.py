from constants import MENU_FILE, BUFFER_FILE, CSV_FILE, sender_email, sender_password
from filelib import read_csv_column, csv_lines_len, write_csv_line, in_csv_column, delete_line, sort_by_label, show_labels, save, show_table
from checkers import validate_and_format_phone_number, validate_capitalized_word, validate_and_format_email, validate_password
from mailling import send_email
from hashlib import md5

def show_users():
    print("Последняя сохранённая таблица пользователей:")
    print(show_labels(CSV_FILE))
    print(show_table())
    print("#======================#")

def add_user():
    correct = False
    user_data = list()
    while not(correct):
        print("\033[1;34m" + "Добавление пользователя" + "\033[0;0m")
        firstname = validate_capitalized_word(input("Введите имя пользователя: "))
        lastname = validate_capitalized_word(input("Введите фамилию пользователя: "))
        process_input = lambda x: "Отсутствует" if x == "" else x
        patronymic = validate_capitalized_word(process_input(input("Введите отчество, если оно есть: ")))
        phonenumber = validate_and_format_phone_number(input("Введите номер телефона в форме c +7: "))
        email = validate_and_format_email(input("Введите почту: "))
        login = input("Введите логин: ")
        password = validate_password(input("Введите пароль: "))

        if(not(firstname and lastname and patronymic)):
            print("Имя, Фамилия, Отчество должны начинаться с заглавных букв!")
        elif(not(phonenumber)):
            print("Введите корректный номер телефона")
        elif(not(email)):
            print("Таких почтовых адресов не существует")
        elif(login == ""):
            print("Логин не может быть пустым полем")
        elif(in_csv_column(BUFFER_FILE, "LOGIN", login)):
            print("Пользователь с таким логином уже существует!")
        elif (in_csv_column(BUFFER_FILE, "phonenumber", phonenumber)):
            print("Пользователь с таким номером уже существует!")
        elif (in_csv_column(BUFFER_FILE, "email", email)):
            print("Пользователь с такой почтой уже существует!")
        elif(not(password)):
            print("Пароль не отвечает требованиям безопасности")
        else:
            # In csv check===========:
            lenght = csv_lines_len(BUFFER_FILE)
            for i in range(lenght - 1):
                if (read_csv_column(BUFFER_FILE, "FIRSTNAME", start=i, end=i + 1)[0] == firstname and
                        read_csv_column(BUFFER_FILE, "LASTNAME", start=i, end=i + 1)[0] == lastname):
                        print("Пользователь с таким именем и фамилией уже существует!")
                        correct = False
                        break
            # =======================
            else:
                print("Пользователь успешно зарегестрирован!")
                print("Не забудьте сохранить изменения")
                correct = True
                user_data = [lastname, firstname, patronymic, phonenumber, email, login, str(md5(password.encode('utf-8')).hexdigest())]
                write_csv_line(BUFFER_FILE, user_data)
                return
        while True:
            answ = input("Хотите ввести форму заново? (Д/Н)")
            if answ == "Н":
                return
            elif answ == "Д":
                break
            else:
                continue
    return


def delete_user():
    display_menu(MENU_FILE, "c")
    flag = True
    while(flag):
        choise = input("Выберите способ удаления: ")
        match (choise):
            case "i":
                flag=False
                firstname = validate_capitalized_word(input("Введите имя: "))
                if(not(firstname)):
                    print("Имя должно начинаться с заглавной буквы!")
                    break
                lastname = validate_capitalized_word(input("Введите фамилию:"))
                if (not (lastname)):
                    print("Фамилия должна начинаться с заглавной буквы!")
                    break
                length = csv_lines_len(BUFFER_FILE)
                for i in range(0, length-1):
                    if (read_csv_column(BUFFER_FILE, "FIRSTNAME", start=i, end=i)[0] == firstname and
                            read_csv_column(BUFFER_FILE, "LASTNAME", start=i, end=i)[0] == lastname):
                            passwd = input("Введите пароль: ")
                            if md5(passwd.encode('utf-8')).hexdigest() == \
                                read_csv_column(BUFFER_FILE, "PASSWORD", start=i, end=i)[0]:
                                print(read_csv_column(BUFFER_FILE, "PASSWORD", start=i, end=i)[0])
                                print(str(md5(passwd.encode('utf-8')).hexdigest()))
                                print("Пользователь удалён, сохраните изменения")
                                delete_line(BUFFER_FILE, i + 1)
                            else:
                                print("Пароль неверный!")
                                return
                else:
                    print("Такой пользователь не найден")
                    break
            case "ii":
                flag = False
                login = input("Введите логин: ")
                length = csv_lines_len(BUFFER_FILE)
                for i in range(0, length-1):
                    if (read_csv_column(BUFFER_FILE, "LOGIN", start=i, end=i)[0] == login):
                        passwd = input("Введите пароль: ")
                        if str(md5(passwd.encode('utf-8')).hexdigest()) == \
                                read_csv_column(BUFFER_FILE, "PASSWORD", start=i, end=i)[0]:
                                print("Пользователь удалён, сохраните изменения")
                                delete_line(BUFFER_FILE, i + 1)
                        else:
                            print("Пароль неверный!")
                            return
                else:
                    print("Такой пользователь не найден")
                    break
            case "iii":
                flag = False
                phone = validate_and_format_phone_number(input("Введите номер телефона: "))
                if(not(phone)):
                    print("Телефон введён некорректно!")
                    break
                length = csv_lines_len(BUFFER_FILE)
                for i in range(0, length-1):
                    if (read_csv_column(BUFFER_FILE, "PHONENUMBER", start=i, end=i)[0] == phone):
                        passwd = input("Введите пароль: ")
                        if str(md5(passwd.encode('utf-8')).hexdigest()) == \
                                read_csv_column(BUFFER_FILE, "PASSWORD", start=i, end=i)[0]:
                                print("Пользователь удалён, сохраните изменения")
                                delete_line(BUFFER_FILE, i + 1)
                        else:
                            print("Пароль неверный!")
                            return
                else:
                    print("Такой пользователь не найден")
                    break
            case _:
                print("Неверный способ")

def change_user():
    display_menu(MENU_FILE, "d")
    flag = True
    while (flag):
        choise = input("Выберите способ изменения: ")
        match (choise):
            case "i":
                flag = False
                firstname = validate_capitalized_word(input("Введите имя: "))
                if (not (firstname)):
                    print("Имя должно начинаться с заглавной буквы!")
                    break
                lastname = validate_capitalized_word(input("Введите фамилию:"))
                if (not (lastname)):
                    print("Фамилия должна начинаться с заглавной буквы!")
                    break
                length = csv_lines_len(BUFFER_FILE)
                for i in range(0, length - 1):
                    if (read_csv_column(BUFFER_FILE, "FIRSTNAME", start=i, end=i)[0] == firstname and
                            read_csv_column(BUFFER_FILE, "LASTNAME", start=i, end=i)[0] == lastname):
                        passwd = input("Введите пароль: ")
                        if str(md5(passwd.encode('utf-8')).hexdigest()) == \
                                read_csv_column(BUFFER_FILE, "PASSWORD", start=i, end=i)[0]:
                            print("Пароль верный")
                            print("Перезапишите данные:")
                            delete_line(BUFFER_FILE, i + 1)
                            add_user()
                            print("Сохраните изменения")
                        else:
                            print("Пароль неверный!")
                            return
                        break
            case "ii":
                flag = False
                login = input("Введите логин: ")
                length = csv_lines_len(BUFFER_FILE)
                for i in range(0, length - 1):
                    if (read_csv_column(BUFFER_FILE, "LOGIN", start=i, end=i)[0] == login):
                        passwd = input("Введите пароль: ")
                        if str(print(md5(passwd.encode('utf-8')).hexdigest())) == \
                                str(print(read_csv_column(BUFFER_FILE, "PASSWORD", start=i, end=i)[0])):
                                print("Пароль верный")
                                print("Перезапишите данные:")
                                delete_line(BUFFER_FILE, i + 1)
                                add_user()
                                print("Сохраните изменения")
                        else:
                            print("Пароль неверный!")
                            return
                else:
                    print("Такой пользователь не найден")
                    break
            case "iii":
                flag = False
                phone = validate_and_format_phone_number(input("Введите номер телефона: "))
                if (not (phone)):
                    print("Телефон введён некорректно!")
                    break
                length = csv_lines_len(BUFFER_FILE)
                for i in range(0, length - 1):
                    if (read_csv_column(BUFFER_FILE, "PHONENUMBER", start=i, end=i)[0] == phone):
                        passwd = input("Введите пароль: ")
                        if str(md5(passwd.encode('utf-8')).hexdigest()) == \
                                read_csv_column(BUFFER_FILE, "PASSWORD", start=i, end=i)[0]:
                                print("Пароль верный")
                                print("Перезапишите данные:")
                                delete_line(BUFFER_FILE, i + 1)
                                add_user()
                                print("Сохраните изменения")
                        else:
                            print("Пароль неверный!")
                            return
                else:
                    print("Такой пользователь не найден")
                    break
            case _:
                print("Неверный способ")

def save_changes():
    save()

def email():
    choise = input("Выберите способ отправления сообщения: ")
    flag = True
    while(flag):
        match (choise):
            case "i":
                flag = False
                firstname = validate_capitalized_word(input("Введите имя: "))
                if (not (firstname)):
                    print("Имя должно начинаться с заглавной буквы!")
                    break
                lastname = validate_capitalized_word(input("Введите фамилию:"))
                if (not (lastname)):
                    print("Фамилия должна начинаться с заглавной буквы!")
                    break
                length = csv_lines_len(CSV_FILE)
                for i in range(0, length-1):
                    if (read_csv_column(BUFFER_FILE, "FIRSTNAME", start=i, end=i)[0] == firstname and
                            read_csv_column(BUFFER_FILE, "LASTNAME", start=i, end=i)[0] == lastname):
                            mail = read_csv_column(CSV_FILE, "EMAIL", start=i, end=i)[0]
                            label = input("Введите заголовок сообщения: ")
                            text = input("Введите своё сообщение: ")
                            send_email(sender_email, sender_password, mail, label, text)
                            print("Сообщение отправлено на почту!")
                            break
            case "ii":
                flag = False
                login = input("Введите логин: ")
                length = csv_lines_len(CSV_FILE)
                for i in range(0, length - 1):
                    if (read_csv_column(CSV_FILE, "LOGIN", start=i, end=i)[0] == login):
                        mail = read_csv_column(CSV_FILE, "EMAIL", start=i, end=i)[0]
                        label = input("Введите заголовок сообщения: ")
                        text = input("Введите своё сообщение: ")
                        send_email(sender_email, sender_password, mail, label, text)
                        print("Сообщение отправлено на почту!")
                        break
                else:
                    print("Такой пользователь не найден")
                    break
            case "iii":
                flag = False
                phone = validate_and_format_phone_number(input("Введите номер телефона: "))
                if (not (phone)):
                    print("Телефон введён некорректно!")
                    break
                length = csv_lines_len(CSV_FILE)
                for i in range(0, length - 1):
                    if (read_csv_column(CSV_FILE, "PHONENUMBER", start=i, end=i)[0] == phone):
                        mail = read_csv_column(CSV_FILE, "EMAIL", start=i, end=i)[0]
                        label = input("Введите заголовок сообщения: ")
                        text = input("Введите своё сообщение: ")
                        send_email(sender_email, sender_password, mail, label, text)
                        print("Сообщение отправлено на почту!")
                        break
                else:
                    print("Такой пользователь не найден")
                    break
            case _:
                print("Неверный способ")

def sort_by_field():
    """Availible fields: LASTNAME;FIRSTNAME;PATRONYMIC;PHONENUMBER;EMAIL;LOGIN;PASSWORD"""
    show_users()
    print("Доступные поля для сортировки: " + str(show_labels(BUFFER_FILE)))
    choise = input("По какому полю вы хотите отсортировать?: ")
    if choise in show_labels(BUFFER_FILE):
        data = sort_by_label(BUFFER_FILE, choise)
        print(show_labels(BUFFER_FILE))
        for line in data:
            print(line)
    else:
        print("Нет такого поля!")


def display_menu(filename:str, identifier:str, color="\033[0;0m", endd="\n"):
    print(color)
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        # Ищем начало и конец блока с нужным идентификатором
        start_idx = None
        end_idx = None
        
        for idx, line in enumerate(lines):
            if line.strip() == f"#={{{identifier}}}":
                start_idx = idx
                break

        if start_idx is not None:
            for idx in range(start_idx + 1, len(lines)):
                if lines[idx].startswith("#={"):
                    end_idx = idx
                    break

            # Если мы не нашли следующий блок, то берем до конца файла
            if end_idx is None:
                end_idx = len(lines)

            # Выводим нужный блок
            for line in lines[start_idx + 1:end_idx]:
                print(line, end="")
            print("\033[0;0m", end="")
            print("", end=endd)
        else:
            print(f"Блок с идентификатором {identifier} не найден.")

    except FileNotFoundError:
        print("Файл 'menu.txt' не найден.")

def menu(input:str) -> bool:
    match input:
        case "a":
            show_users()
            return True
        case "b":
            add_user()
            return True
        case "c":
            delete_user()
            return True
        case "d":
            change_user()
            return True
        case "e":
            save_changes()
            print("Изменения сохранены")
            return True
        case "f":
            display_menu(MENU_FILE, "f")
            email()
            return True
        case "g":
            sort_by_field()
            return True
        case "h":
            display_menu(MENU_FILE, "h","\033[;1m"+ "\033[1;31m")
            return False
        case _:
            display_menu(MENU_FILE, "!", "\033[1;31m")
            return True
