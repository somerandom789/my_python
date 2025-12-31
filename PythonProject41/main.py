number_of_dollars = int(input(f"Enter number of dollars: "))
dollar_in_hryvnias = float(input(f"Enter how much hryvnias is 1 dollar: "))
for z in range(1, number_of_dollars + 1):
    print(z, round(z * dollar_in_hryvnias, 2))
