# LESSON #3. Условные операторы

password = '123456'

is_logged = False
is_reset = False
is_skipped = False

data = input("\nВведіть пароль: ")

if data == password:
    is_logged = True

elif data == 'reset':
    is_reset = True

elif data == 'skip':
    is_skipped = True

else:
    is_logged = False

if is_logged:
    print("\nВи успішно увійшли у систему!")

elif is_reset:
    data = input("\nВведіть новий пароль: ")
    data = data if data != password else None

    if data != None:
        password = data
        print("\nПароль успішно змінено!")

    else:
        print("\nВведіть пароль відмінний від минулих!")

elif is_reset and not is_logged:
    password = input("\nВведіть пошту: ")

elif is_skipped or not is_logged:
    print("\nВ доступі відмовлено!")
