"""
Задача 12-07. Слияние упорядоченных списков

Напишите функцию merge_sorted(a, b), которая сливает два отсортированных
списка в один отсортированный за один проход (два указателя). Встроенные
sort/sorted запрещены.

Примеры
--------
merge_sorted([1, 4], [2, 3, 5]) → [1, 2, 3, 4, 5]
"""


def merge_sorted(a, b):
    result = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # Добавляем оставшиеся элементы из списка a
    while i < len(a):
        result.append(a[i])
        i += 1

    # Добавляем оставшиеся элементы из списка b
    while j < len(b):
        result.append(b[j])
        j += 1

    return result
