# задача 439 я її раніше пропустив
# Напишіть простий інтерпретатор математичного виразу.
# На вхід подається рядок з виразом, що складається з двох чисел (0 ≤ a, b ≤ 1000)
# об’єднаних бінарним оператором: a operator b, де замість operator можуть використовуватися такі слова:
# plus, minus, multiply, divide для, відповідно, додавання, віднімання, множення і цілочисельного ділення.
# Результат обчислення - рядок, що містить ціле число.
#
# Вхідні дані:
#
# 20 plus 7
# 15 minus 9
# 144 multiply 2
# 49 divide 7
#
# Вихідні дані:
#
# 27
# 6
# 288
# 7

expression = input("Enter math expression: ")
parts = expression.split()
first_part = int(parts[0])
second_part = parts[1]
last_part = int(parts[2])
result = 0
if second_part == "plus":
    result = first_part + last_part
elif second_part == "minus":
    result = first_part - last_part
elif second_part == "multiply":
    result = first_part * last_part
elif second_part == "divide":
    result = first_part // last_part
print(f"Answer is: {result}")