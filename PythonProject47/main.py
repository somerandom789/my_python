number = int(input(f"Enter first number: "))
number_2 = int(input(f"Enter second number: "))
if number > number_2:
    for a in reversed(range(number_2, number + 1)):
        print(a, end=" ")




