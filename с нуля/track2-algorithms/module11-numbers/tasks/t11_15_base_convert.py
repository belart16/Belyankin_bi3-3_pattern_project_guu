"""
Задача 11-15 ★. В любую систему счисления

Напишите функцию base_convert(n, base), которая переводит число n ≥ 1
в систему счисления base (2 ≤ base ≤ 16) и возвращает строку. Цифры
выше девяти — буквы A–F.

Примеры
--------
base_convert(255, 16) → "FF"
base_convert(10, 2)   → "1010"
base_convert(7, 7)    → "10"
"""


def base_convert(n, base):
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")
    if base < 2 or base > 16:
        raise ValueError("base must be between 2 and 16")

    digits = "0123456789ABCDEF"
    result = ''
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result
