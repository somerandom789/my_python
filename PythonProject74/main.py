number = int(input(f"Please enter number: "))
for i in range(number):
    for j in range(number + 1):
        print(j - i, end="\t")
    print()

