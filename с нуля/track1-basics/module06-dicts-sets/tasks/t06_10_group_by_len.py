"""
Задача 06-10. Группировка по длине

Прочитайте слова через пробел и сгруппируйте их по длине. Выведите строки
«длина: слова через пробел» — длины по возрастанию, слова внутри группы
в порядке появления.

Пример
------
Ввод:
кот дом дерево
Вывод:
3: кот дом
6: дерево
"""

words = input().split()
length_groups = {}
for word in words:
    length = len(word)
    if length in length_groups:
        length_groups[length].append(word)
    else:
        length_groups[length] = [word]

for length in sorted(length_groups):
    print(f"{length}: {' '.join(length_groups[length])}")
