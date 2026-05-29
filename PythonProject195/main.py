# задача 454
# Напишіть програму для друку елементів певного цілочисельного списку після видалення з нього парних чисел.
# Значення списку вводяться через пропуск в одному рядку.
#
# Вхідні дані:
#
# 3 44 6 8 9 12 7
#
# Вихідні дані:
#
# [3, 9, 7]

input_num = input("Enter numbers: ")
list_str = input_num.split()
list_num = []
for element in list_str:
    num = int(element)
    if num % 2 != 0:
        list_num.append(num)
print(list_num)