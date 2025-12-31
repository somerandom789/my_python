word = input(f"Enter first word: ")
word_2 = input(f"Enter second word: ")
first_letter = word.lower()[0]
last_letter = word_2.lower()[-1]
if first_letter == last_letter:
    print(f"True")
else:
    print(f"False. {first_letter} is not {last_letter}")

