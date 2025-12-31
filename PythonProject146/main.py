numbers = list(map(int, input(f"Enter numbers: ").split()))
min_num = min(numbers)
max_min = max(numbers)
count = len(numbers)
avarage = sum(numbers) / count
print(f"Smallest number:{min_num}")
print(f"Biggest number:{max_min}")
print(f"Count: {count}")
print(f"Avarage number is:{avarage}")




