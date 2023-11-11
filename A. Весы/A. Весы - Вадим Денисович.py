class Balance:
    '''
    При создании экземлпяра класса присваиваем ему два параметра: right и left.
    Соответсвенно, right - правая чаша, left - левая.
    '''
    def __init__(self):
        self.left = 0
        self.right = 0
    def add_right(self, value):
        self.right += value

    def add_left(self, value):
        self.left += value

    def result(self):
        if self.right == self.left: 
            return '='
        else: 
            return "R" if self.right > self.left else "L"
