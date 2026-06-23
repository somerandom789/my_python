# задача 464
# На вхід програми подається деякий текст в одному рядку з пропусками.
# Необхідно знайти у тексті слово під певним номером (наприклад, п’яте слово за рахунком)
# і вивести на екран його першу букву.
#
# Вхідні дані:
#
# Now is better than never
# 3
#
# Вихідні дані:
#
# b

text = input("Enter words: ")
number = int(input("Enter index: ")) - 1
words = text.split()
target_word = words[number]
first_letter = target_word[0]
print(first_letter)