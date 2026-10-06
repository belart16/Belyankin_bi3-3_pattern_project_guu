"""
Задача 12-05. Сортировка вставками

Напишите функцию insertion_sort(items), которая возвращает НОВЫЙ
отсортированный список, сортируя вставками (встроенные sort/sorted
запрещены, исходный список не менять).

Примеры
--------
insertion_sort([3, 1, 2]) → [1, 2, 3]
"""


def insertion_sort(items):
    sorted_items = items.copy()
    n = len(sorted_items)

    for i in range(1, n):
        key = sorted_items[i]
        j = i - 1
        while j >= 0 and sorted_items[j] > key:
            sorted_items[j + 1] = sorted_items[j]
            j -= 1
        sorted_items[j + 1] = key

    return sorted_items
