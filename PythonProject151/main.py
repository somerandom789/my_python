numbers = list(map(int, input(f"Enter numbers: ").split()))
result = []
for it in numbers:
    if it > 0:
        result.append(it)
print(f"Only additional numbers are:{result}")



