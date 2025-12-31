for Sviat in range(2):
    number = input(f"Enter anything: ")
    lenth = len(number)
    result = 0
    if lenth >= 2:
        result = number[-2:]
        result = result * 5
    print(result)