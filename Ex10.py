# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input("Введите количество монет - "))
count_0 = 0
count_1 = 0
for i in range(n):
    x = int(input("Введите 0 или 1 - "))
    if x == 0:
        count_0 += 1
    else:
        count_1 += 1
if count_1 > count_0:
    print(count_0)
else:
    print(count_1)
