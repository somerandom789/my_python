for a in range(3):
    number = int(input(f"Enter number of hours: "))
    result = 1
    for i in range(1, number + 1):
        if i % 3 == 0:
            result = result * 2
    print(result)
