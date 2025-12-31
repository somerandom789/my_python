n = int(input(f"Enter number: "))
if n >= 2:
    a = 0
    for z in range(1, n + 1):
        a = a + (z - 1) * z
    print(a)
else:
    print(f"Number {n} in lower then 2. ")