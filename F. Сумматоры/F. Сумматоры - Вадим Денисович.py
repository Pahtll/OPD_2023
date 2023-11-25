class Summator:
    def __init__(self, n):
        self.n = n

    def _transform(self, n):
        return n

    def Sum(self):
        sum = 0
        for i in range(1, self.n+1):
            sum += self._transform(i)
        return sum

class SquareSummator(Summator):
    def __init__(self, n):
        self.n = n

    def _transform(self, n):
        return n**2

class CubeSummator(Summator):
    def __init__(self, n):
        self.n = n

    def _transform(self, n):
        return n**3

# здесь делать проверки
c = SquareSummator(3)
print(c.Sum())

