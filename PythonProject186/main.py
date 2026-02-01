# задача 473
# Користувач вводить два цілих додатних числа n і m.
# Напишіть програму, яка створює двовимірний масив розміром n x m і заповнює його символами .
# і * у шаховому порядку (як у вихідних даних). Лівий верхній кут повинен мати символ ..
#
# Вхідні дані:
#
# 6 8
#
# Вихідні дані:
#
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .

line = int(input("Enter number of lines: "))
column = int(input("Enter number of columns: "))
for lines in range(line):
    for columns in range(column):
        if (lines + columns) % 2 == 0:
            print(".", end=" ")
        else:
            print("*", end=" ")
    print()