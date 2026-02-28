# задача 477
#
# Для введеної послідовності цілих чисел, вивести їх у списку так,
# щоб парні елементи розташовувалися на початку списку, а непарні - в кінці.
#
# Вхідні дані:
#
# 2 5 7 8 9 10 12 32 5
#
# Вихідні дані:
#
# 32 12 10 8 2 5 7 9 5
#
numbers = list(map(int, input("Enter numbers: ").split()))
sorted_num = sorted(numbers)
for it in reversed(sorted_num):
    if it % 2 == 0:
        print(it, end=" ")
for it in numbers:
    if it % 2 == 1:
        print(it, end=" ")
