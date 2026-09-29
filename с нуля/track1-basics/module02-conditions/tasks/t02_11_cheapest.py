"""
Задача 02-11. Самая дешёвая цена

Прочитайте три цены (это дробные числа) и выведите наименьшую.
Функцией min не пользоваться — только сравнения.

Обратите внимание: цены читаются как float, поэтому целая цена
напечатается с десятичной частью (см. пример).

Пример
------
Ввод:
250
199
300
Вывод:
199.0
"""

price1 = float(input())
price2 = float(input())
price3 = float(input())

if price1 <= price2 and price1 <= price3:
    print(price1)
elif price2 <= price1 and price2 <= price3:
    print(price2)
else:
    print(price3)
