password = 12345
while True:
    password_type = int(input(f"Please enter the password: "))
    if password_type == password:
        print(f"Done")
        break
    else:
        print(f"Error")


