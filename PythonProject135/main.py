number_of_penguins = int(input("Enter number of penguins: "))
line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
line_5 = ""

for i in range(1, number_of_penguins + 1):
    line_1 = line_1 + "   _~_   " + " "
    line_2 = line_2 + "  (o o)  " + " "
    line_3 = line_3 + " /  V  \ " + " "
    line_4 = line_4 + f"/(  {i}  )\ "
    line_5 = line_5 + "  ^^ ^^  " + " "
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)



