# задача 437
# Напишіть програму для перетворення списку декількох цілих чисел у єдине ціле число.
# Значення списку вводяться через пропуск в одному рядку.
#
# Вхідні дані:
#
# 1 7 9 4
#
# Вихідні дані:
#
# 1794

input_list = input("Enter numbers: ").split()
joined_num = "".join(input_list)
result_num = int(joined_num)
print(f"Your number is: {result_num}")
