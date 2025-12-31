number = int(input(f"Enter number: "))
column = int(input(f"Enter number of columns: "))
for a in range(0, number + 1):
    for b in range(column):
        print(a, end="\t")
    print()



