for repeat in range(3):
    numbers = list(map(int, input(f"Enter numbers: ").split()))
    result = numbers[-1:] + numbers[:-1]
    for it in result:
        print(it, end=" ")
    print()
