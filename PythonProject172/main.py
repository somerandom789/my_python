numbers = list(input("Enter numbers: ").replace(" ", "").split(','))
numbers_2 = list(input("Enter numbers: ").replace(" ", "").split(','))
result = []
for it in numbers:
    if it in numbers_2 and it not in result:
        result.append(it)
for finish in result:
    print(finish, end=" ")

