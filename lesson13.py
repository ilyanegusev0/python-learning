# LESSON #13. Менеджер «With ... as» для работы с файлами

# try:
#     file = open("file", 'r')
#     file.read()
# except FileNotFoundError:
#     print("ERROR: The file could not be found.")
# finally:
#     file.close() # NameError

try:
    with open("file", 'r', encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("ERROR: The file could not be found.")
