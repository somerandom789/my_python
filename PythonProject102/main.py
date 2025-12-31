number = int(input(f"Enter number: "))

for dilene in range(1, number + 1):
    count = 0
    for dilnyk in range(1, dilene + 1):
        if dilene % dilnyk == 0:
            count = count + 1
    print(f"{dilene}{'+' * count}")



