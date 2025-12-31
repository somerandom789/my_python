last_number = 0
counter = 0
while True:
    number = int(input(f"Enter number: "))
    if number == 0:
        break
    if last_number > 0 and last_number > number:
        counter = counter + 1
    last_number = number
print(counter)

