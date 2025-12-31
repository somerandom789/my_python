number = int(input(f"Enter number from 0 to: "))
for z in range(1, number + 1):
    for a in range(z, number + 1):
        print(a, end="   ")
    print()
