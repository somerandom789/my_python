text_first = input(f"Enter any text: ")
text_second = input(f"Enter any text: ")
len_first = len(text_first)
len_second = len(text_second)
if len_first > len_second:
    print(f"{text_first} is bigger than {text_second}")
elif len_first == len_second:
    print(f"equally")
else:
    print(f"{text_second} is bigger than {text_first}")

