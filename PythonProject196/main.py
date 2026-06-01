# задача 452
# Напишіть програму для обчислення добутку цілих чисел (без використання циклу for),
# які вводяться через пропуск користувачем в одному рядку.
# Вхідні дані:
# 2 5 3
# Вихідні дані:
# 30

numbers = list(map(int, input("Enter numbers: ").split()))
num = 1
index = 0
while index < len(numbers):
    num = num * numbers[index]
    index = index + 1
print(num)