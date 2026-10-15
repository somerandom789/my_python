# задача 439
# Напишіть простий інтерпретатор математичного виразу. На вхід подається
# рядок з виразом, що складається з двох чисел (0 ≤ a, b ≤ 1000), об’єднаних
# бінарним оператором: a operator b, де замість operator можуть використовуватися
# такі слова: plus, minus, multiply, divide для, відповідно, додавання, віднімання,
# множення і цілочисельного ділення. Результат обчислення - рядок, що містить ціле число.
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

line = input("Enter action: ").split()
first = int(line[0])
op = line[1]
second = int(line[2])
result = 0
if op == "plus":
    result = first + second
elif op == "minus":
    result = first - second
elif op == "multiply":
    result = first * second
elif op == "divide":
    result = first // second

print(result)