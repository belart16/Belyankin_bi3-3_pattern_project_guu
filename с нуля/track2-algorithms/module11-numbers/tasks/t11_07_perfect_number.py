"""
Задача 11-07. Совершенное число

Напишите функцию perfect_number(n), которая возвращает True, если n равно
сумме своих делителей, меньших n (например, 6 = 1 + 2 + 3).

Примеры
--------
perfect_number(6)  → True
perfect_number(28) → True
perfect_number(12) → False
"""


def perfect_number(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i and n // i != n:
                divs.append(n // i)
    return sum(divs) == n
