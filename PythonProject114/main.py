surname = input(f"Enter your surname: ")
name = input(f"Enter your name: ")
patronymic = input(f"Enter your patronymic name: ")
first_letter_name = name.upper()[0]
first_letter_patronymic = patronymic.upper()[0]
print(f"{first_letter_name}.{first_letter_patronymic}.{surname}")


