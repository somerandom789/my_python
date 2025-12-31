first_number = int(input(f"Enter first number: "))
second_number = int(input(f"Enter second number: "))
print(f"{first_number} {'<' if first_number < second_number else'' '>' if first_number > second_number else''  '='if first_number == second_number else ''} {second_number} ")

