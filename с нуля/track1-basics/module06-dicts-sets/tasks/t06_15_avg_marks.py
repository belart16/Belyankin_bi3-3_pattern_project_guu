"""
Задача 06-15. Средний балл

Прочитайте целое число n, затем n строк «имя предмет оценка» (имя и предмет —
одно слово, оценка — целое число). Для каждого студента выведите средний
балл по его предметам (round 2): строку «имя среднее». Студенты — в порядке
первого появления.

Пример
------
Ввод:
3
анна матем 5
борис физика 4
анна физика 3
Вывод:
анна 4.0
борис 4.0
"""

marks = {}
n = int(input())
for _ in range(n):
    name, subject, grade = input().split()
    grade = int(grade)
    if name not in marks:
        marks[name] = []
    marks[name].append(grade)

for name in marks:
    avg = round(sum(marks[name]) / len(marks[name]), 2)
    print(f"{name} {avg}")
