"""
Задача 06-06. Частоты букв

Прочитайте строку и посчитайте частоты букв (без учёта регистра, пробелы
не считать). Выведите «буква: количество» построчно, буквы — по алфавиту.

Пример
------
Ввод:
мама
Вывод:
а: 2
м: 2
"""

text = input().lower()
letter_counts = {}
for char in text:
    if char != " ":
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

for letter in sorted(letter_counts):
    print(f"{letter}: {letter_counts[letter]}")
