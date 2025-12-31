number = int(input(f"Enter any number from 0 to 9: "))
helper = 0
result = 0
if 0 < number <=9:
    for a in range(1, number + 1):
        helper = a % 10
        result = result * 10 + a
        print(result)
else:
    print(f"The number isn't in between 0 and 9.")