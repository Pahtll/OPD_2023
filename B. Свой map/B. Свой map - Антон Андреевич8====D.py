def simple_map(function, values):
    return [function(element) for element in values]
print(simple_map(lambda x: x+ 5, [1,3,1,5,7]))


