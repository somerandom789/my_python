number_of_days = int(input(f"Please enter the number of days: "))
bugs = 0
for i in range(number_of_days):
    number_of_bugs = int(input(f"Please enter the number of bugs: "))
    bugs = bugs + number_of_bugs
print(f"The sum of all bugs is: {bugs}")


