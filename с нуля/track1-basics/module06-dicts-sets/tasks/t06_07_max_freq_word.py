"""
Задача 06-07. Самое частое слово

Прочитайте предложение и выведите самое часто встречающееся слово.
Гарантируется, что такое слово ровно одно.

Пример
------
Ввод:
a b a c a b
Вывод:
a
"""

sentence = input().split()
word_counts = {}
for word in sentence:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

