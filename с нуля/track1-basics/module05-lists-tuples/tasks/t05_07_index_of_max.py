"""
Задача 05-07. Где максимум

Прочитайте числа через пробел (гарантируется хотя бы одно) и выведите
индекс первого максимального числа. Нумерация с нуля.

Пример
------
Ввод:
3 7 10 4 10
Вывод:
2
"""

numbers = list(map(int, input().split()))
max_value = max(numbers)
index_of_max = numbers.index(max_value)
print(index_of_max)

