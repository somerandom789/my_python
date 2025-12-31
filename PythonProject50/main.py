for i in range(2):
    number = int(input(f"Enter number from 1 to: "))
    for a in range(1, number + 1):
        if a % 2 != 0:
            print(a, end=" ")
    print()


