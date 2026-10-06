"""
Задача 12-02. Бинарный поиск

Напишите функцию binary_search(items, x), которая ищет x в ОТсортированном
списке бинарным поиском и возвращает индекс или −1. Методом index
и перебором пользоваться нельзя — только деление диапазона пополам.

Примеры
--------
binary_search([1, 3, 5, 7, 9], 7) → 3
binary_search([1, 3, 5, 7, 9], 4) → -1
"""


def binary_search(items, x):
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == x:
            return mid
        elif items[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1
