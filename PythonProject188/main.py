# задача 476
#
# Напишіть програму, яка приймає 2 цілих числа, a і b і генерує двовимірний масив.
# Значення елемента в i-му рядку і j-му стовпці масиву має бути i * j (i = 0,1...,a-1; j = 0,1..., b-1).
#
# Вхідні дані:
#
# 3 5
#
# Вихідні дані:
#
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
lists = []
for it in range(number_1):
    row = []
    for it_2 in range(number_2):
        row.append(it * it_2)
    lists.append(row)
print(lists)

