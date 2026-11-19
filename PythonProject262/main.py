# задача 431
# Напишіть програму для друкування всіх парних чисел із введеного списку чисел у
# тому ж порядку і припиніть друк, якщо у списку буде число n або нуль. Значення
# списку вводяться через пропуск в одному рядку, число n вводиться у новому рядку.
#
# Вхідні дані:
#
# 1 8 9 0 4 2 5 6
# 2
#
# Вихідні дані:
#
# 8

numbers = list(map(int, input("Enter numbers: ").split()))
second_num = int(input("Enter number: "))
even_numbers = []
for it in numbers:
    if it == second_num or it == 0:
        break
    if it % 2 == 0:
        even_numbers.append(it)
print(*even_numbers)
