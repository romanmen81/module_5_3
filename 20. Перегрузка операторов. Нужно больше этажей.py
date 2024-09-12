class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name  # Имя
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        # Метод для перехода на указанный этаж
        if new_floor < 1 or new_floor > self.number_of_floors:
            # Если этаж вне допустимых границ
            print("Такого этажа не существует")
        else:
            # Если этаж находится в допустимых границах, выводим все этажи до него
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строку с информацией о доме
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


# Создаем объекты класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Проверяем метод __str__
print(h1)
print(h2)

# Проверяем метод __eq__
print(h1 == h2)  # False

h1 = h1 + 10  # Увеличиваем этажи
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

h1 += 10  # Увеличиваем этажи (используя __iadd__)
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # Увеличиваем этажи через __radd__
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

# Проверка операторов сравнения
print(h1 > h2)  # False
print(h1 >= h2)  # True
print(h1 < h2)  # False
print(h1 <= h2)  # True
print(h1 != h2)  # False