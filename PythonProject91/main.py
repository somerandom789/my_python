previous_number = -1
min_count = 999999
current_count = 0
while True:
    number = int(input(f"Enter number: "))
    if number == 0:
        break
    if number == previous_number:
        current_count += 1
    else:
        current_count = 1
        previous_number = number
    if current_count > 1 and current_count < min_count:
        min_count = current_count

print(min_count)
