def Map(func, value: list) -> list:
    lst = []
    for things in value:
        lst.append(func(things))
    return lst

lst = [1, 3, 6]
print(Map(lambda x: x + 5, lst))