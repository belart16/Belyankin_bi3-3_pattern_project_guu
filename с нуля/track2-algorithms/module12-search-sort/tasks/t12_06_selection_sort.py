"""
Задача 12-06. Сортировка выбором

Напишите функцию selection_sort(items), которая возвращает НОВЫЙ
отсортированный список: на каждом шаге ищите минимум в неотсортированном
остатке и ставьте его на место. Встроенные sort/sorted запрещены.

Примеры
--------
selection_sort([3, 1, 2]) → [1, 2, 3]
"""


def selection_sort(items):
    sorted_items = items.copy()
    n = len(sorted_items)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_items[j] < sorted_items[min_index]:
                min_index = j
        sorted_items[i], sorted_items[min_index] = sorted_items[min_index], sorted_items[i]

    return sorted_items
