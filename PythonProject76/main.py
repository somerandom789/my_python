number = 0
try:
    number = 10 / 0
    print(f"True")

except Exception as ZeroDivisionError:
    print(f"Error: {ZeroDivisionError}")
print(f"Finish")





