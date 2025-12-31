for b in range(2):
    number_str = input(f"Please enter an automorphic number: ")
    number_int = int(number_str)
    stepen1 = number_int ** 2
    length = len(number_str)
    stepen2 = 10 ** length
    last_digits = stepen1 % stepen2

    if last_digits == number_int:
        print(f"True")
    else:
        print(f"False")



