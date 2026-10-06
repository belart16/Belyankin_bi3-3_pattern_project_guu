"""
Задача 12-09 ★. Быстрая сортировка

Напишите функцию quick_sort(items), которая сортирует список быстрой
сортировкой: выберите опорный элемент (например, первый), разложите
остальные на «меньшие», «равные», «большие» и рекурсивно отсортируйте
крайние части. Встроенные sort/sorted запрещены.

Примеры
--------
quick_sort([5, 2, 9, 1]) → [1, 2, 5, 9]
"""


def quick_sort(items):
    if len(items) <= 1:
        return items

    pivot = items[0]
    less_than_pivot = [x for x in items[1:] if x < pivot]
    equal_to_pivot = [x for x in items if x == pivot]
    greater_than_pivot = [x for x in items[1:] if x > pivot]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)
