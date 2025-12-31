number = int(input("Enter number: "))
a = number
while number != 0:
    number = int(input("Enter number: "))
    if number == 0:
        break
    a = a + number
print(f"The sum of all numbers is: {a}")
