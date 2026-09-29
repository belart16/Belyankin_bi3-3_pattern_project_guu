"""
Задача 06-17 ★. Сумма пары

Прочитайте строку с числами через пробел, затем отдельной строкой — целое
число target. Найдите два элемента списка, сумма которых равна target,
и выведите их индексы (нумерация с нуля) через пробел: «i j», где i < j.
Гарантируется, что подходящая пара ровно одна.

Пример
------
Ввод:
2 7 11 15
9
Вывод:
0 1
"""

numbers = list(map(int, input().split()))
target = int(input())
num_to_index = {}
for i, num in enumerate(numbers):
    complement = target - num
    if complement in num_to_index:
        print(num_to_index[complement], i)
        break
    num_to_index[num] = i

