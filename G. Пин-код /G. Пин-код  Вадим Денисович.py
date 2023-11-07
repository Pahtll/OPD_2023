# функция для проверки простоты числа
def isprime(n):

    # если число меньше 2, то оно непростое
    if n < 2:
        return False

    # перебираем возможные делители от 2 до n-1 
    for i in range(2, n):
        
        # если делитель найден, то число непростое, так как просто делится только на 1 и на себя
        if n % i == 0:
            return False
    return True


def check_pin(pinCode) -> str:
    a, b, c = pinCode.split('-')
    
    # проверем простоту числа, затем проверяем палидром число или нет, и 
    # после смотрим является ли число степенью. 
    if isprime(int(a)) and (b == b[::-1]) and (int(c)**0.5) % 1 == 0:
        return 'Корректен'
    return 'Некорректен'

print(check_pin(input()))
