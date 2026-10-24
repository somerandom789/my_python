# задача 428
# Напишіть програму, яка приймає послідовність чисел, розділених
# комами, від користувача і створює список і кортеж з цими числами.
#
# Вхідні дані:
#
# 7, 9, 12, 4
#
# Вихідні дані:
#
# [7, 9, 12, 4]
# (7, 9, 12, 4)

numbers = list(map(int,input("Enter numbers: ").split(", ")))
numbers_tuple = tuple(numbers)
print(numbers)
print(numbers_tuple)