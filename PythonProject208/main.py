# задача 448
# Для введеної послідовності цілих чисел обміняйте сусідні елементи
# у парах (A[0] з A[1], A[2] з A[3] і т. д.). Надрукуйте отриманий список.
# Якщо в списку є непарне число елементів, залиште останній елемент на місці.
#
# Вхідні дані:
#
# 1 4 5 3 7
# 4 2 10 5
# 2
#
# Вихідні дані:
#
# 4 1 3 5 7
# 2 4 5 10
# 2

for repeat in range(3):
    numbers = list(map(int, input("Enter numbers: ").split()))
    for it in range(0, len(numbers) - 1, 2):
        numbers[it], numbers[it + 1] = numbers[it + 1], numbers[it]
    for unpack in numbers:
        print(unpack, end=" ")
    print()




