"""
Задача 06-09. Обратный словарь

Прочитайте целое число n, затем n строк «английское русское». Постройте
обратный словарь (русское → английское) и выведите его пары «ключ: значение»
построчно, отсортировав по ключу (русские слова — по алфавиту).

Пример
------
Ввод:
3
one один
two два
three три
Вывод:
два: two
один: one
три: three
"""

n = int(input())
forward_dict = {}
for _ in range(n):
    english, russian = input().split()
    forward_dict[english] = russian

reverse_dict = {v: k for k, v in forward_dict.items()}

for key in sorted(reverse_dict):
    print(f"{key}: {reverse_dict[key]}")
