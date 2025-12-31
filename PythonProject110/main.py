for i in range(3):
    number = int(input(f"Enter any number: "))
    number_in_number = len(str(number))
    number_of_zeros = 10 ** number_in_number
    number = number / number_of_zeros + 2
    number = number * number_of_zeros
    number = number * 10 + 2
    print(int(round(number, 0)))


