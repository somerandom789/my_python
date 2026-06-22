# задача 434
# Напишіть програму для отримання частини рядка URL, що позначає назву ресурсу.
#
# Вхідні дані:
#
# https://www.namesite.com/folder/index.html
#
# Вихідні дані:
#
# index.html

user_url = input("Enter your URL: ").split("/")
resource_name = user_url[-1]
print("Result:", resource_name)