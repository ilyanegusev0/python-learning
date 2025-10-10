# LESSON #4. Циклы и операторы в них (for, while)

for i in range(-10, 10, 2):  # from -10 to 9 with step 2
    print(i)

is_running = True
while True:
    text = input("\nВведіть текст: ")

    if text == 'exit':
        is_running = False
        break

    if text == '':
        continue

    symbol = input("Введіть символ для пошуку: ")

    count = 0
    for l in text:
        if l == symbol:
            count += 1

    print(f"Знайдено збігів: {count}.")
