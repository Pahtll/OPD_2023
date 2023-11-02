from sys import stdin

# record = учёт. Создаем учетный словарь
record = {}

# считываем по строке из консоли
for element in stdin.readlines():
    element = element.split()

    # Клиент - ключ, для каждого клиент мы устанавливаем словарь по умолчанию
    record.setdefault(element[0], {})

    # Проверяем, существует ли элемент в словаре
    if element[1] in record[element[0]]:
        record[element[0]][element[1]] += int(element[2])
        continue

    # Если не существует, то создаем
    record[element[0]][element[1]] = int(element[2])


# Сортируем ключи (в данном случае имена) в лексиграфическом порядке 
sorted_names = sorted(record.keys())

for name in sorted_names:
    print(name + ':')

    # Сортируем ключи (в данном случае купленные товары) в лексиграфическом порядке 
    sorted_items = sorted(record[name].keys())
    
    for item in sorted_items:
        print(f"{item} {record[name][item]}")
