# задача 436
# Напишіть програму для знаходження другого найменшого елемента у цілочисельного списку.
# Значення списку вводяться через пропуск в одному рядку.
#
# Вхідні дані:
#
# 20 56 14 9 1 15
#
# Вихідні дані:
#
# 9

numbers = list(map(int, input("Enter numbers: ").split()))
numbers.remove(min(numbers))
second_smallest_num = min(numbers)
print(f"Second smallest number is: {second_smallest_num}")
