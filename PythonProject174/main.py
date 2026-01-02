numbers = list(map(int, input(f"Enter numbers: ").split()))
min_num = min(numbers)
max_num = max(numbers)
min_index = numbers.index(min_num)
max_index = numbers.index(max_num)
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
for it in numbers:
    print(it, end=" ")


