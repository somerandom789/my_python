number = int(input(f"Enter number: "))
a = number
b = 1
avg = 0
while number != 0:
    number = int(input("Enter number: "))
    if number == 0:
        break
    b = b + 1
    a = a + number
    avg = a / b
print(f"THe average number is: {avg}")
