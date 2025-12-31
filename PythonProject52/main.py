for Sviatoslav in range(3):
    number = int(input(f"Enter number: "))
    a = 0
    for z in range(1 , number + 1):
        x = 1
        for h in range(1, z + 1):
            x = x * h
        a = a + x
    print(a)

