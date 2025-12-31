numbers = list(map(int, input("Enter numbers to swap biggest and lowest number: ").split()))
biggest_num = max(numbers)
smallest_num = min(numbers)
index_biggest = numbers.index(biggest_num)
index_smallest = numbers.index(smallest_num)
numbers[index_smallest], numbers[index_biggest] = numbers[index_biggest], numbers[index_smallest]
for num in numbers:
    print(num, end=" ")