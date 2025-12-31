number = int(input(f"Enter number of #: "))
for a in range(1, number + 1):
    s = "#"
    print(f"{a *s:>{number}}", sep="\n")


