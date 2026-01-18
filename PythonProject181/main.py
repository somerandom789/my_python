numbers = list(map(int, input(f"Enter numbers: ").split()))
while numbers:
    if len(numbers) >= 3:
        numbers.pop(2)
    else:
        numbers.pop(0)
    print(numbers)



