for i in range(3):
    number = int(input(f"Enter any number: "))
    last_digit = 0
    result = 0
    while number > 0:
        if number > 0:
            last_digit = number % 10
            number = number // 10
            result = result * 10 + last_digit

    print(result)



