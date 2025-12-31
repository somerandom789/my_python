for Sviat in range(3):
    number = int(input(f"Enter number: "))
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number = number // 10
    print(result)

