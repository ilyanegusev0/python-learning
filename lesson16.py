# LESSON #16. Конструкторы, переопределение методов

class Cat:
    name = None
    age = None
    weight = None

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def set_data(self, name=None, age=None, weight=None):
        self.name = name
        self.age = age
        self.weight = weight

    def show_info(self):
        print(f"NAME: {self.name} | AGE: {self.age} | WEIGHT: {self.weight}")


cat1 = Cat("Harry", 3, 5.5)
cat2 = Cat("Joseph", 2, 4.0)

cat1.show_info()
cat2.show_info()

cat1.set_data(age=4)
cat2.set_data(weight=4.5)

cat1.show_info()
cat2.show_info()
