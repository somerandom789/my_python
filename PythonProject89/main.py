max_number = 0
counter = 0
while True:
    number = int(input(f"Enter number: "))
    if number == 0:
        break
    if number > max_number:
        max_number = number
        counter = 1
    elif number == max_number:
        counter = counter + 1
print(counter)