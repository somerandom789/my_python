a = 0
while True:
    number = int(input(f"Enter number: "))
    if number == 0:
        break
    if number % 2 == 0:
        a = a + 1
print(a)
