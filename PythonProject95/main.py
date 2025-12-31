for Sviat in range(3):
    number = int(input("Enter number: "))
    counter = 0
    if 1 <= number <= 100000:
        for a in range(1, number + 1):
            temporary_number = a
            result = 0
            while temporary_number > 0:
                result = result * 10 + temporary_number % 10
                temporary_number = temporary_number // 10
            if a == result:
                counter = counter + 1
        print(counter)
    else:
        print(f"Number isn't bigger 1 or lower 100000.")

