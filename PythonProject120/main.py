for a in range(4):
    something = input(f"Enter palindrome: ")
    something = something.replace(" ", "")
    something = something.lower()
    if something == something[::-1]:
        print(f"True")
    else:
        print(f"False")




