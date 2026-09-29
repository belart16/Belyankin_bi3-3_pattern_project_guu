"""
Задача 06-14. Голосование

Прочитайте целое число n, затем n строк — имена проголосовавших (по одному
имени в строке). Выведите победителя и число голосов: «имя количество».

Победитель — набравший больше всех голосов; если сразу несколько набрали
максимум, побеждает имя, идущее раньше по алфавиту.

Пример
------
Ввод:
5
борис
анна
борис
анна
анна
Вывод:
анна 3
"""


votes = {}
n = int(input())
for _ in range(n):
    name = input().strip()
    votes[name] = votes.get(name, 0) + 1

max_votes = max(votes.values())
winners = [name for name, count in votes.items() if count == max_votes]
winner = min(winners)  

print(f"{winner} {max_votes}")
