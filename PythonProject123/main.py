for Sviat in range(3):
    text = input(f"Enter anything: ")
    if text.isdigit():
        print(f"Your message includes numbers only.")
    elif text.isalpha():
        print(f"Your message includes letters only.")
    else:
        print(f"Your message includes numbers and letters.")
