# задача 480
# Дано список назв міст світу, перерахованих в рядку через кому. Сформуйте
# з елементів списку повідомлення, у якому перед останнім елементом буде
# вставлено слово and так, як у вихідних даних. Програма має працювати з
# будь-якими списками, які мають довільну довжину, відмінну від нуля.
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
    cities = input("Enter cities: ").split(", ")
    if len(cities) == 1:
        print(cities[0])
    elif len(cities) == 2:
        print(cities[0] + " and " + cities[1])
    else:
        main_part = ", ".join(cities[:-1])
        print(main_part + " and " + cities[-1])