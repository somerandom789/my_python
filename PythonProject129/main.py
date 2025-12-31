for Sviat in range(3):
    text = input(f"Enter anything: ")
    if text.islower():
        print(text.upper())
    elif text.isupper():
        print(text.lower())
    else:
        print(text)

