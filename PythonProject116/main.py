for Sviat in range(4):
    number = int(input(f"Enter any number: "))
    number_len = len(str(number))
    if number < 10:
        print(number)
    else:
        last_digit = number % 10
        first_number_place = 10 ** (number_len - 1)
        first_digit = number // first_number_place
        middle_part = (number % first_number_place) // 10
        middle_part = middle_part * 10
        new_number = last_digit * first_number_place + middle_part + first_digit
        print(new_number)


