number = int(input(f"Enter number: "))
for a in range(10, 99 + 1):
    b = a // 10
    c = a % 10
    if b ** 2 + c ** 2 >= 100:
        print(a, end=" ")





