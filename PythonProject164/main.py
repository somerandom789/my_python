for repeat in range(3):
    numbers = list(map(int, input(f"Enter numbers: ").split()))
    for find_index in range(0, len(numbers)-1, 2):
        numbers[find_index], numbers[find_index + 1] = numbers[find_index + 1], numbers[find_index]
    for it in numbers:
        print(it, end=" ")
    print()




