# задача 429
# Напишіть програму для підрахунку кількості днів, в яких температура
# була не нижче, ніж середня температура за весь період. У першому рядку
# вводиться список показників температури на кожен день. У рядку виведення
# одне число - кількість днів, які відповідають умові.
#
# Вхідні дані:
#
# -3 -1 0 2 6 8 12 15
#
# Вихідні дані:
#
# 4

numbers = list(map(int, input("Enter numbers: ").split()))
average_temp = sum(numbers) / len(numbers)
higher_temp = 0
for temp in numbers:
    if temp >= average_temp:
        higher_temp = higher_temp + 1
print(higher_temp)