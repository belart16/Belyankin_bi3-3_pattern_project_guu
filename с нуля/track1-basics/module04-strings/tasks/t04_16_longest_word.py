"""
Задача 04-16 ★. Самое длинное слово

Прочитайте предложение и выведите его самое длинное слово. Если несколько
слов имеют одинаковую длину — первое из них.

Пример
------
Ввод:
я учу язык python
Вывод:
python
"""

s = input().split()
longest_word = s[0]
for word in s:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)

