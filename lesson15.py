# LESSON #15. Основы ООП. Создание класса и объекта

class Cat:
    name = None
    age = None
    weight = None

    def set_data(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def show_info(self):
        print(f"NAME: {self.name} | AGE: {self.age} | WEIGHT: {self.weight}")


cat1 = Cat()
cat1.set_data("Harry", 3, 5.5)

cat2 = Cat()
cat2.set_data("Joseph", 2, 4.0)

print(f"cat1.name: {cat1.name}")
cat1.show_info()
print(f"cat2.name: {cat2.name}")
cat2.show_info()
