for again in range(2):
    numbers = list(map(int, input(f"Enter numbers: ").split()))
    result = 0
    second_number = int(input(f"Enter number to find in {numbers}: "))
    for it in numbers:
        if it == second_number:
            result = result + 1
    print(result)
















