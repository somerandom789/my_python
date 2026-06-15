# задача 430
# Напишіть програму для підрахунку кількості цілих чисел n, які
# вводяться користувачем (значення вводяться через пропуск в одному рядку, число n вводиться у новому рядку).
#
# Вхідні дані:
#
# 2 5 8 19 7
# 5
# 2 6 7 8 9 9 2 3
# 9
#
# Вихідні дані:
#
# 1
# 2
for repeat in range(2):
    all_num = input("Enter all numbers: ").split()
    counting_num = input("Enter number that will be counted: ")
    counted_num = all_num.count(counting_num)
    print(counted_num)
