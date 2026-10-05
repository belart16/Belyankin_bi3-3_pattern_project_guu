"""
Задача 11-14. Двоичная запись

Напишите функцию binary_str(n), которая возвращает двоичную запись числа
n ≥ 1 строкой — циклом деления на 2, НЕ используя bin().

Примеры
--------
binary_str(5)  → "101"
binary_str(10) → "1010"
binary_str(1)  → "1"
"""


def binary_str(n):
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")
    
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result
