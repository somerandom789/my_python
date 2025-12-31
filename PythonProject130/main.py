number = input(f"Enter 3 digit number: ")
if len(number) == 3:
    summ = int(number[0]) + int(number[1]) + int(number[2])
    print(summ)
else:
    print(f"{number} is {len(number)} digit number not 3 digit.")


