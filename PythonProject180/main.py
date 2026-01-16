numbers = list(map(int, input(f"Enter numbers: ").split()))
index_and_num = list(map(int, input(f"Enter index and number: ").split()))
numbers.insert(index_and_num[0], index_and_num[1])
print(numbers)


