previous = None
count = 0
while True:
    current = int(input(f"Enter number: "))
    if current == 0:
        break
    if previous is not None and ((previous > 0 and current < 0) or (previous < 0 and current > 0)):
        count = count + 1
    previous = current
print(count)




