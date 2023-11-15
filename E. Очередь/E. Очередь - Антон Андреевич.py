class Queue:
    def __init__(self, *args):
        #*args - позволяет добавить в очередь произвольное количество элементов
        self.queue = list(args)
    
    def __add__(self, other):
        """queue1+queue2 – склейка очередей создаёт новую увеличенную очередь."""
        return Queue(*self.queue, *other.queue)

    def __iadd__(self, other):
        """queue1+=queue2 – расширяет первую очередь второй."""
        self.queue.extend(other.queue)
        return self

    def __eq__(self, other):
        """queue1==queue2 – проверяет очереди на равенство всех элементов. Возвращает True или False."""
        return self.queue == other.queue

    def __rshift__(self, N):
        """queue>>N – создаёт новую очередь без первых N (вышедших) элементов. В случае, когда N превышает количество элементов очереди, следует вернуть пустую очередь."""
        if N <= len(self.queue):
            return Queue(*self.queue[N:])
        else: 
            return None

    def append(self, *nums):
        """append(∗values) – добавляет несколько значений в конец очереди (как минимум одно)."""
        for num in list(nums):
            self.queue.append(num)

    def copy(self):
        """copy() – создаёт копию данной очереди, то есть возвращает новую очередь, полностью аналогичную исходной."""
        return Queue(*self.queue)
    
    def pop(self):
        """Если длина листа с значениями очереди больше 0, то при помощи встроенного в листы метода .pop() возвращаем 
        первый элемент листа и убираем его"""
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def extend(self, other):
        """extend(queue) – расширяет данную очередь другой, то есть приклеивает вторую очередь к первой."""
        self.queue.extend(other.queue)

    def next(self):
        """next() – возвращает новую очередь, начинающуюся со второго элемента текущей."""
        return Queue(*self.queue[1:])

    def __next__(self):
        """next(queue) – аналогичное действие методу next()"""
        return Queue(*self.queue[1:])
        
    def __str__(self):
        """Выводим лист добавляя -> при помощи метода .join. Добавляем в начало и конец строки квадратные скобочки"""
        return '[' + ' -> '.join(str(num) for num in self.queue) + ']'

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = "\n")
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)


        