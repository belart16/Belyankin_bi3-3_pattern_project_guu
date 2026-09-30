"""
Задача 11-08. Сколько простых на отрезке

Напишите функцию count_primes(a, b), которая возвращает количество простых
чисел на отрезке от a до b включительно (a и b могут быть любыми целыми).

Примеры
--------
count_primes(1, 10)   → 4   (2, 3, 5, 7)
count_primes(10, 20)  → 4   (11, 13, 17, 19)
"""


def count_primes(a, b):
    if a > b:
        a, b = b, a
    sieve = [True] * (b + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(b**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, b + 1, i):
                sieve[j] = False
    return sum(sieve[a:b + 1])
