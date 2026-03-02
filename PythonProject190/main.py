# задача 480
#
# Дано список назв міст світу, перерахованих в рядку через кому.
# Сформуйте з елементів списку повідомлення, у якому перед останнім елементом буде вставлено слово and так,
# як у вихідних даних. Програма має працювати з будь-якими списками, які мають довільну довжину, відмінну від нуля.
#
# Вхідні дані:
#
# Budapest, Rome, Istanbul, Sydney, Kyiv, Hong Kong
# Kyiv, Hong Kong
# Budapest
#
# Вихідні дані:
#
# Budapest, Rome, Istanbul, Sydney, Kyiv and Hong Kong
# Kyiv and Hong Kong
# Budapest
for repeat in range(3):
    cities = input("Enter cities: ").split(', ')
    result = 0
    if len(cities) == 1:
        result = cities[0]
    else:
        first_part = ", ".join(cities[:-1])
        result = " and ".join([first_part, cities[-1]])
    print(f"Cities are: {result}.")












