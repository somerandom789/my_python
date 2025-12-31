number = int(input(f"Enter first number: "))
number_2 = int(input(f"Enter second number: "))
result = 0
while number_2 > 0:
    result = result + number
    number_2 = number_2 - 1
print(result)
