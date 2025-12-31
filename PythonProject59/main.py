for n in range(3):
    number = int(input(f"Enter any number: "))
    result = 0
    for z in range(100, 1000):
        helper_1 = z // 100
        helper_2 = (z // 10) % 10
        helper_3 = z % 10
        if helper_1 + helper_2 + helper_3 == number:
            result = result + 1
    print(f"The number of three-digit numbers whose sum of digits = {number} is {result}")


