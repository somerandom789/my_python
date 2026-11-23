# задача 419
# Вводиться список чисел. Всі числа списку знаходяться в одному рядку.
# Не змінюючи його і не використовуючи додаткові списки, визначте, яке число
# в цьому списку зустрічається найчастіше. Якщо таких чисел декілька, виведіть будь-яке з них.
#
# Вхідні дані:
#
# 1 0 0 1 0 0 1 1 0
# 2 4 6 9 9 2 3 2 4
#
# Вихідні дані:
#
# 0
# 2

numbers = list(map(int, input("Enter numbers: ").split()))
best_num = numbers[0]
max_count = 0
for it in numbers:
    current_count = numbers.count(it)
    if current_count > max_count:
        max_count = current_count
        best_num = it
print(best_num)