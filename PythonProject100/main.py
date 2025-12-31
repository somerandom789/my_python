number = int(input(f"Enter number: "))
money = [64, 32, 16, 8, 4, 2, 1]
result = []

for nominal in money:
    a = number // nominal
    if a != 0:
        print(f"{a} ({nominal})")
    number = number - a * nominal

