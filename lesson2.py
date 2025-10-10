# LESSON #2. Переменные и типы данных

sym = '-'

# Part #1

print("\n" + sym * 50)

name = '1984'  # str
author = "Джордж Орвелл"  # str
year = '1949'  # int
pages_count = 312  # int
weight = 280.0  # float
is_available = True  # bool

print(
    "\nНазва: " + name,
    "\nАвтор: " + author,
    "\nКількість сторінок: " + str(pages_count),
    "\nРік першого видання: " + year + " (" + str((2025 - int(1949))) + " років тому)",
    "\nВага: " + str(weight),
    "\nЧи є в наявності: " + str(is_available))

# Part #2

print("\n" + sym * 50)

num1 = int(input("\nВведіть перше число: "))
num2 = int(input("Введіть друге число: "))

print(
    f"\n{num1} + {num2} = {num1 + num2}\n"
    f"{num1} - {num2} = {num1 - num2}\n"
    f"{num1} * {num2} = {num1 * num2}\n"
    f"{num1} / {num2} = {num1 / num2}\n"
    f"{num1} ** {num2} = {num1 ** num2}\n"
    f"{num1} % {num2} = {num1 % num2}"
)

sym = 0
print("\n" + str(sym) * 50)