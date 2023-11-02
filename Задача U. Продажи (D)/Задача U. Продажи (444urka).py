from sys import stdin
#Создаём словарь и считываем консоль подстрочно, добавляя в словарь в качестве ключа имя, а в качестве значения ещё один словарь в котором ключ - предмет покупки, а значение - список с количеством покупок этого товара
dictionary = {}
for buy in stdin.readlines():
    buy = buy.split()
    dictionary.setdefault(buy[0], {}).setdefault(buy[1],[]).append(int(buy[2]))
#Cортируем ключи внешнего словаря в лексикографическом порядке и выводим их
for name in list(sorted(dictionary.keys())):
    print(name + ':')
    #Сортируем ключи внутреннего соваря в лексикографическом порядке, затем выводим их и сумму списка значений
    for buy in list(sorted(dictionary[name].keys())):
        print(buy, sum(dictionary[name][buy]))


