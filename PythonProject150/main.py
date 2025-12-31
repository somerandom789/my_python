numbers = list(map(int, input(f"Enter numbers: ").split()))
second_num = int(input(f"Enter second number: "))
for it in numbers:
    if it > second_num:
        print(f"{second_num} is not bigger than {it}.")
        break
else:
    print(f"{second_num} is bigger than {numbers}.")


