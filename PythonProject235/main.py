# задача 433
# Цілі числа (додатні і від’ємні) вводяться через пропуск в одному рядку.
# Напишіть програму для друку списку лише із введених додатних чисел.
#
# Вхідні дані:
#
# 0 9 -4 6 8 -15 4
#
# Вихідні дані:
#
# [9, 6, 8, 4]

numbers = list(map(int, input("Enter numbers: ").split()))
positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
print(positive_numbers)