n = int(input(f"Enter any number: "))
for i in range(1, n + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")

