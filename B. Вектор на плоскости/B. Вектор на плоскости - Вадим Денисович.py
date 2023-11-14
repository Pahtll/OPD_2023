from math import sqrt

class MyVector:

    # Экземпляр класс передает значения для параметров x и y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Специальная функция сложения, когда складывается два вектора
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return MyVector(self.x, self.y)

    # Специальная функция вычитания, когда вычитается два вектора
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return MyVector(self.x, self.y)

    # Умножение вектора на константу
    def __mul__(self, other):
        self.x *= other
        self.y *= other
        return MyVector(self.x, self.y)

    # Если константа стоит справа: 3 * MyVector
    def __rmul__(self, other):
        return MyVector.__mul__(self, other)

    # Вывод координат вектора
    def result(self):
        return (self.x, self.y)

    # Вывод длины вектора
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Сравнение на равенство
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Сравнение на неравенство
    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    # Вывод в консоль вектора
    def __str__(self):
        return f'MyVector({self.x}, {self.y})'
