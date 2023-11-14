from math import sqrt

class MyVector(object):
    #Инициализируем координаты вектора
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    #Реализуем сложение, вычитание и умножение
    def __add__(self, other):
        return MyVector((self.x + other.x), (self.y + other.y))
    def __sub__(self, other):
        return MyVector((self.x - other.x), (self.y - other.y))
    def __mul__(self, value):
        return MyVector(self.x * value, self.y * value)
    #Метод для измерения абсолютного значения (длинны) вектора
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    #Проверка на равенство, неравенство
    def __eq__(self, other):
        if isinstance(other, MyVector):
            return self.x == other.x and self.y == other.y
        return False
    def __ne__(self, other):
        return not self != other
    #Строковое представление (то, что даётся при str(MyVector), что и делает print() при выводе в консоль)
    def __str__(self):
        return f"{abs(MyVector(self.x, self.y))}"

#Создание и тесты экземпляров класса        
v1 = MyVector(-2, 5)
v2 = MyVector(3, -4)
v_sum = v1 + v2
print(v_sum)
