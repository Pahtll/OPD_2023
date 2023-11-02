dict = {}
for i in range(int(input())):
    str = input().split()
    country = str[0]
    lst = str[1:]
    for i in lst:
        dict[i] = country
for j in range(int(input())):
    print(dict[input()])
