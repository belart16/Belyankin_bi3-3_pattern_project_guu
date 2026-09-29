"""
Задача 06-13. Общие буквы

Прочитайте две строки и выведите буквы, которые встречаются в обеих
(без учёта регистра, без пробелов, каждая буква один раз), — по алфавиту,
через пробел. Если общих букв нет, ничего не выводите.

Пример
------
Ввод:
мама
папа
Вывод:
а
"""

first_string = input().lower().replace(" ", "")
second_string = input().lower().replace(" ", "")

first_set = set(first_string)
second_set = set(second_string)

common_letters = first_set & second_set

if common_letters:
    print(" ".join(sorted(common_letters)))
