numbers = list(map(int, input(f"Enter numbers: ").split()))
second_num = int(input(f"Enter second number: "))
for num in numbers:
    if num == second_num or num == 0:
        break
    if num % 2 == 0:
        print(num)







