from sys import stdin
from collections import Counter

bigstr = stdin.read().split()
words_count = Counter(bigstr)
sorted_words = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))

for words, c in sorted_words:
    print(words)
