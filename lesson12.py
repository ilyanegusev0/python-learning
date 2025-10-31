# LESSON #12. Обработчик исключений. Конструкция «try - except»

while True:
    try:
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))

        res = a / b

        print(f"{a} / {b} = {res}")

    except ValueError as ex:
        print("Значення має бути цілочисленним.")

    except ZeroDivisionError:
        print("Ділення на нуль неможливе.")

    else:
        break

    finally:
        print()
