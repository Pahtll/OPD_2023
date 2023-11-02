dictionary = dict()
lst2 = []
for i in (range(int(input()))):
    lst1 = input().replace("-","").replace(",","").split()
    lst2.append(' '.join(lst1[1:]))
    for j in range(1,len(lst1)):
        dictionary.setdefault(lst1[j], []).append(lst1[0])
lst2 = sorted(set(' '.join(lst2).split()))
print(len(lst2))
for i in lst2:
    print(i , "-", ", ".join(dictionary[i]))
