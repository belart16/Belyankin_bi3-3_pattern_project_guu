"""
Задача 05-12. Без повторов

Прочитайте числа через пробел и выведите их без повторов — каждая величина
один раз, в порядке первого появления. Множества (set) не использовать:
собирайте новый список и проверяйте наличие оператором in.

Пример
------
Ввод:
1 2 1 3 2 4
Вывод:
1 2 3 4
"""

numbers = input().split()
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(" ".join(unique_numbers))

