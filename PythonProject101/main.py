bigger = int(input(f"Enter bigger number: "))
smaller = int(input(f"Enter smaller number: "))
result = []
for a in reversed(range(smaller + (smaller % 2 == 0), bigger + 1, 2)):
    result.append(a)
for nice_looking in result:
    print(nice_looking, end=" ")





