class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for i, coefficient in enumerate(self.coefficients):
            result += coefficient * (x ** i)
        return result

    def __add__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            coefficients = self.coefficients.copy()
            for i, coefficient in enumerate(other.coefficients):
                coefficients[i] += coefficient
        else:
            coefficients = other.coefficients.copy()
            for i, coefficient in enumerate(self.coefficients):
                coefficients[i] += coefficient
        return Polynomial(coefficients)

# Проверки
poly = Polynomial([10, -1])
print(poly(2))
