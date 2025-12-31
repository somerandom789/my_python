number = int(input(F"Enter number: "))
remove = int(input(F"Enter number to remove from {number}: "))
result = 0
while number > 0:
    digit = number % 10
    if digit != remove:
        result = result * 10 + digit
    number = number // 10
final = 0
while result > 0:
    digit_2 = result % 10
    final = final * 10 + digit_2
    result = result // 10
print(final)


