numbers = list(map(int, input(f"Enter numbers: ").split()))
smallest_num = numbers[0]
for it in numbers:
    if it < smallest_num:
        smallest_num = it
print(smallest_num)



