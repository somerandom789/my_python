for a in range(3):
    number = int(input(f"Enter number: "))
    result_1 = 0
    result_2 = 0
    midresult_1 = 0
    midresult_2 = 0
    if number != 0:
        for b in range(10, number) :
            midresult_1 = b // 10
            midresult_2 = b % 10
            if midresult_1 != 0 and midresult_2 != 0:
                result_1 = b % midresult_1
                result_2 = b % midresult_2
                if b % midresult_1 == 0 and b % midresult_2 == 0:
                    print(b, end=" ")
            else:
                continue
        print()


    else:
        print(f"The number is 0.")



