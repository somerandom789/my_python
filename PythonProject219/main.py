# задача 452
# Напишіть програму для обчислення добутку цілих чисел (без використання циклу for),
# які вводяться через пропуск користувачем в одному рядку.
#
# Вхідні дані:
#
# 2 5 3
#
# Вихідні дані:
#
# 30

import math
numbers = list(map(int, input("Enter numbers: ").split()))
result = math.prod(numbers)
print(result)