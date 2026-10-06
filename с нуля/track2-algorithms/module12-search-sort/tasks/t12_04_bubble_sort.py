"""
Задача 12-04. Пузырьковая сортировка

Напишите функцию bubble_sort(items), которая возвращает НОВЫЙ отсортированный
по возрастанию список, отсортированный пузырьком. Встроенные sort/sorted
запрещены; исходный список изменять нельзя.

Примеры
--------
bubble_sort([3, 1, 2]) → [1, 2, 3]
"""


def bubble_sort(items):
    sorted_items = items.copy()
    n = len(sorted_items)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_items[j] > sorted_items[j + 1]:
                sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]

    return sorted_items
