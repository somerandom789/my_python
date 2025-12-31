for a in range(3):
    number_or_text = input(f"Enter number: ")
    try:
        number_or_text = int(number_or_text)
        print(f"Yes")
    except ValueError:
        print(f"No")



