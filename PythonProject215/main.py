# задача 467
# Напишіть програму для перетворення двійкового числа в десяткове число.
#
# Вхідні дані:
#
# 1001
# 101010111
# 10000
#
# Вихідні дані:
#
# 9
# 343
# 16

for repeat in range(3):
    input_numbers = input("Enter 2 digit numbers: ")
    decimal_number = int(input_numbers, 2)
    print(decimal_number)


