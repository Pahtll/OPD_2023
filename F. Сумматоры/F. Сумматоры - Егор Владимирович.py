class Summator:
    def __init__(self, n: int) -> None:
        self.sum = 0
        self.n = n
    #Трансформ ничего не меняет, изменять значения он будет в дочерних классах
    def Transform(self, n: int) -> int:
        return n
    #Сумм, очевидно суммирует все элементы от 0, до N (включительно)
    def Sum(self) -> int:
        for num in range(0, self.n + 1):
            self.sum += self.Transform(num)
        return self.sum
    
class SquareSummator(Summator):
    #Проводим инициализацию по иницаиализации класса родителя для дочерних классов
    def __init__(self, n: int) -> None:
        super().__init__(n)
        
    def Transform(self, n: int) -> int:
        return super().Transform(n**2)    

class CubeSummator(Summator):
    def __init__(self, n: int) -> None:
        super().__init__(n)
        
    def Transform(self, n: int) -> int:
        return super().Transform(n**3)

#Тесты
line = Summator(15)
square = SquareSummator(15)
cube = CubeSummator(15)

print(f"{line.Sum()} in ^1, {suqare.Sum()} in ^2 and {cube.Sum()} in ^3")