for a in range(3):
    number = abs(int(input(f"Enter number: ")))
    result_1 = 0
    result_2 = 1
    counter = 0
    while True:
        sum_num = result_1 + result_2
        counter = counter + 1
        if counter == number:
            print(sum_num)
            break
        result_2 = result_1
        result_1 = sum_num


