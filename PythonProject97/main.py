number = int(input("Enter number: "))
list = []
number_2 = 0
for a in range(number - 1):
    number_2 = int(input("Enter number: "))
    list.append(number_2)
for i in range(1, number + 1):
    if i not in list:
        print(i)
        break
    else:
        continue
