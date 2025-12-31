smaller = int(input(f"Enter smaller number: "))
bigger = int(input(f"Enter bigger number: "))
result = []
for a in range(smaller + (bigger % 2 == 0), bigger + 1, 2):
    result.append(a)
for nice_looking in result:
    print(nice_looking, end=" ")