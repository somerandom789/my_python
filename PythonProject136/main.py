first_number = int(input(f"Enter number bigger than 32: "))
second_number = int(input(f"Enter number bigger than 32 and smaller than 127: "))
if (first_number > 32) and (first_number <= second_number < 127):
    for a in range(first_number, second_number + 1):
        print(chr(a), a)
else:
    print(f"Error. Please try again.")




