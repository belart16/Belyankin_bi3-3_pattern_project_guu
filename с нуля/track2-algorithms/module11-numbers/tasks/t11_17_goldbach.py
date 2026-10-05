"""
Задача 11-17 ★. Гипотеза Гольдбаха

Напишите функцию goldbach(n), которая для чётного n ≥ 4 возвращает кортеж
(p, q) двух простых чисел с суммой n; при нескольких вариантах берите
наименьшее p (тогда q наибольшее).

Примеры
--------
goldbach(4)  → (2, 2)
goldbach(10) → (3, 7)
goldbach(26) → (3, 23)
"""


def goldbach(n):
    if n < 4 or n % 2 != 0:
        raise ValueError("n must be an even number greater than or equal to 4")

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for p in range(2, n):
        q = n - p
        if is_prime(p) and is_prime(q):
            return (p, q)
