"""
Задача 11-12. В римскую запись

Напишите функцию roman_encode(n), которая переводит целое число
(1 ≤ n ≤ 3999) в римскую запись. Идите по парам «значение–буквы» от больших
к меньшим (таблица в шпаргалке модуля).

Примеры
--------
roman_encode(9)    → "IX"
roman_encode(58)   → "LVIII"
roman_encode(1994) → "MCMXCIV"
"""


def roman_encode(n):
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, numeral in roman_numerals:
        while n >= value:
            result += numeral
            n -= value
    return result
