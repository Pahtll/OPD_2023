# преображаем позицию в более понятный вид [x, y]
def makeover(pos):
    makeovered_pos = [ord(pos[0]) - ord('A') + 1, int(pos[1])]
    return makeovered_pos

# возвращаем позицию в исходный вид, допустим, 'A2'
def unmakeover(makeovered_turn):
    return f'{chr(makeovered_turn[0]+64)}{makeovered_turn[1]}'

def list_of_turns(start_pos):
    # получаем координаты начальной позиции
    x, y = makeover(start_pos)

    # прикидываем все возможные варианты ходов от начальной позиции
    sample = [(x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1), (x - 1, y - 2), (x + 1, y - 2),
              (x + 2, y + 1), (x + 2, y - 1)]

    # добавляем в список только те ходы, которые можно сделать
    turns = [unmakeover(el) for el in sample if ((1 <= el[0] <= 8) and (1 <= el[1] <= 8))]
    return turns

print(list_of_turns(input()))
