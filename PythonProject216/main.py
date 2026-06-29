# задача 427
# Створіть програму, яка отримує на вхід послідовність цілих чисел,
# і друкує на екрані: найменше число у списку, найбільше число у списку,
# кількість чисел у списку, середнє значення елементів у списку.
#
# Вхідні дані:
#
# 1 3 7 5
#
# Вихідні дані:
#
# 1
# 7
# 4
# 4.0

numbers = list(map(int, input("Enter numbers: : ").split()))
smallest = min(numbers)
largest = max(numbers)
count = len(numbers)
average = sum(numbers) / count
print(smallest)
print(largest)
print(count)
print(average)