"""
Задача 06-02. Частоты слов

Прочитайте предложение и посчитайте, сколько раз встречается каждое слово.
Выведите «слово количество» построчно — в порядке первого появления слова
в предложении.

Пример
------
Ввод:
мама мыла раму мама
Вывод:
мама 2
мыла 1
раму 1
"""

sentence = input().split()
word_counts = {}
for word in sentence:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word in sentence:
    if word in word_counts:
        print(f"{word} {word_counts[word]}")
        del word_counts[word]
