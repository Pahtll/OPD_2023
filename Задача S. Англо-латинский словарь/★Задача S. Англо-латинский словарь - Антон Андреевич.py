dictionary = {}
set = set()
for i in (range(int(input()))):
    words = input().replace("-","").replace(",","").split()
    for j in range(1, len(words)):
        # добавляем во множество, чтобы пробегать только по уникальным элементам
        set.add(words[j])
        dictionary.setdefault(words[j], []).append(words[0])
print(len(set))
for i in sorted(set):
    print(i , "-", ", ".join(dictionary[i]))

# Структура кода заложена Антоном Андреевичем, оптимизация выполнена Вадимом Денисовичем.
