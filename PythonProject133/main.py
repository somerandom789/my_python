for a in range(2):
    text = input(f"Enter anything to take numbers from it: ")
    result = ""
    for final in text:
        if final.isdigit():
            result = result + final
    print(result)



