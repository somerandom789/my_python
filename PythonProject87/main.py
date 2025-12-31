last_number = None
counter = 0
counter_2 = 0
while True:
    number = int(input(f"Enter number: "))
    if number == 0:
        break
    if last_number is not None and number > last_number:
        counter = counter + 1
    last_number = number
    counter_2 = counter_2 + 1
    print(counter_2)
print(counter)

