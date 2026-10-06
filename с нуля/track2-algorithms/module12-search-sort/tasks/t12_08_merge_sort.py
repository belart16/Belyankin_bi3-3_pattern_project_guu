"""
Задача 12-08 ★. Сортировка слиянием

Напишите функцию merge_sort(items), которая сортирует список рекурсивной
сортировкой слиянием: список делится пополам, части сортируются рекурсивно
и сливаются (слияние — как в задаче 12-07). Базовый случай: список длины
0–1 уже отсортирован. Встроенные sort/sorted запрещены.

Примеры
--------
merge_sort([5, 2, 9, 1]) → [1, 2, 5, 9]
"""


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left_half = merge_sort(items[:mid])
    right_half = merge_sort(items[mid:])

    return merge_sort(left_half, right_half)
