days = int(input(f"Enter number of days: "))
a = 0
for z in range(days):
    errors = int(input(f"Enter number of errors: "))
    a = a + errors
print(a)