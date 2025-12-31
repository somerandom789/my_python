number = int(input(f"Enter number: "))
result = number
result_2 = number ** 2
while result != 0:
    number = int(input(f"Enter number: "))
    result = result + number
    result_2 = result_2 + number ** 2
print(result_2)
