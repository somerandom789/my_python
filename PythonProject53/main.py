number = int(input("Enter number: "))
while number > 0:
    number = number // 10
    if number > 0:
        print(f"{number:<{len(str(number))}}", sep="\n")
