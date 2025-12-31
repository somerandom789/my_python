number = list(map(int, input(f"Enter numbers: ").split()))
for a in range(1, len(number)):
    if number[a] > number[a - 1]:
        print(number[a], end=" ")

