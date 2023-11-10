from math import sqrt

class MyVector(object):
    #�������������� ���������� �������
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    #��������� ��������, ��������� � ���������
    def __add__(self, other):
        return MyVector((self.x + other.x), (self.y + other.y))
    def __sub__(self, other):
        return MyVector((self.x - other.x), (self.y - other.y))
    def __mul__(self, value):
        return MyVector(self.x * value, self.y * value)
    #����� ��� ��������� ����������� �������� (������) �������
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    #�������� �� ���������, �����������
    def __eq__(self, other):
        if isinstance(other, MyVector):
            return self.x == other.x and self.y == other.y
        return False
    def __ne__(self, other):
        return not self == other
    #��������� ������������� (��, ��� ����� ��� str(MyVector), ��� � ������ print() ��� ������ � �������)
    def __str__(self):
        return f"{abs(MyVector(self.x, self.y))}"

#�������� � ����� ����������� ������        
v1 = MyVector(-2, 5)
v2 = MyVector(3, -4)
v_sum = v1 + v2
print(v_sum)