# задача 454
# Напишіть програму для друку елементів певного цілочисельного списку
# після видалення з нього парних чисел. Значення списку вводяться через пропуск в одному рядку.
#
# Вхідні дані:
#
# 3 44 6 8 9 12 7
#
# Вихідні дані:
#
# [3, 9, 7]

input_numbers = list(map(int, input("Enter numbers: ").split()))
odd_numbers = []
for it in input_numbers:
    if it % 2 != 0:
        odd_numbers.append(it)
print(odd_numbers)