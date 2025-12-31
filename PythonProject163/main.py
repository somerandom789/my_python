result = []
while True:
    words = input(f"Enter word: ")

    if words == "" or words == " ":
        break
    result.append(words)
for it in result:

    print(it.upper())



