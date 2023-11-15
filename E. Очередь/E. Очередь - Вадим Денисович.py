class Queue:
    # Получает в качестве аргумента список и по символьно перебираем его через list comprehension, добавляя в атрибут list
    def __init__(self, *args):
        self.list = [el for el in args]

    # Создаем переменную copy, которая содержит в себе неизменяемый элемент - кортеж, чтобы последующие изменения копируемого списка не
    # влияли на скопированный элемент. 
    def copy(self):
        copy = tuple(self.list)
        return Queue(*list(copy))

    # Удаляем первый элемент из списка и возвращаем его.
    def pop(self):
        if len(self.list) == 0: return None
        else:
            returned = self.list[0]
            del self.list[0]
            return returned

    # Внутренняя функция для получения списка другого класса в функции extend().
    def _returnList(self):
        return self.list

    # добавляет элементы путем создания нового списка через list comprehension и присоединением к другому списку. 
    def append(self, *args):
        self.list += [el for el in args]

    # Возвращаем новую очередь, где список уже без первого элемента, если длина списка > 0, иначе возвращаем None
    def next(self):
        if len(self.list) == 0: return None
        else: return Queue(*self.list[1:])

    # Добавляем одну очередь к другой. Но поскольку в данном случае мы работаем с классами, мы вынуждены прописать внутренную ф-ию _returnList()
    def extend(self, cls):
        self.list += cls._returnList()

    # Добавляем к одному из списков класса, а потом возвращаем новую очередь с измененым списком, раскрывая список поэлементно. 
    def __add__(self, other):
        self.list += other.list
        return Queue(*self.list)

    # То же самое сложение, что и выше, только в виде "+=". Добавляем к списку одного класса список другого и возвращаем очередь. 
    def __iadd__(self, other):
        self.list += other.list
        return self

    # Проверяем на схожесть очереди.
    def __eq__(self, other):
        return self.list == other.list

    # В виде знака побитового сдвига ">>" мы смещаем очередь на N число (в параметрах функции оно указано, как other) 
    def __rshift__(self, other):
        return Queue(*self.list[other:])

    # То же самое, что и next(), только это для уже имеющейся функции у Python
    def __next__(self):
        return self.next()

    # Метод __str__ срабатывает, когда мы передаем экземпляр класса в качестве аргумента функции print().
    # Если список очереди пустой, то возвращается пустой список.
    # У нас есть параметр по умолчанию lst = 0, если он не передается в функцию, то lst = self.list, или же lst = передаваемому значению.
    # Возвращаем строку в виде "[1 -> 2 -> 3 -> ... -> n]"
    def __str__(self, lst=0):

        if lst == 0: lst = self.list
        if len(lst) == 0: return []

        done = '['
        for el in lst:
            done += f'{el} -> '
        done = done[:-4] + ']'
        return done


# Тесты для проверки работоспособности кода 
q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q1, id(q1) == id(q2))
q3 = q2.next()
print(q3)
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
