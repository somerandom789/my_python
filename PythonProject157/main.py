for sviat in range(4):
    numbers = input(f"Enter expression: ").split()
    result = 0
    int_num_1 = int(numbers[0])
    action = numbers[1]
    int_num_2 = int(numbers[-1])
    if action == "plus":
        result = int_num_1 + int_num_2
    if action == "minus":
        result = int_num_1 - int_num_2
    if action == "multiply":
        result = int_num_1 * int_num_2
    if action == "divide":
        result = int_num_1 // int_num_2
    print(result)



