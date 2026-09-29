"""
Задача 05-13. Соседние равные

Прочитайте числа через пробел и выведите True, если в списке есть два
соседних равных элемента, иначе False.

Пример
------
Ввод:
1 2 2 3
Вывод:
True
"""

numbers = list(map(int, input().split()))
has_neighbors = False
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1]:
        has_neighbors = True
        break
print(has_neighbors)
