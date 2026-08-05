# задача 475
# Напишіть програму, яка приймає на вхід список чисел в одному рядку і виводить
# на екран в один рядок значення, які повторюються в ньому більш ніж один раз.
# Виведені числа не повинні повторюватися, порядок їх виведення маж бути за зростанням.
#
# Вхідні дані:
#
# 5 8 1 3 5 2 1 3 0
# 2 2 4 4 4 1
#
# Вихідні дані:
#
# 1 3 5
# 2 4

for repeat in range(2):
    numbers = list(map(int, input("Enter numbers: ").split()))
    duplicates = []
    for it in numbers:
        if numbers.count(it) > 1 and it not in duplicates:
            duplicates.append(it)
    duplicates.sort()
    print(*duplicates)