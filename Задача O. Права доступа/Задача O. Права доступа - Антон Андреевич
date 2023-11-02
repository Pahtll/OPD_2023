#Создаем функцию для проверки соответсвия доступа
def checkAccess(str):
    if str in dictionary[operation[1]]:
        print('OK')
    else:
        print('Access denied')

#Создаём словарь в который как ключи помещаем названия файлов, а как запросы помещаем допустимые операции
dictionary = {}
for _ in range(int(input())):
    lst = input().split()
    dictionary[lst[0]] = lst[1:]

#Считываем операции в отдельный лист, и каждую операцию сплитаем, получая подсписок, в котором нулевой элемент - это запрашиваемая операция
operations = []
for _ in range(int(input())):
    operations.append(input().split())

#Затем проверяем на соответствие, используя функцию
for operation in operations:
    if operation[0] == 'write':
        checkAccess('W')
    elif operation[0] ==  'read':
        checkAccess('R')    
    elif operation[0] ==  'execute':
        checkAccess('X')
