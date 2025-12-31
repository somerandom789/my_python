for Sviat in range(2):
    number = int(input(f"Please enter number: "))
    stepen = 10 ** number
    for a in reversed(range(0, stepen)):
        if a % 2 == 1:
            print(a, end=" ")
    print()


