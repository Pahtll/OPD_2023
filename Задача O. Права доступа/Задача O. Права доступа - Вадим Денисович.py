lst = [input().split() for _ in range(int(input()))]
opp = {el[0]:el[1:] for el in lst}
lst2 = [input().split() for _ in range(int(input()))]

for el in lst2:
    if el[1] not in opp:
        print('не существует')
        exit()
    elif el[0] == "read" and "R" in opp[el[1]]:
        print("OK")
    elif el[0] == "write" and "W" in opp[el[1]]:
        print("OK")
    elif el[0] == "execute" and "X" in opp[el[1]]:
        print("OK")
    else:
        print("Access denied")
