"""
Задача 11-13. Из римской записи

Напишите функцию roman_decode(s), которая переводит строку с римской
записью числа (валидной) обратно в целое число. Правило вычитания: буква,
меньшая следующей, вычитается (IV = 4).

Примеры
--------
roman_decode("IX")      → 9
roman_decode("MCMXCIV") → 1994
"""


def roman_decode(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
