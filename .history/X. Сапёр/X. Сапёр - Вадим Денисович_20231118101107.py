# n - строк, m - столбцов, k - кол-во мин на поле
n, m, k = [int(x) for x in input().split()]
indexes = []
mines = [tuple(map(int, input().split())) for _ in range(k)]
field = {i:{} for i in range(1, n+1)} # тут i - строка
for el in field:
    for i in range(1, m+1): # тут i - столбец
        field[el][i] = 0
        indexes.append((el,i))

# n1 - строки, m1 - столбцы
for n1, m1 in indexes:
    if (n1, m1) in mines:
        field[n1][m1] = "*"

for n1, m1 in indexes:

    # проверка на мину
    if (n1, m1) in mines:
        continue

    # угловые цифры, максимум 3 мины в окружении
    if n1 == 1 and m1 == 1:
        field[n1][m1] += (field[n1+1][m1] == '*') + (field[n1+1][m1+1] == '*') + (field[n1][m1+1] == '*')
    elif n1 == 1 and m1 == m:
        field[n1][m1] += (field[n1+1][m1] == '*') + (field[n1+1][m1-1] == '*') + (field[n1][m1-1] == '*')
    elif n1 == n and m1 == 1:
        field[n1][m1] += (field[n1-1][m1] == '*') + (field[n1-1][m1+1] == '*') + (field[n1][m1+1] == '*')
    elif n1 == n and m1 == m:
        field[n1][m1] += (field[n1-1][m1] == '*') + (field[n1-1][m1-1] == '*') + (field[n1][m1-1] == '*')

    # цифры в верхней или нижней строках, максимум 5 мин в окружении
    elif n1 == 1 and 1 < m1 < m:
        field[n1][m1] += ((field[n1 + 1][m1] == '*') + (field[n1 + 1][m1 + 1] == '*') + (field[n1 + 1][m1 - 1] == '*')
            + (field[n1][m1 + 1] == '*') + (field[n1][m1 - 1] == '*'))
    elif n1 == n and 1 < m1 < m:
        field[n1][m1] += ((field[n1][m1 + 1] == '*') + (field[n1][m1 - 1] == '*') + (field[n1 - 1][m1 - 1] == '*') +
                (field[n1 - 1][m1] == '*') + (field[n1 - 1][m1 + 1] == '*'))

    # цифры в первом и последнем столбцах, максимум 5 цифр в окружении
    elif 1 < n1 < n and m1 == 1:
        field[n1][m1] += ((field[n1 + 1][m1] == '*') + (field[n1 + 1][m1 + 1] == '*') +
                          (field[n1][m1 + 1] == '*') + (field[n1 - 1][m1] == '*') + (field[n1 - 1][m1 + 1] == '*'))
    elif 1 < n1 < n and m1 == m:
        field[n1][m1] += (
                    (field[n1 + 1][m1] == '*') + (field[n1 + 1][m1 - 1] == '*') + (field[n1][m1 - 1] == '*') +
                    (field[n1 - 1][m1 - 1] == '*') + (field[n1 - 1][m1] == '*'))

    # цифры не в углах, не в верхней, не в нижней строках, не в крайних столбцах, максимум 8 мин в окружении
    else:
        field[n1][m1] += ((field[n1+1][m1] == '*') + (field[n1+1][m1+1] == '*') + (field[n1+1][m1-1] == '*') +
                          (field[n1][m1+1] == '*') + (field[n1][m1-1] == '*') +
                          (field[n1-1][m1-1] == '*') + (field[n1-1][m1] == '*') + (field[n1-1][m1+1] == '*'))

for el in field:
    for el1 in field[el]:
        print(field[el][el1], end=" ")
    print()