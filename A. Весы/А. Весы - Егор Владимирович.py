class Balance:
    def __init__(self): 
        self.left = 0
        self.right = 0
    def add_right(self, value: int) -> int:
        self.right = self.right + value
        return self.right
    def add_left(self, value: int) -> int:
        self.left = self.left + value
        return self.left
    def result(self) -> int:
        if(self.left == self.right): 
            return '='
        else:
            return 'L' if self.left > self.right else 'R'
    
balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())