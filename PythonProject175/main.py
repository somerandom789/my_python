for cycle in range(2):
    text = input(f"Enter text: ").split('_')
    result = ""
    for it in text:
        result = result + it.capitalize()
    print(result)
