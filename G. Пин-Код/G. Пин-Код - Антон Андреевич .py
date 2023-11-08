from math import log
#Проверка на простое число
def isPrime(a):
    d = 2
    while a % d != 0:
        d+=1
    return d==a
def check_pin(pinCode):
    #Делим строку на 3 числа
    ListPins = pinCode.split('-')
    #Первое число проверяем на простоту, второе число проверяем на палиндром, проверяем являетя ли третье число степенью двойки при помощи логарифма
    if isPrime(int(ListPins[0])) and  ListPins[1] == ListPins[1][::-1] and log(int(ListPins[2]),2)  %  1 == 0:
        return 'Корректен'
    else:
        return 'Некорректен'