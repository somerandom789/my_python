a = 0
while True:
    number = int(input(f"Please enter the number: "))
    if number == 0:
        break
    if number > a:
        a = number
print(f"The biggest number is: {a}")
