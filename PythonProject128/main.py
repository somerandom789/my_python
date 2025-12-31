for a in range(2):
    text = input("Enter anything to delete numbers from it: ")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for final in numbers:
        text = text.replace(str(final), "")

    print(text)



