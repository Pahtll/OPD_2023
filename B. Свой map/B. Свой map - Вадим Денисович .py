- def map(func, values):
    new_lst = []
    for el in values:
        new_lst.append(func(el))
    return new_lst

# Можете ввести свою функцию и значения
operation = lambda x: x + 5
values = [1, 3, 1, 5, 7]

print(map(operation, values))
