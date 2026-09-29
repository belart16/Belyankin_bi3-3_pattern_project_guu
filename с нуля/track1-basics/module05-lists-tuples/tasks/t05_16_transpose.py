"""
Задача 05-16 ★. Транспонирование матрицы

Прочитайте два целых числа n и m (каждое с отдельной строки), затем n строк
матрицы — по m целых чисел через пробел. Выведите транспонированную
матрицу: m строк по n чисел — столбцы исходной становятся строками.

Пример
------
Ввод:
2
3
1 2 3
4 5 6
Вывод:
1 4
2 5
3 6
"""

n = int(input())
m = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for j in range(m):
    row = [matrix[i][j] for i in range(n)]
    print(" ".join(map(str, row)))
