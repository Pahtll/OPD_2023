#Считываем N,K как целые числа
N,K = map(int, input().split())
#Создаём список длиной N, состоящий из кеглей
ryad = N*['I']
for _ in range(K):
    #Считываем какие кегли сбили (от k1 до k2) и заменяем их на точки
    k1, k2 = map(int, input().split())
    for keglya in range(k1-1, k2):
        ryad[keglya] = '.'
#Переводим список в строку и выводим
print(''.join(ryad))
