from math import log
def primal(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_pincode(pinCode):
    pin = pinCode.split('-')
    return "Корректен" if primal(int(pin[0])) and (pin[1] == pin[1][::-1]) and (log(int(pin[2]), 2) % 1 == 0) else "Некорректен"

print(check_pincode(input()))
