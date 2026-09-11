# задача 424
# Визначте, скільки різних слів у введеному рядку.
#
# Вхідні дані:
#
# New Delhi New York Paris Prague Reykjavik
# Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend
#
# Вихідні дані:
#
# 6
# 19

words = input("Enter numbers: ").split()
unique_words = set(words)
print(len(unique_words))