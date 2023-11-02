# считываем каждую строку и разделяем по проблему название файла и операции 
files = [input().split() for _ in range(int(input()))]

# вносим доступные операции для конкретного файла
available_operations = {el[0]:el[1:] for el in lst}

# считываем строки с проделываемыми операциями в виде списка ['операция', 'название файла']
operations = [input().split() for _ in range(int(input()))]

# пробегаем по проделываемым операциям над файлами
for el in operations:
    if el[1] not in a:
        print('не существует')
        exit()
    elif el[0] == "read" and "R" in available_operations[el[1]]:
        print("OK")
    elif el[0] == "write" and "W" in available_operations[el[1]]:
        print("OK")
    elif el[0] == "execute" and "X" in available_operations[el[1]]:
        print("OK")
    else:
        print("Access denied")
