# задача 484
# Виведіть таблицю розміром n × n, заповнену числами від 1 до n2 по спіралі,
# що виходить з лівого верхнього кута і закрученою за годинниковою стрілкою.
#
# Вхідні дані:
#
# 4
#
# Вихідні дані:
#
# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7

num = int(input("Enter number: "))
graph = []
for it in range(num):
    row = [0] * num
    graph.append(row)
top = 0
bottom = num - 1
left = 0
right = num - 1
current_num = 1
max_num = num * num
while current_num <= max_num
    for column in range(left, right + 1):
        graph[top][column] = current_num
        current_num += 1
    top += 1
    for row in range(top, bottom + 1):
            graph[row][right] = current_num
            current_num += 1
    right -= 1
    for col in range(right, left - 1, -1):
        graph[bottom][col] = current_num
        current_num += 1
    bottom -= 1
    for row in range(bottom, top - 1, -1):
        graph[row][left] = current_num
        current_num += 1
    left += 1
for row in graph:
    print(*row)







