number1 = int(input(f"Введіть ділене: "))
number2 = int(input(f"Введіть дільник: "))
division = number1
result = 0
if number1 > number2:
    while division > number2:
        division = division - number2
        result= result + 1
    print(f"Результат: {result}, залишок: {division}.")
else:
    print(f"Число {number1} менше за число {number2}.")


