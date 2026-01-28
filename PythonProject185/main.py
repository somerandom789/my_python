# задача 472
#
# Дано список слів. Напишіть програму, яка виконає заміну останніх трьох символів слів,
# що мають певну довжину, на певний символ. Користувач відповідно вводить наступні дані:
# кількість слів у списку, довжину слів, які будуть редагуватися, символ заміни останніх тьох символів
# і сам список слів (кожне слово в окремому рядку). Гарантовано, що довжина слів у списку щонайменше 3 символи.
#
# Вхідні дані:
#
# 4
# 5
# %
# writer
# painter
# programmer
# scientist
#
# Вихідні дані:
#
# ['wri%', 'pain%', 'program%', 'scient%']

number_of_words = int(input(f"Enter number of words: "))
length_of_words = int(input(f"Enter length of words: "))
symbol = input(f"Enter symbol to replace words with: ")
all_words = []
for words in range(number_of_words):
    words_typed = input(f"Enter words: ")
    if len(words_typed) >= length_of_words:
        words_typed = words_typed[:-3] + symbol
        all_words.append(words_typed)
print(all_words)
