from sys import stdin

# функция для сортировки, которая подсчитывает все порядковые номера символов, а потом выводит их сумму
def codeSymbols(word):
    sum_codes = 0

    # Считаем порядковые номера каждых букв, где A - 1, Z - 26
    # Далее добавляем в сумму порядковый номер символа
    # Используем метод .upper() поскольку работаем с заглавными буквами в таблице ASCII
    for symbol in word.upper():
        sum_codes += ord(symbol) - ord('A') + 1
        
    return sum_codes

words = [word for word in stdin.read().split()]

print(*[word for word in sorted(words, key=codeSymbols)], sep='\n')
