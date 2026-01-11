numbers = list(map(int, input(f"Enter numbers: ").split()))
index = int(input(f"Enter index: "))
for it in numbers:
    if it != numbers[index]:
        print(it, end=" ")

