num_max = 0
index_max = 0
index_now = 0
while True:
    num = int(input(f"Enter number: "))
    if num == 0:
        break
    if num > num_max:
        num_max = num
        index_max = index_now
    index_now = index_now + 1
print(index_max)
