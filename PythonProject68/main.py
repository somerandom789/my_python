days = int(input(f"Enter number of days: "))
temperature_lowest = 0
temperature_question = False
if 1 <= days <= 31:
    for a in range(days):
        temp = int(input(f"Enter the temperature: "))
        if temp < temperature_lowest:
            temperature_lowest = temp
        if temp < -15:
            temperature_question = True
    print(f"The lowest temperature was: {temperature_lowest}")
    if temperature_question is True:
        print(f"Yes")
    else:
        print(f"No")
else:
    print(f"Wrong number of days.")