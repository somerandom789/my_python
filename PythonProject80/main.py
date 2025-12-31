for Sviat_BEST in range(2):
    number = input(f"Enter number: ")
    try:
        max_num = int(max(number))
        min_num = int(min(number))
        result = max_num - min_num
        print(max_num, min_num, result)
        if result % 2 == 0:
            print(f"True")
        else:
            print(f"False")
    except Exception as ValueError:
        print(f"This is not a number")


