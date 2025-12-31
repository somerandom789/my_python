a = int(input(f" Enter first number: "))
b = int(input(f" Enter second number: "))
c = int(input(f" Write the divisor: "))
for x in range(a, b+1):
    if x % c == 0:
        print(x, end=" ")


