num_sum = 0
squered_sum = 0
while True:
    number = int(input(f"Enter number: "))
    num_sum = num_sum + number
    squered_sum = squered_sum + number ** 2
    if num_sum == 0:
        break
print(squered_sum)

