number = int(input("Enter number: "))
number_2 = int(input("Enter number: "))
number_length = len(str(number))
number_length_2 = len(str(number_2))
if number_length == 4 and number_length_2 == 4:
    for a in range(number, number_2 + 1):
        temporary_number = a
        result = 0
        while temporary_number > 0:
            result = result * 10 + temporary_number % 10
            temporary_number = temporary_number // 10
        if a == result:
            print(a)
else:
    print(f"One of number length isn't 4-digit.")
