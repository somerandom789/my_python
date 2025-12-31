text = input(f"Enter word: ")
letter = input(f"Enter letter to find in {text}: ")
position = text.find(letter)
if position == -1:
    print(0)
else:
    print(position + 1)



