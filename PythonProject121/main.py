text_1 = input(f"Enter text: ")
text_2 = input(f"Enter text again to find ({text_1}) in: ")
if text_1 in text_2:
    print(f"Yes")
else:
    print(f"No")
