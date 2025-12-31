password = int(input(f"Enter your password please: "))
password_input = int(input(f"Enter password: "))
while password_input != password:
    print(f"Error. Try again.")
    password_input = int(input(f"Enter password: "))
    if password_input == password:
        print(f"Done.")
        break

