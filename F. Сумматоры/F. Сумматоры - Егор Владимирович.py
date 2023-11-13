class Summator:
    def __init__(self, n: int) -> None:
        self.sum = 0
        self.n = n
    def Transform(self, n: int) -> int:
        return n
    def Sum(self) -> int:
        for num in range(0, self.n + 1):
            self.sum += self.Transform(num)
        return self.sum
    
class SquareSummator(Summator):
    def __init__(self, n: int) -> None:
        self.sum = 0
        self.n = n
    def Transform(self, n: int) -> int:
        return super().Transform(n**2)    

class CubeSummator(Summator):
    def __init__(self, n: int) -> None:
        self.sum = 0
        self.n = n
    def Transform(self, n: int) -> int:
        return super().Transform(n**3)
    
cube = CubeSummator(15)
square = SquareSummator(15)

print(f"{cube.Sum()} in ^3 and {square.Sum()} in ^2")
 