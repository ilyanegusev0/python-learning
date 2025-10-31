# LESSON #11.  Работа с файлами за счет Питон

file = open("files/text.txt", 'w')  # w - write
file.write("This file was created by function write().")
file.close()

with open("files/text.txt", 'a') as file:  # a - append
    while True:
        data = input("\nВведіть текст: ")

        if data.lower() == 'close':
            print("File closed.")
            break

        file.write("\n" + data)

with open("files/text.txt", 'r') as file:  # r - read
    print("\nfile.read(10): " + file.read(15))

    print("\nfor line in file:\n")
    for line in file:
        print(line)
