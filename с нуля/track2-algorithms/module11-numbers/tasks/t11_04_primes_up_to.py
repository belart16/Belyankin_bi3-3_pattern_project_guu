"""
Задача 11-04. Простые числа до N

Напишите функцию primes_up_to(n), которая возвращает список всех простых
чисел от 2 до n включительно. Способ на выбор: перебор делителей
или решето Эратосфена.

Примеры
--------
primes_up_to(10) → [2, 3, 5, 7]
primes_up_to(2)  → [2]
"""


def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]
