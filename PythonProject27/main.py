n = int(input(f" Enter number from 1 to 1000: "))
if 0 < n < 1000:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("*35*")
        elif i % 3 == 0:
            print("*3*")
        elif i % 5 == 0:
            print("*5*")
        else:
            print(i)
else:
    print(f" Sorry number {n} is not from 1 to 1000: ")