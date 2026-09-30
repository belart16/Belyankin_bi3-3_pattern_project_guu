"""
Задача 11-03. Простые множители

Напишите функцию prime_factors(n), которая возвращает список простых
множителей числа n (n ≥ 2) с учётом кратности, по возрастанию.

Примеры
--------
prime_factors(100) → [2, 2, 5, 5]
prime_factors(13)  → [13]
"""


def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
