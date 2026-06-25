# задача 460
# Вводиться список цілих чисел. Всі числа списку знаходяться на одному рядку.
# У списку всі елементи різні. Поміняйте місцями мінімальний і максимальний елементи цього списку.
#
# Вхідні дані:
#
# 5 6 8 1 4 9 12
#
# Вихідні дані:
#
# 5 6 8 12 4 9 1

all_num = list(map(int, input("Enter numbers: ").split()))
min_idx = all_num.index(min(all_num))
max_idx = all_num.index(max(all_num))
all_num[min_idx], all_num[max_idx] = all_num[max_idx], all_num[min_idx]
for it in all_num:
    print(it, end=" ")