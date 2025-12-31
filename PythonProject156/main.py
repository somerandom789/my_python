numbers = list(map(int, input(f"Enter numbers: ").split()))
result = sum(numbers) / len(numbers)
print(f"{int(result)}.{int(result%1 * 100):02}")








