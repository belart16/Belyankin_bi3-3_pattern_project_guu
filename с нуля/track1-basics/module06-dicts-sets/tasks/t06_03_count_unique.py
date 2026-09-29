"""
Задача 06-03. Сколько различных

Прочитайте числа через пробел и выведите, сколько среди них различных.

Пример
------
Ввод:
3 1 3 2 1
Вывод:
3
"""

numbers = input().split()
unique_numbers = set(numbers)
print(len(unique_numbers))

