class MyVector:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return MyVector(self.x - other.x, self.y - other.y)
    def __mul__(self, a):
        return MyVector(self.x * a, self.y * a)
    def __rmul__(self, other):
        return MyVector.__mul__(self, other)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    def __str__(self):
        return 'MyVector({}, {})'.format(self.x, self.y)



