# задачв 432
# Напишіть програму, щоб перевірити, чи певне ціле число n перевищує всі
# елементи цілочисельного списку. Значення списку вводяться через пропуск
# в одному рядку, число n вводиться у новому рядку.
#
# Вхідні дані:
#
# 4 67 109 25 44 12
# 99
#
# Вихідні дані:
#
# False

numbers = list(map(int, input("Enter numbers: ").split()))
num = int(input("Enter number: "))
is_greater = True
for it in numbers:
    if it >= num:
        is_greater = False
print(is_greater)