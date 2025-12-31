number = int(input(f"Enter number: "))
count = 0
current_num = 0
while count < number:
    for sviat in range(current_num):
        if count == number:
            break
        print(current_num, end=" ")
        count = count + 1
    current_num = current_num + 1
