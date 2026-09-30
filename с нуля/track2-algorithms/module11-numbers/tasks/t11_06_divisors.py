"""
Задача 11-06. Все делители

Напишите функцию divisors(n), которая возвращает список всех делителей
числа n ≥ 1 по возрастанию.

Примеры
--------
divisors(12) → [1, 2, 3, 4, 6, 12]
divisors(7)  → [1, 7]
"""


def divisors(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return sorted(divs)
