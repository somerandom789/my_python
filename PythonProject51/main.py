for Sviat in range(3):
    number = int(input(f"Enter number: "))
    a = 1
    while number > 1:
        a *= number
        number -= 1
    print(a)
