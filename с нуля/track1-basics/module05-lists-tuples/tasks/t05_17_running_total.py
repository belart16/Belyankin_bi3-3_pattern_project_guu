"""
Задача 05-17 ★. Частичные суммы

Прочитайте числа через пробел и выведите их частичные суммы одной строкой
через пробел: первое число, сумма первых двух, сумма первых трёх и т.д.

Пример
------
Ввод:
1 2 3 4
Вывод:
1 3 6 10
"""

numbers = list(map(int, input().split()))
partial_sums = []
current_sum = 0
for num in numbers:
    current_sum += num
    partial_sums.append(current_sum)
print(" ".join(map(str, partial_sums)))

