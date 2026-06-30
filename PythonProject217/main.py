# задча 450
# У введеному списку цілих чисел, знайдіть і надрукуйте сусідні елементи,
# які мають однаковий знак. Якщо такої пари немає, не повинно нічого виводитися.
#
# Вхідні дані:
#
# 1 -2 -3 5 6 -3 7 8
#
# Вихідні дані:
#
# -2 -3
# 5 6
# 7 8

input_numbers = list(map(int, input("Enter numbers: ").split()))
for it in range(len(input_numbers) - 1):
    current_num = input_numbers[it]
    next_num = input_numbers[it + 1]
    if current_num * next_num > 0:
        print(current_num, next_num)
