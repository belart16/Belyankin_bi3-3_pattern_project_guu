"""
Задача 06-16 ★. Первое уникальное слово

Прочитайте слова через пробел и выведите первое слово, которое встречается
в тексте ровно один раз. Если такого нет, выведите «-».

Пример
------
Ввод:
а б а в б г
Вывод:
в
"""

words = input().split()
word_count = {}
for word in words:  
    word_count[word] = word_count.get(word, 0) + 1

for word in words:
    if word_count[word] == 1:
        print(word)
        break
else:
    print("-")

