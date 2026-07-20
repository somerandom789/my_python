# задача 425
# Напишіть програму, яка отримує два цілих числа в одному рядку
# через пропуск і виводить ці числа аналогічним чином, помінявши їх місцями.
#
# Вхідні дані:
#
# 101 56
#
# Вихідні дані:
#
# 56 101

first_num, second_num = map(int, input("Enter numbers: ").split())
first_num, second_num = second_num, first_num
print(first_num, second_num)








