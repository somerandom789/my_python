n = int(input(f"Enter number: "))
if n > 0:
    a = 0
    for z in range(1, n + 1):
        a = a + z / (z + 1)
    print(round(a, 2))
else:
    print(f"Number {n} is equal or lower 0. ")