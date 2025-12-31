for repeat in range(2):
    numbers = list(map(int, input("Enter numbers: ").split()))
    for it in numbers:
        if numbers.count(it) == 1:
            print(it, end=' ')
    print()





