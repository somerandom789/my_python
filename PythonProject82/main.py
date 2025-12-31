for Sviat_cool in range(3):
    number = abs(int(input(f"Enter number: ")))
    result = 0
    while number > 0:
        result = result + number % 10
        number = number // 10
    print(result)




