n, words = int(input()), {} #Вадим сколько мне ждать мой блант?
for _ in range(n):
    el = input().replace("-",'').replace(',','').split()
    for i in range(1, len(el)):
        if el[i] not in words:
            words[el[i]] = [el[0]]
        else:
            words[el[i]] += [el[0]]
words, res, tres = sorted([(ell, words[ell]) for ell in words]), '', ''
for el in words:
    tres += f'{el[0]} - '
    if len(el[1]) > 1:
        for n in el[1]:
            tres += f'{n}, '
        tres = tres[:-2]
    else:
        tres += f'{el[1][0]}'
    tres += '\n'
    res += tres
    tres = ''
print(len(words), res, sep='\n')
