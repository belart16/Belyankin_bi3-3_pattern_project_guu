"""
Задача 11-05. Число-палиндром

Напишите функцию is_palindrome_num(n), которая возвращает True, если
целое число n (n ≥ 0) одинаково читается в обе стороны. Строками
пользоваться можно (в отличие от задачи модуля 3).

Примеры
--------
is_palindrome_num(12321) → True
is_palindrome_num(123)   → False
"""


def is_palindrome_num(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num
