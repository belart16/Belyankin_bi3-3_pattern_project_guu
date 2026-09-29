"""
Задача 06-11. Только в первой

Прочитайте две строки с числами через пробел. Выведите числа, которые есть
в первой строке, но отсутствуют во второй, — по возрастанию, через пробел.
Если таких нет, ничего не выводите.

Пример
------
Ввод:
1 3 5 7
3 7
Вывод:
1 5
"""

first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))
difference = first_set - second_set
if difference:
    print(" ".join(map(str, sorted(difference))))
    
    
