for n in range(3):
    number = list(map(int, input(f"Enter numbers: ").split()))
    result = 0
    for a in range(1, len(number) - 1):
        if number[a] > number[a - 1] and number[a] > number[a + 1]:
            result = result + 1
    print(result)
    
