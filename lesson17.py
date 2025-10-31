# LESSON #17. Наследование, инкапсуляция, полиморфизм

class Building:
    city = None
    year = None

    def __init__(self, city, year):
        self.city = city
        self.year = year

    def show_info(self):
        print(
            f"City: {self.city}\n"
            f"Year: {self.year}")


class School(Building):
    students = None

    def __init__(self, city, year, students):
        super(School, self).__init__(city, year)
        self.students = students

    def show_info(self):
        super().show_info()
        print(f"Students: {len(self.students)}")


class House(Building):
    residents = None

    def __init__(self, city, year, residents):
        super(House, self).__init__(city, year)
        self.residents = residents

    def show_info(self):
        super().show_info()
        print(f"Residents: {len(self.residents)}")


class Shop(Building):
    goods = None

    def __init__(self, city, year, goods):
        super(Shop, self).__init__(city, year)
        self.goods = goods

    def show_info(self):
        super().show_info()
        print(f"Goods: {self.goods}")


school = School('Київ', 1990, ['Андрій', 'Максим', 'Олексій'])
house = House('Харків', 2010, ['Володимир', 'Оксана', 'Олександр'])
shop = Shop('Львів', 2020, ['Ноутбук', 'Смартфон', 'Навушники'])

school.show_info()
house.show_info()
shop.show_info()
